# Dominus Broker Deep Overview Guide

## 1. What this guide is for

This guide explains `Referance/dominus-broker` as a standalone system.

The goal is to make the broker understandable without having to jump randomly between the TFM, the README, the proto repo, and the source code.

It focuses on:

- what the broker does;
- how requests move through the code;
- why the folders are separated the way they are;
- where gRPC, Redis, HTTP monitoring, security, telemetry, tests, and Terraform fit;
- which design decisions are strong;
- which parts should be treated carefully if the project is rebuilt.

## 2. One-sentence definition

`dominus-broker` is a Go service that exposes a hybrid messaging broker over gRPC: one side handles real-time streaming fan-out/fan-in behavior, and the other side handles queue-style asynchronous messaging backed by Redis Streams.

## 3. What problem the broker is trying to solve

The project is trying to combine two communication needs that are usually handled by separate tools:

1. **Real-time communication**

   Services need persistent, low-latency message flow. This is handled with gRPC streaming.

2. **Asynchronous queue-like communication**

   Producers and consumers need to be decoupled. A producer can submit a message, a consumer can later request it, and an ack can confirm processing. This is handled with Redis Streams.

The broker attempts to sit between both worlds.

It is not just a wrapper around Redis, and it is not just a raw gRPC server. It is a coordinated runtime that provides:

- `BrokerAPI` for streaming;
- `SqsAPI` for queue-style operations;
- Redis-backed message storage;
- Redis-backed idempotency checks;
- monitoring endpoints;
- metrics and tracing hooks;
- a layered internal structure.

## 4. Relationship to the other Dominus repositories

`dominus-broker` depends on the other repositories conceptually like this:

| Repository | Role for the broker |
|---|---|
| `dominus-proto-definition` | Provides generated protobuf messages and gRPC service interfaces |
| `dominus-sdk` | Provides client-side helpers that external apps can use to call this broker |
| `dominus-broker` | Implements the actual runtime server |

The broker should not redefine message contracts locally.
It imports the generated proto package from `dominus-proto-definition`.

That keeps the protocol as a separate source of truth.

## 5. Main runtime surfaces

The broker exposes two network surfaces:

| Surface           | Technology               | Main purpose                        |
| ----------------- | ------------------------ | ----------------------------------- |
| gRPC server       | `google.golang.org/grpc` | Broker streaming and SQS-style APIs |
| REST/HTTP monitor | `fasthttp`               | Health and metrics endpoints        |

The gRPC surface is the product.
The HTTP surface is operational support.

This distinction matters because clients should use gRPC for application behavior and HTTP only for monitoring.

## 6. Top-level repository structure

Important paths:

| Path                       | Purpose                                           |
| -------------------------- | ------------------------------------------------- |
| `cmd/api/`                 | Executable entry point                            |
| `config/`                  | Typed configuration model and validation          |
| `internal/bootstraps/`     | Runtime composition root                          |
| `internal/domain/`         | Entity and port definitions                       |
| `internal/application/`    | Broker and SQS use cases                          |
| `internal/infrastructure/` | gRPC, Redis, HTTP, logging, constants             |
| `doc/`                     | Technical implementation documentation            |
| `tests/`                   | Unit-style and integration tests                  |
| `mocks/`                   | Generated mocks for interfaces                    |
| `terraform/`               | Local infrastructure stack                        |
| `env/`                     | Development and production config examples        |
| `Makefile.ps1`             | Windows automation for test/build/terraform tasks |
| `Dockerfile`               | Container image definition                        |

The layout follows a clean/hexagonal style.
The inner code defines what the system needs, while infrastructure code provides concrete implementations.

## 7. Architectural mental model

The broker has four main layers:

| Layer             | Folder                          | Responsibility                                   |
| ----------------- | ------------------------------- | ------------------------------------------------ |
| Entry/composition | `cmd`, `internal/bootstraps`    | Start the app and wire concrete dependencies     |
| Domain            | `internal/domain`               | Define entities and repository interfaces        |
| Application       | `internal/application/usecases` | Orchestrate broker and queue behavior            |
| Infrastructure    | `internal/infrastructure`       | Implement gRPC, Redis, HTTP, logging, middleware |

The important idea is dependency direction.

Application code should depend on interfaces.
Infrastructure code implements those interfaces.
Bootstrapping connects them.

This makes the code easier to test because application behavior can be exercised with mocks instead of live Redis or real gRPC clients.

## 8. Startup flow

The broker starts from:

`cmd/api/main.go`

That file does very little:

- defines `-prod` and `-banner` flags;
- parses CLI arguments;
- calls `bootstraps.RunApp(...)`.

This is good design because `main.go` stays thin.
The real wiring is delegated to:

`internal/bootstraps/bootstraps.go`

## 9. Bootstrap flow

`RunApp` is the composition root.

It does the following:

1. Reads configuration through `config.NewConfig()`.
2. Creates the logging/event adapter.
3. Creates shutdown signal handling.
4. Checks whether certificate files exist.
5. Builds  and gRPC metrics collectors.
6. Starts the REST monitor server.
7. Starts the gRPC server.
8. Prints runtime information.
9. Waits for OS signal or context cancellation.
10. Shuts down REST and gRPC.

The gRPC server setup inside `gRPCServer(...)` is the most important part.

It wires:

- Redis checker client for idempotency;
- Redis memory client for queue messages;
- server-side gRPC middleware;
- client-side gRPC interceptors;
- outbound gRPC broker client;
- broker use case;
- SQS use case;
- gRPC API registrations;
- reflection;
- TCP listener.

That makes `bootstraps.go` the best file to read when you want to understand the runtime dependency graph.

## 10. Configuration model

Configuration lives in:

`config/config.go`

Main config blocks:

| Config block | Purpose |
|---|---|
| `GrpcConfig` | gRPC port and API token |
| `RestConfig` | REST monitor port, API token, allowed origins |
| `CertConfig` | TLS cert/key/CA paths |
| `RedisConfig` | Redis host, port, DBs, stream, group, TTL, TLS |
| `LogConfig` | Logging mode and optional log URL |

`NewConfig()` reads JSON from the `APP_CONFIG` environment variable.

That means production startup expects config to be injected as environment JSON.

Why this approach exists:

- it works well in containers;
- it avoids hardcoded config files;
- it fails early when required fields are missing.

Trade-off:

- malformed config causes panic;
- large JSON blobs in environment variables can be awkward;
- local development must ensure `APP_CONFIG` exists or use the documented dev workflow.

## 11. TLS behavior

The broker checks whether configured cert files exist.

If cert, key, and CA files are present:

- gRPC server uses TLS;
- outbound gRPC client uses TLS;
- REST server uses HTTPS.

If files are missing:

- outbound gRPC uses insecure credentials;
- REST starts as HTTP;
- the gRPC server does not attach TLS credentials.

Why this exists:

- easier local development;
- no certificate setup required for a quick run.

Production concern:

- a missing certificate may silently downgrade the runtime to insecure transport.

For a hardened rebuild, make TLS mode explicit instead of inferring it only from file existence.

## 12. Domain layer

The domain layer is thin.

Important files:

- `internal/domain/entities/message.go`
- `internal/domain/repositories/broker.go`
- `internal/domain/repositories/sqs.go`

### `Message` entity

The `Message` entity stores:

- `Message []byte`
- `MessageId string`
- `CreatedAt time.Time`

`NewMessageWithID` creates an ID using current Unix milliseconds in Redis Stream format:

`<milliseconds>-0`

Why this matters:

Redis Streams use IDs with the shape `time-sequence`.
The broker aligns its message IDs with that model.

`SetMessageId` validates that a message ID has two numeric parts separated by `-`.

Why this exists:

- it prevents invalid ack IDs;
- it keeps the application layer from acknowledging malformed Redis stream IDs.

### Repository interfaces

`BrokerClient` defines outbound streaming behavior:

- `ClientStream`
- `ServerStream`
- `BidirectionalStream`

`MemoryClient` defines Redis queue behavior:

- `SendMessage`
- `GetMessage`
- `AckMessage`
- `Group`

`CheckerClient` defines idempotency behavior:

- `SaveConsumer`
- `CheckConsumer`

Why these interfaces exist:

- application code can use abstract ports;
- infrastructure code can implement those ports;
- tests can use mocks.

## 13. Application layer

Application use cases live in:

- `internal/application/usecases/broker/`
- `internal/application/usecases/sqs/`

This layer coordinates behavior but should not know Redis command details or raw gRPC implementation details.

## 14. Broker streaming use cases

Broker streaming use cases are in:

- `stream_client_conn_service.go`
- `stream_server_conn_service.go`
- `stream_bi_conn_service.go`

They orchestrate the three `BrokerAPI` RPC patterns.

### Client streaming flow

Source:

`internal/application/usecases/broker/stream_client_conn_service.go`

What happens:

1. The first inbound message is read.
2. Subscribers are extracted from that first message.
3. If there are no subscribers, the use case fails.
4. A payload channel is created.
5. Outbound `ClientStream` starts in a goroutine.
6. The first payload is sent to the channel.
7. Every subsequent inbound payload is forwarded to the same channel.
8. When inbound receive fails, the payload channel is closed and the context is cancelled.

Why the first message matters:

The subscriber list is treated as connection setup metadata.
Further messages are treated mainly as payload frames.

### Server streaming flow

Source:

`internal/application/usecases/broker/stream_server_conn_service.go`

What happens:

1. A single inbound request arrives with subscribers and initial payload.
2. Subscribers are validated.
3. A buffered response channel is created.
4. Outbound `ServerStream` is started for each subscriber.
5. Responses from subscribers are merged into the channel.
6. The inbound client receives payloads through `stream.Send`.
7. When outbound work signals closure, local channels are closed and the use case exits.

Why the buffer size depends on subscriber count:

The broker expects multiple subscribers to send responses concurrently.
A small buffer reduces immediate blocking while still keeping memory bounded by subscriber count.

### Bidirectional streaming flow

Source:

`internal/application/usecases/broker/stream_bi_conn_service.go`

What happens:

1. The first inbound message is read.
2. Subscribers are extracted.
3. `streamProv` carries provider payloads toward outbound subscriber streams.
4. `streamSub` carries subscriber payloads back to the inbound caller.
5. Outbound `BidirectionalStream` is started.
6. One goroutine keeps receiving provider messages and writes them to `streamProv`.
7. The main loop forwards subscriber responses from `streamSub` to the original gRPC stream.
8. A `closed` channel coordinates final shutdown with the outbound client.

Why this exists:

Bidirectional streaming is the broker's most complete real-time mode.
Both sides can send data over persistent streams.

Important caution:

Some internal docs describe a more elaborate channel lifecycle than the current source file shows.
For exact behavior, trust the source code first.
Use `doc/broker-streaming.md` as architecture context, not as a perfect line-by-line description.

## 15. Outbound gRPC adapter

Source:

`internal/infrastructure/grpc/outbound/client_v1.3.7.go`

This adapter implements `repositories.BrokerClient`.

It is the part of the broker that calls downstream subscriber URLs.

### Why it exists

The broker is not only an inbound server.
For streaming flows, it also becomes a gRPC client that connects to subscriber endpoints.

Keeping outbound behavior in infrastructure avoids leaking gRPC client mechanics into application use cases.

### ClientStream outbound behavior

For each subscriber URL:

- create or reuse a client-stream closure;
- send payloads to that stream;
- reconnect on error when possible;
- fan out each incoming message to all subscriber closures.

Design benefit:

- all subscribers receive the provider's payloads.

Trade-off:

- each message launches goroutines for fan-out;
- under high load this can create unbounded goroutine growth;
- subscriber backpressure is not strongly controlled.

### ServerStream outbound behavior

For each subscriber URL:

- create a gRPC client;
- call `ServerStream` with initial payload;
- receive payloads from the subscriber stream;
- forward those payloads into a merged channel;
- reconnect on errors.

Design benefit:

- the broker can aggregate responses from multiple downstream streams.

Trade-off:

- reconnect uses a tight millisecond ticker;
- repeated failures could create noisy retry behavior.

### BidirectionalStream outbound behavior

For each subscriber URL:

- connect to a bidirectional stream;
- send provider payloads to each subscriber;
- receive subscriber payloads;
- merge subscriber payloads back to the inbound caller;
- reconnect when needed.

Design benefit:

- full duplex behavior across many subscribers.

Trade-off:

- concurrency is complex;
- shared payload slices must be treated as read-only;
- connection lifecycle needs careful testing.

## 16. SQS-style use cases

The project calls this part `SqsAPI`, but it is not AWS SQS.
It is an SQS-like queue interface backed by Redis Streams.

Use cases live in:

- `internal/application/usecases/sqs/producer_service.go`
- `internal/application/usecases/sqs/consumer_service.go`
- `internal/application/usecases/sqs/ack_service.go`

### Producer flow

What happens:

1. Payload is read.
2. Empty payload is rejected.
3. A `Message` entity is created with generated Redis-style ID.
4. The message is sent through the `MemoryClient` port.

Why it exists:

Producer gives clients a simple way to enqueue data without managing Redis directly.

### Consumer flow

What happens:

1. Worker ID and group ID are read from the request.
2. The use case calls `MemoryClient.GetMessage`.
3. Redis Stream returns the next message for that consumer group.

Why it exists:

Consumers pull messages instead of passively receiving pushed messages.
That gives consumers control over processing pace.

### Ack flow

What happens:

1. Message ID is validated.
2. Group ID and worker ID are validated at inbound layer.
3. The use case calls `MemoryClient.AckMessage`.

Why it exists:

Ack tells Redis that a consumer group message was processed.
Without ack, pending entries remain unresolved.

## 17. gRPC inbound adapters

Inbound adapters live in:

- `internal/infrastructure/grpc/inbound/broker_v1.3.7.go`
- `internal/infrastructure/grpc/inbound/sqs_v1.3.7.go`

They implement generated gRPC server interfaces from `dominus-proto-definition`.

### Broker inbound adapter

Responsibilities:

- register `BrokerAPI`;
- receive streaming RPCs;
- wrap raw streams with mappers;
- call application broker use cases;
- convert errors into gRPC status responses;
- write logs.

Why it exists:

Application use cases should not depend directly on generated gRPC stream types.
The inbound adapter keeps transport details at the edge.

### SQS inbound adapter

Responsibilities:

- register `SqsAPI`;
- validate request fields;
- call SQS use cases;
- map domain message data to proto responses;
- return gRPC status errors on invalid input or failed operations.

Why validation appears here:

Some validation is transport/request-level validation.
For example:

- missing payload;
- missing worker ID;
- missing group ID;
- missing message ID.

That belongs close to the boundary because it protects the use case from malformed RPC requests.

## 18. Redis memory adapter

Source:

`internal/infrastructure/redis/cmemory/outbound.go`

This is the queue-like storage adapter.

It implements `MemoryClient`.

### What it does

It uses Redis Streams operations:

- `XADD` to produce messages;
- `XREADGROUP` to consume messages;
- `XACK` to acknowledge messages;
- `XGROUP CREATE MKSTREAM` to create the consumer group.

### Why Redis Streams are used

Redis Streams provide a lightweight append-only stream with consumer groups.
That is enough for a thesis-scale queue-like broker without deploying Kafka, RabbitMQ, or cloud SQS.

### Producer storage behavior

`SendMessage` marshals the domain message into JSON and stores it in Redis under a `payload` field.

Why JSON inside Redis Stream:

- the stream field can carry a serialized structure;
- it preserves message ID, created time, and payload together.

### Consumer behavior

`GetMessage` reads one message from the configured stream and consumer group.

Important parameters:

- `Group`
- `Consumer`
- `Streams: [streamID, ">"]`
- `Block: 100ms`
- `Count: 1`

Why `">"` matters:

It asks Redis for new messages not yet delivered to this consumer group.

### Ack behavior

`AckMessage` calls `XACK` with stream ID, group ID, and message ID.

Why this matters:

Ack completes the consumer-group lifecycle for a processed message.

## 19. Redis idempotency adapter

Source:

`internal/infrastructure/redis/cchecker/outbound.go`

This adapter implements `CheckerClient`.

### What it does

It stores idempotency keys in Redis with:

- prefix: `idempotency`
- mode: `NX`
- TTL in seconds from config

It also checks if a key already exists.

### Why it exists

Distributed systems often retry requests.
If a producer retries a request, the broker needs a way to detect duplicate logical operations.

The idempotency checker gives the gRPC middleware a shared memory of recently seen keys.

### Important limitation

The server middleware checks existence first and then saves the key asynchronously.

That means two concurrent requests using the same idempotency key can theoretically both pass before the async save completes.

For a stronger rebuild, use a synchronous atomic `SET NX` as the reservation step before calling the handler.

## 20. gRPC middleware and interceptors

Sources:

- `internal/infrastructure/grpc/middlewares/middlewares.go`
- `internal/infrastructure/grpc/middlewares/interceptors.go`

### Server-side middleware

The server-side middleware handles:

- API token validation;
- idempotency validation for unary calls;
- logging bridge for gRPC middleware.

API token validation:

- reads `x-api-key` metadata;
- hashes received token and configured token;
- compares them with constant-time comparison.

Why this exists:

- all gRPC calls require shared-secret authentication;
- constant-time comparison reduces timing leak risk.

Idempotency validation:

- reads `idempotency-header`;
- checks Redis for prior use;
- rejects duplicates;
- saves new keys with TTL.

Why unary only:

The middleware chain applies idempotency to unary interceptors.
Streaming calls use auth and metrics but not the same idempotency guard.

### Client-side interceptors

Outbound client interceptors attach API token metadata to broker-to-subscriber gRPC calls.

Why this exists:

Subscriber endpoints may apply the same API-key requirement.
The broker therefore authenticates itself when calling downstream services.

## 21. REST monitor API

Source:

`internal/infrastructure/fasthttp/inbound/monitor_api.go`

The monitor API exposes:

- `/health`
- `/metrics`

### `/health`

Returns a simple health response:

`Health ok`

Why it exists:

- liveness checks;
- quick local validation;
- container health checks.

### `/metrics`

Exports Prometheus-compatible metrics.

It collects:

- gRPC metrics from registered middleware;
- CPU percentage;
- memory usage percentage.

Why this exists:

Message brokers are operationally sensitive.
Latency, stream behavior, resource usage, and failures need visibility.

## 22. Logging and events

Sources:

- `internal/infrastructure/event/event.go`
- `internal/infrastructure/event/logs.go`

The logging abstraction is named `Event`.

It supports:

- writing structured log entries;
- adding a request correlation ID to context;
- selecting log output mode.

Log records contain:

- ID;
- description;
- operation name.

Why this exists:

The system crosses async and streaming boundaries.
Correlation IDs help connect related events across calls.

Current limitation:

`clientLog` is empty, so external log shipping appears planned but not implemented.

## 23. Constants and enums

Source:

`internal/infrastructure/enum/enum.go`

This file centralizes:

- log levels;
- metadata header names;
- status/error messages;
- Redis field names;
- project name;
- gRPC load-balancing config;
- idempotency constants.

Why it exists:

It avoids duplicating string literals across middleware, Redis, gRPC, and logging code.

Trade-off:

Some names contain spelling mistakes, and constants can become a mixed bag if too many unrelated concerns are placed in one file.

## 24. Tests

Tests are split into:

- `tests/cases/`
- `tests/integration/`

### `tests/cases`

These are focused tests for:

- application use cases;
- domain entities;
- Redis adapters;
- gRPC inbound/outbound adapters;
- fasthttp middleware;
- event logging;
- mappers.

Why this exists:

Each layer can be tested without always running the full stack.

### `tests/integration`

These validate larger flows:

- broker streaming flows;
- SQS-style producer/consumer/ack flows.

Why this exists:

Streaming systems can pass unit tests and still fail at channel, cancellation, or network boundaries.
Integration tests are necessary here.

### Mocks

`mocks/` contains generated mocks for:

- broker repositories;
- SQS repositories;
- use cases;
- DTOs;
- event logging.

Why this exists:

Mocks allow use cases and adapters to be tested without requiring live downstream systems.

## 25. Terraform and local stack

Terraform files live in:

`terraform/`

The local stack includes modules and dev resources for:

- broker container;
- Redis;
- sidecar;
- Prometheus;
- Grafana;
- Docker networks;
- volumes;
- images;
- containers.

Why it exists:

The broker depends on external infrastructure.
Terraform provides a repeatable way to run the surrounding stack locally.

For a team project, this is useful because everyone can recreate a similar environment.

## 26. Dockerfile and deployment shape

`Dockerfile` defines how to package the broker.

Together with Terraform, it supports this deployment shape:

1. Build broker image.
2. Start Redis.
3. Start broker container.
4. Expose gRPC and monitor ports.
5. Scrape metrics with Prometheus.
6. View dashboards in Grafana.

This confirms that the project is intended as a service, not just a library.

## 27. Internal docs

The `doc/` folder is an important companion to source code.

Important docs:

| Document | Why it matters |
|---|---|
| `broker-streaming.md` | Explains streaming design and channel lifecycle |
| `concurrency.md` | Captures concurrency and race detector concerns |
| `configuration.md` | Explains config model |
| `grpc-security.md` | Explains auth, idempotency, TLS, metrics |
| `redis.md` | Explains `cchecker` and `cmemory` |
| `sqs-use-cases.md` | Explains producer/consumer/ack flows |
| `http-monitor.md` | Explains monitor endpoints |
| `testing.md` | Explains test strategy |
| `tradeoffs.md` | Explains deliberate compromises |
| `terraform.md` | Explains local infrastructure |

Most valuable document:

`tradeoffs.md`

Why:

It describes known limits and intentional engineering choices.
That is exactly what you need when rebuilding the system.

## 28. Main request flows

### Flow A: Real-time client-stream fan-out

1. External client calls `BrokerAPI.ClientStream`.
2. Inbound gRPC adapter receives stream.
3. Mapper wraps stream into DTO interface.
4. Broker use case reads first request.
5. Subscribers are extracted.
6. Outbound broker client opens streams to subscriber URLs.
7. Payloads from external client are sent to all subscribers.
8. On inbound close/error, channel closes and context cancels.

### Flow B: Real-time server-stream aggregation

1. External client calls `BrokerAPI.ServerStream`.
2. Request includes subscribers and initial payload.
3. Broker use case creates a merged response channel.
4. Outbound client calls `ServerStream` on each subscriber.
5. Subscriber responses are merged.
6. External client receives stream responses.
7. Completion is signaled by outbound workers.

### Flow C: Real-time bidirectional stream

1. External client opens `BrokerAPI.BidirectionalStream`.
2. First message defines subscribers.
3. Provider payloads flow to subscribers.
4. Subscriber payloads flow back to the original client.
5. Outbound client manages per-subscriber bidirectional streams.
6. Context cancellation and channel closure coordinate shutdown.

### Flow D: Queue producer

1. External client calls `SqsAPI.Producer`.
2. gRPC unary middleware checks API token and idempotency.
3. Inbound adapter validates payload.
4. SQS producer use case creates `Message`.
5. Redis `cmemory` adapter writes to stream using `XADD`.
6. Client receives status response.

### Flow E: Queue consumer

1. External client calls `SqsAPI.Consumer`.
2. Middleware checks token and idempotency.
3. Inbound adapter validates worker ID and group ID.
4. SQS consumer use case calls memory port.
5. Redis `cmemory` uses `XREADGROUP`.
6. Response returns message ID, timestamp, and payload.

### Flow F: Queue ack

1. External client calls `SqsAPI.Ack`.
2. Middleware checks token and idempotency.
3. Inbound adapter validates message ID, group ID, worker ID.
4. SQS ack use case validates Redis-style message ID format.
5. Redis `cmemory` calls `XACK`.
6. Client receives ack response.

## 29. What the broker does well

Strong parts:

- Clear separation between proto contract and broker runtime.
- Thin entry point.
- Single composition root.
- Domain ports for Redis and outbound gRPC behavior.
- Explicit split between streaming API and queue-style API.
- Redis Streams are a pragmatic fit for a lightweight async queue.
- Observability is included early.
- Tests exist at both case and integration levels.
- Documentation captures trade-offs instead of pretending the design is perfect.

## 30. Risks and weaknesses to watch

Important concerns:

- Idempotency is not fully atomic under concurrent duplicate requests.
- Fan-out can create unbounded goroutines under high message rates.
- TLS fallback is implicit when cert files are missing.
- Some docs appear to drift from current source behavior.
- The domain is thin, so the architecture may be more integration-oriented than domain-driven.
- Retry loops can be aggressive.
- Some errors are mapped broadly to `codes.Aborted`.
- `clientLog` is not implemented.
- Config panics are practical for fail-fast startup but rough for controlled error reporting.
- API key auth is simple shared-secret auth, not identity-aware authorization.

## 31. What to improve in a rebuild

If this project is rebuilt as a stronger version, prioritize:

1. Make idempotency atomic with synchronous Redis `SET NX`.
2. Add bounded fan-out workers or backpressure controls.
3. Make TLS mode explicit: dev insecure, prod TLS-required.
4. Clarify retry policy with exponential backoff and limits.
5. Normalize gRPC status code mapping.
6. Strengthen config loading for dev and prod separately.
7. Add connection pooling/lifecycle management for outbound gRPC clients.
8. Replace shared raw `[]byte` payload assumptions with safer ownership rules.
9. Improve docs so they match current source.
10. Decide whether the broker is generic transport or domain-aware messaging.

## 32. Recommended reading order

Use this order to understand the broker quickly:

1. `README.md`
2. `cmd/api/main.go`
3. `internal/bootstraps/bootstraps.go`
4. `config/config.go`
5. `internal/domain/repositories/*.go`
6. `internal/domain/entities/message.go`
7. `internal/application/usecases/broker/*.go`
8. `internal/application/usecases/sqs/*.go`
9. `internal/infrastructure/grpc/inbound/*.go`
10. `internal/infrastructure/grpc/outbound/client_v1.3.7.go`
11. `internal/infrastructure/redis/cmemory/outbound.go`
12. `internal/infrastructure/redis/cchecker/outbound.go`
13. `doc/tradeoffs.md`
14. `doc/testing.md`

## 33. How this broker supports the TFM idea

The TFM describes a hybrid broker concept.
This repository implements that concept concretely:

- gRPC streaming proves the real-time side;
- Redis Streams prove the async queue side;
- API token middleware adds basic access control;
- idempotency middleware addresses duplicate unary calls;
- Prometheus and OpenTelemetry support observability;
- Terraform demonstrates local deployment;
- SDK/proto separation supports ecosystem reuse.

So `dominus-broker` is the implementation core of the thesis.

## 34. Final assessment

`dominus-broker` is a meaningful prototype of a hybrid messaging broker.

Its main strength is the combination of:

- explicit protobuf contracts;
- streaming gRPC;
- Redis-backed async consumption;
- layered code organization;
- operational tooling.

Its main weakness is that some production-grade guarantees are incomplete:

- idempotency is not fully atomic;
- fan-out has limited backpressure;
- TLS and retry behavior need hardening;
- docs and source should be synchronized.

For a new project based on the same idea, this repo should be used as a reference implementation and learning map, not as a final architecture to copy line by line.
