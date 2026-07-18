# Referance Folder Overview Guide

## 1. Purpose of this folder

The `Referance` folder is acting as the **knowledge base and reverse-engineering package** for the Dominus ecosystem and for the TFM that describes it.

It contains four different kinds of assets:

1. **The written TFM source material**
2. **The diagrams extracted from that TFM**
3. **The real code repositories that implement the system**
4. **A helper script to restore those repositories on another machine**

This matters because the folder is not just "documentation" and not just "code".
It is a **bridge between theory and implementation**.

If you want to understand the project well enough to rebuild it as a new and stronger version, this folder gives you:

- the academic narrative;
- the architecture diagrams;
- the actual implementation;
- the contracts shared between components;
- the client-side SDK abstraction;
- the bootstrap script to recreate the local dependency set.

## 2. The big picture: how all pieces fit together

At a high level, the Dominus ecosystem is split into three software repositories plus one thesis document:

- `dominus-broker`
- `dominus-sdk`
- `dominus-proto-definition`
- `TFM_v1.md` / `TFM_v1.docx`

They map to four different responsibilities:

| Piece | What it is | Why it exists |
|---|---|---|
| `dominus-broker` | The running backend service | It is the actual server that routes messages, exposes gRPC APIs, talks to Redis, and exposes monitoring |
| `dominus-sdk` | A client/server helper layer in Go | It reduces boilerplate for applications that need to talk to the broker |
| `dominus-proto-definition` | The shared contract repository | It defines the protobuf messages and gRPC services used by broker and SDK |
| `TFM_v1.*` | The academic explanation of the system | It explains the problem, architecture, rationale, and implementation decisions in thesis format |

The design intention is clear:

- **The proto repo** defines the language.
- **The broker repo** implements the server.
- **The SDK repo** makes consumption easier for client applications.
- **The TFM** explains why the system was designed this way.

This separation exists for a good reason:

- contracts evolve differently from runtime logic;
- SDK concerns differ from server concerns;
- academic documentation should not be the only source of truth;
- diagrams and narrative help humans, while protos and code help machines.

## 3. Top-level inventory of `Referance`

Current top-level contents:

- `Attachments/`
- `dominus-broker/`
- `dominus-sdk/`
- `dominus-proto-definition/`
- `clone-dominus-deps.sh`
- `TFM_v1.docx`
- `TFM_v1.md`

Each one has a different role.

## 4. `TFM_v1.md`

### What it is

`TFM_v1.md` is a Markdown version of the thesis draft or thesis source material describing the Dominus system.

### What it does

It documents:

- the problem domain;
- the state of the art;
- the project objectives;
- the architecture decisions;
- the implementation approach;
- the testing/evaluation intention;
- the bibliography behind the project.

### Why it exists

This file exists because the system is not just a codebase. It is also an academic project.
The thesis needs to justify:

- why a hybrid broker is needed;
- why gRPC is used for real-time communication;
- why Redis is used as temporary storage;
- why fan-in and fan-out patterns matter;
- why idempotency is necessary;
- why a clean or hexagonal architecture helps.

### Why it matters to you

If you are rebuilding the project, `TFM_v1.md` is the **conceptual map**.
It tells you what the author believed the system should do and how they justified it.

That does not make it perfect.
In fact, it is useful precisely because it contains both:

- strong ideas worth keeping;
- weak spots worth correcting in a new version.

### What is valuable inside it

The most useful parts are:

- the system goal: a hybrid messaging broker;
- the distinction between synchronous and asynchronous communication;
- the role of gRPC streams;
- the role of Redis in queue-like flows;
- the mention of idempotency;
- the architectural intention around clean/hexagonal principles.

### What is weak or unstable inside it

You should not treat it as unquestionable truth.
It contains signs of draft-stage material:

- leftover template content;
- uneven source quality;
- some claims that are more blog-level than research-grade;
- some formatting artifacts;
- at least one placeholder-like figure section near the end.

### Practical reading strategy

Use this file to answer:

- What problem was being solved?
- What exact capabilities were envisioned?
- What arguments were used to justify the design?

Do not use it as final wording for your new work.

## 5. `TFM_v1.docx`

### What it is

`TFM_v1.docx` is the editable Word version of the thesis document.

### What it does

It serves as the likely authoring format for the thesis.
The Markdown file is easier to inspect in a repository, but the `.docx` is usually the format used for:

- institutional formatting;
- page layout;
- figures and captions;
- submission workflow;
- direct academic editing.

### Why it exists

A thesis often has to be delivered in Word or PDF-ready layout.
The `.docx` version is the real "editable deliverable" while the `.md` is the repository-friendly textual representation.

### Why it matters

If you want to understand content, the Markdown file is better.
If you want to preserve academic formatting, the `.docx` matters more.

### Good practice

Treat `TFM_v1.md` as the analysis source and `TFM_v1.docx` as the formatted source.

## 6. `Attachments/`

### What it is

`Attachments/` stores the images referenced by `TFM_v1.md`.

### What it does

It contains the visual support for the thesis:

- cover image or title figure;
- system-level architecture diagrams;
- directory structure diagram;
- communication diagrams;
- Redis interaction diagrams;
- log structure figure;
- one formatting/template example figure.

### Why it exists

Markdown references images by path.
Without this folder, `TFM_v1.md` would lose the diagrams that explain the system visually.

### Why it matters

The code shows implementation details, but the diagrams reveal the author's mental model.
That is especially useful when you want to rebuild the same idea without copying the same text.

### Attachment-by-attachment explanation

| File | Referenced as | What it likely represents | Why it exists |
|---|---|---|---|
| `TFM_v1.png` | Cover image at line 1 of `TFM_v1.md` | Front page or exported thesis header image | Visual presentation of the thesis |
| `TFM_v1 1.png` | Figure 1 | General system scheme with producers, broker, consumers | Explains the macro architecture simply |
| `TFM_v1 2.png` | Figure 2 | Broker architecture diagram | Shows the internal layers/components of the broker |
| `TFM_v1 3.png` | Figure 3 | Directory structure | Connects conceptual architecture to repository organization |
| `TFM_v1 4.png` | Figure 4 | Component diagram | Explains how broker-side elements collaborate in one communication path |
| `TFM_v1 5.png` | Figure 5 | Communication diagram | Shows request/response or stream behavior between actors |
| `TFM_v1 6.png` | Figure 6 | Redis-related component diagram | Explains how Redis participates in async messaging |
| `TFM_v1 7.png` | Figure 7 | Redis-related communication diagram | Shows message movement through Redis-backed flows |
| `TFM_v1 8.png` | Figure 8 | Log structure | Documents the shape of log records for observability |
| `TFM_v1 9.png` | Figure 9 | Formatting example figure | Looks like a template/example artifact rather than domain architecture |

### Why the images are important for reconstruction

These files help answer:

- What did the original author think the boundaries were?
- Which layers were considered core versus infrastructure?
- Was the broker imagined as a router, a queue manager, or both?
- How was Redis positioned: storage, coordination, or both?

That is critical when building a new version, because many architectural mistakes happen when teams inherit words but not the original model.

## 7. `clone-dominus-deps.sh`

### What it is

This is a restoration script for the three Dominus repositories.

### What it does

It:

- locates its own directory;
- clones each repository if missing;
- pulls the latest changes if the directory already exists.

The repositories it manages are:

- `dominus-broker`
- `dominus-sdk`
- `dominus-proto-definition`

### Why it exists

This script exists to solve a workflow problem:

- you want these repositories locally for study and implementation;
- you do not want the cloned directories tracked in your own repository;
- you still want a repeatable setup process on another machine.

So the script gives you **reproducible local restoration without polluting repository history**.

### Why it matters

This is a small file, but it carries an important design idea:

the `Referance` folder is not only archival, it is also **self-reconstructing**.

That is useful for:

- onboarding another collaborator;
- restoring a fresh workstation;
- documenting external dependencies without vendoring them into your main repo.

### Why the script uses clone-or-update logic

It does not only clone because that would fail on second execution.
It does not only pull because the directory may not exist.

So it supports both states:

- first-time setup;
- incremental refresh.

That is the right behavior for a portable utility script.

## 8. `dominus-proto-definition/`

### What it is

This repository is the **contract layer** of the whole system.

### What it does

It defines:

- the protobuf message shapes;
- the gRPC service interfaces;
- the generated Go code derived from those contracts.

### Why it exists as a separate repository

Separating contracts from implementation is a strong design choice because:

- the broker and the SDK both depend on the same service definitions;
- generated code should come from a single source of truth;
- contract versioning should be explicit;
- server and clients should not maintain duplicate protocol definitions.

If the broker and SDK each carried their own copy of `.proto` files, drift would eventually happen.
This repo avoids that drift.

### The most important file: `proto/dominus.proto`

This is the real center of the repo.

It defines six message types:

- `StreamRequestMessage`
- `StreamResponseMessage`
- `ProducerRequest`
- `ProducerResponse`
- `ConsumerRequest`
- `ConsumerResponse`

It also defines two services:

- `BrokerAPI`
- `SqsAPI`

### Why these messages exist

The contract reflects the hybrid nature of the system.

#### Real-time side

`StreamRequestMessage` and `StreamResponseMessage` are used for streaming communication.

Key design clues:

- `subscribers` is part of the request;
- `payload` is raw `bytes`.

This means the broker is not enforcing a rich domain schema at the contract level.
Instead, it is acting more like a **transport/routing layer**.

Why that matters:

- it keeps the broker generic;
- it lets clients send arbitrary binary payloads;
- it avoids locking business semantics into the broker contract.

The downside:

- schema meaning moves out to client agreement;
- payload validation becomes weaker unless another layer exists.

#### Queue side

`ProducerRequest` and `ProducerResponse` model enqueue-like behavior.

`ConsumerRequest` and `ConsumerResponse` model pull-based consumption and acknowledgment.

Important fields:

- `worker_id`
- `message_id`
- `group_id`
- timestamp/date

These exist because async processing needs:

- worker identity;
- consumer-group context;
- message identity for ack;
- traceable time of creation/delivery.

### Why there are two services

The system could have forced everything through one service, but it does not.

That split is deliberate:

- `BrokerAPI` is for streaming-oriented real-time flows.
- `SqsAPI` is for queue-style asynchronous flows.

This separation is good because the communication patterns are fundamentally different:

- stream lifecycle and backpressure for `BrokerAPI`;
- request/consume/ack semantics for `SqsAPI`.

Keeping them separate makes both code and reasoning cleaner.

### Generated files

- `dominus/dominus.pb.go`
- `dominus/dominus_grpc.pb.go`

These are generated artifacts, not hand-authored business logic.

They exist because Go code needs typed request/response structures and service bindings derived from protobuf.

### Supporting proto tool files

- `proto/buf.yaml`
- `proto/buf.gen.yaml`
- `proto/dominus-api.dsc`

These exist to support proto toolchain workflows such as:

- generation;
- schema management;
- descriptor export.

### Important caveat

The README of this repo appears generic and partially incorrect for the actual project.
It reads like a copied template in places.

That tells you something useful:

- the repo's real source of truth is the `.proto` file and generated Go code;
- the README itself should not be trusted blindly.

## 9. `dominus-sdk/`

### What it is

This repository is a **Go convenience layer** for interacting with the Dominus broker.

### What it does

It wraps low-level gRPC usage into higher-level helpers for:

- broker streaming operations;
- queue-like producer/consumer/ack calls;
- optional server registration;
- auth metadata attachment;
- TLS/insecure client setup.

### Why it exists

Without an SDK, every consuming application would need to repeat:

- gRPC dial configuration;
- TLS setup;
- metadata injection;
- interceptor setup;
- client creation patterns;
- validation rules.

That would lead to:

- inconsistent client behavior;
- more copy-paste;
- easier mistakes around security and connection setup.

So the SDK exists to standardize and reduce friction.

### Core design idea

The SDK is not the protocol source.
It is not the server.
It is a **developer ergonomics layer** on top of the proto definitions.

That is why it depends on `dominus-proto-definition` instead of redefining messages itself.

### Main public concepts

From the docs and source, the key types are:

- `DominusConfig`
- `Broker`
- `Sqs`
- `ServerOption`
- `BrokerRegister`

### Why these types exist

#### `DominusConfig`

This exists to centralize broker client setup:

- subscriber list;
- broker address;
- auth token;
- TLS or insecure mode.

Why this matters:

- it gives one place to validate inputs;
- it creates clients in a repeatable way;
- it reduces setup noise in application code.

#### `Broker`

This exists to expose real-time broker stream operations in a friendlier way than raw generated stubs.

Why it matters:

- stream setup code is verbose in raw gRPC;
- the SDK hides some of that complexity;
- subscribers are attached consistently.

#### `Sqs`

This exists to expose the async API in a simple unary-call style.

Why it matters:

- queue semantics should feel different from streaming semantics;
- producer/consumer/ack are conceptually separate operations;
- the SDK keeps them grouped under one client-side abstraction.

#### `ServerOption`

This exists because some applications may want to embed compatible server behavior or register services with consistent auth and TLS setup.

#### `BrokerRegister`

This exists to make server registration less repetitive when working with the broker service.

### Important implementation details from source

#### `broker_client_factory.go`

The broker client factory validates:

- subscribers are not empty;
- each subscriber passes URI rules;
- the broker address passes URI rules;
- token is not empty.

Why it does this:

- fail early;
- prevent malformed routing targets;
- stop unusable client setup before network calls begin.

This is defensive API design.

#### `sqs_client_factory.go`

The SQS client factory validates:

- broker address;
- API token;
- idempotency key.

Why it asks for idempotency:

because unary queue-like operations are the place where duplicate submission control is expected in this design.

#### `rules.go`

The SDK uses a regex-based URI validator.

Why that exists:

- the system expects a constrained set of target formats;
- the author wanted to reject invalid connection inputs before runtime.

Why it can also be problematic:

- regex-based network validation can be too strict;
- docs already mention edge cases such as `localhost` not matching.

That tells you the SDK values strictness, but maybe at the cost of usability.

### Repository structure

Important paths:

- `dominus/` - implementation package
- `doc/` - operational and usage documentation
- `README.md` - quick overview
- `go.mod` - module definition and dependency pinning

### Why the docs are important here

The SDK docs are unusually valuable because SDK behavior often contains assumptions that are not obvious from type names alone.

For example:

- panic behavior on invalid setup;
- connection lifecycle caveats;
- metadata and security expectations;
- TLS versus insecure initialization differences.

### Why this repo matters to your rebuild

If you rebuild the project from scratch, this repo tells you:

- how the ecosystem was expected to be consumed by applications;
- what developer experience the original author was aiming for;
- which responsibilities were intentionally kept out of the broker core.

It is effectively the "consumer-facing architecture" of the system.

## 10. `dominus-broker/`

### What it is

This is the actual **runtime server application**.

### What it does

It combines several concerns into one service:

- gRPC broker streaming
- gRPC queue-like messaging
- Redis-backed async memory
- idempotency checks
- HTTP monitoring endpoints
- metrics and telemetry
- optional TLS

### Why it exists

This repo is where the thesis stops being an idea and becomes a system.

It exists to implement the hybrid broker promise:

- real-time streaming over gRPC;
- async queue-style processing through Redis;
- one runtime that bridges both.

### Why the architecture is split into layers

The repo layout strongly signals a layered or clean architecture style:

- `internal/domain`
- `internal/application`
- `internal/infrastructure`
- `internal/bootstraps`

This separation exists to avoid coupling business orchestration directly to infrastructure libraries.

That is important because the broker uses many external technologies:

- gRPC
- Redis
- fasthttp
- Prometheus
- OpenTelemetry

If all of that were mixed directly in handlers, the code would become hard to test and harder to evolve.

### Entry point: `cmd/api/main.go`

This is the executable entry point.

What it does:

- parses CLI flags;
- decides production mode or not;
- optionally shows a banner;
- calls `bootstraps.RunApp(...)`.

Why it is so small:

- entrypoints should stay minimal;
- startup orchestration belongs elsewhere;
- this makes testing and maintenance easier.

### Configuration: `config/config.go`

This file defines the configuration model:

- gRPC config
- REST config
- certificate config
- Redis config
- log config

Why it exists:

- one typed shape for startup configuration;
- validation before server boot;
- separation between config format and runtime wiring.

Why `NewConfig()` reads JSON from environment:

- production friendliness;
- container compatibility;
- fail-fast startup.

Why that is good:

- explicit required fields;
- early crash if configuration is broken.

Why that is also risky:

- startup is unforgiving;
- malformed config causes panic instead of graceful recovery;
- development path assumptions can be fragile.

### Bootstrap wiring: `internal/bootstraps/bootstraps.go`

This file is one of the most important in the whole system.

What it does:

- builds config;
- creates logging;
- configures metrics;
- creates Redis checker and memory adapters;
- creates gRPC interceptors and middleware;
- creates use cases;
- registers gRPC APIs;
- creates REST monitor endpoints;
- starts both servers;
- handles shutdown.

Why it exists:

This is the **composition root**.
It is the place where abstractions become concrete implementations.

That is exactly where bootstrapping should happen.

Why this matters:

- you can reason about the dependency graph in one place;
- the rest of the code can depend on interfaces and use cases;
- startup complexity is isolated from domain/application code.

### Domain layer: `internal/domain`

What it contains:

- entities
- repository interfaces

Why it exists:

The domain layer defines the minimal conceptual model without binding to Redis or gRPC directly.

This is useful because the system wants infrastructure to be swappable.

The domain is intentionally thin here.
That means the project is more of an **integration-heavy transport system** than a domain-rich business system.

### Application layer: `internal/application/usecases`

What it contains:

- broker use cases
- SQS-like use cases
- DTOs
- factories

Why it exists:

This is where orchestration happens.
Not low-level transport, not raw persistence.

Examples of what belongs here:

- how a stream request gets handled;
- how producer/consumer/ack flows are coordinated;
- how repository ports are invoked.

Why this is valuable:

- one place for use-case behavior;
- easier unit testing with mocks;
- cleaner separation from infrastructure.

### Infrastructure layer: `internal/infrastructure`

This is where the real technology integrations live.

Main subareas:

- `grpc/inbound`
- `grpc/outbound`
- `grpc/middlewares`
- `redis/cchecker`
- `redis/cmemory`
- `fasthttp/inbound`
- `fasthttp/middlewares`
- `event`
- `enum`

#### `grpc/inbound`

What it does:

- receives incoming gRPC calls from clients;
- maps proto requests to internal contexts/use cases;
- registers service handlers.

Why it exists:

The broker should not put orchestration logic directly inside generated gRPC handlers.
Inbound adapters translate transport calls into application-layer actions.

The file `broker_v1.3.7.go` is a good example:

- it receives the gRPC stream call;
- logs the request;
- maps it into internal context;
- calls the broker use case;
- converts the result into gRPC status behavior.

That is exactly what an adapter should do.

#### `grpc/outbound`

What it does:

- sends broker messages out to subscribers over gRPC.

Why it exists:

The broker is not just a server receiving traffic.
It also acts as a dispatcher to other subscriber endpoints.

This outbound layer exists so fan-out behavior is isolated from the use-case layer.

#### `redis/cchecker`

What it does:

- manages idempotency keys in Redis.

Why it exists:

Duplicate request protection is a cross-cutting concern.
Redis is being used as a fast shared state store for this.

It is separated because:

- idempotency logic should not be mixed into every handler manually;
- Redis operations should remain behind a port-like abstraction.

#### `redis/cmemory`

What it does:

- implements queue-like message persistence and retrieval via Redis Streams.

Why it exists:

This is the async memory part of the hybrid broker.
It provides:

- message storage;
- consumer group reads;
- acknowledgments.

Without this adapter, the broker would only be a real-time stream router.
With it, the broker also supports delayed or decoupled processing.

#### `fasthttp/inbound` and `fasthttp/middlewares`

What they do:

- expose monitor/health/metrics endpoints;
- protect those endpoints with token and host filtering middleware.

Why they exist:

The project needs operational visibility.
Using a separate lightweight HTTP layer keeps observability endpoints apart from the gRPC API surface.

### Redis role in the broker

From docs and code, Redis is used in two logically separate ways:

- as a stream-backed memory queue;
- as an idempotency key store.

Why separate DB indexes are used:

- queue data and deduplication keys have different purposes;
- separation reduces accidental collision or operational confusion;
- cleanup and TTL logic differ.

This is a pragmatic infrastructure design choice.

### Monitoring and observability

The broker includes:

- Prometheus metrics;
- OpenTelemetry gRPC instrumentation;
- logging;
- a REST monitor surface.

Why this matters:

distributed messaging systems are hard to debug without visibility.

The author clearly expected:

- concurrency;
- transient failures;
- async flows;
- the need to inspect runtime behavior.

That is why observability is treated as a first-class concern rather than an afterthought.

### Terraform and local infrastructure

The `terraform/` directory defines a local stack using Docker provider resources.

What it includes conceptually:

- Dominus broker container;
- Redis;
- sidecar;
- Prometheus;
- Grafana;
- shared modules for image/network/container/volume.

Why it exists:

- repeatable local environment;
- easier demo and testing setup;
- infrastructure as code for development stack.

This is important because the project is more than a single binary.
It needs surrounding services to demonstrate real behavior.

### Tests and mocks

The repo contains:

- `tests/cases/`
- `tests/integration/`
- `mocks/`

Why they exist:

- unit-like validation of layers and use cases;
- integration coverage for streaming and SQS-style flows;
- mock-based isolation where real services are not needed.

This indicates the project is trying to validate both:

- correctness of local logic;
- behavior of cross-component flows.

### Documentation folder inside broker

The `doc/` directory is substantial and important.
It is effectively the implementation handbook.

Key topics:

- streaming flows;
- concurrency;
- configuration;
- gRPC security;
- Redis adapters;
- SQS use cases;
- HTTP monitoring;
- testing;
- trade-offs;
- coverage;
- Terraform.

Why it exists:

The broker is complex enough that the code alone is not enough for fast onboarding.
This repo tries to preserve architectural reasoning close to the implementation.

### Important engineering trade-offs revealed by the docs

The `tradeoffs.md` file is especially valuable because it explains not only what was built, but what compromises were knowingly made.

Examples:

- per-message goroutine fan-out for speed, at the cost of scalability risk;
- asynchronous idempotency writes, at the cost of race windows;
- optional TLS fallback, at the cost of possibly insecure startup if certs are absent;
- thin domain layer, at the cost of some boilerplate for abstraction.

That is excellent material for a rebuild because it tells you:

- what to preserve;
- what to harden;
- where the original design already knew its own limitations.

## 11. Relationship between the three code repositories

The dependency direction is conceptually this:

`dominus-proto-definition` -> used by `dominus-broker`

`dominus-proto-definition` -> used by `dominus-sdk`

`dominus-sdk` -> intended to be used by external client applications

`dominus-broker` -> intended to be deployed as the central messaging service

This is a healthy dependency direction because:

- contracts are lowest-level shared truth;
- the broker implements the contracts;
- the SDK consumes the same contracts;
- clients depend on the SDK rather than re-implementing wire behavior.

This avoids circular ownership of protocol meaning.

## 12. Why the architecture is intellectually coherent

Even if parts of the docs are rough, the overall decomposition is coherent.

The system is trying to solve a real design tension:

- low-latency real-time interaction;
- decoupled asynchronous processing;
- transport efficiency;
- manageable infrastructure complexity.

The chosen answer is:

- gRPC streams for live communication;
- Redis-backed queue behavior for decoupled async;
- protobuf for explicit contracts;
- SDK for usability;
- observability for operational control.

That is a reasonable architecture for a thesis-scale experimental broker.

## 13. Where each item is most useful

| Item | Best used for |
|---|---|
| `TFM_v1.md` | Understanding the original reasoning and academic framing |
| `TFM_v1.docx` | Recovering final formatting and formal thesis presentation |
| `Attachments/` | Understanding the author’s visual architecture model |
| `dominus-proto-definition/` | Understanding the wire contract and service surface |
| `dominus-sdk/` | Understanding intended client consumption patterns |
| `dominus-broker/` | Understanding the real runtime system and its internal architecture |
| `clone-dominus-deps.sh` | Reproducing the local study environment on another machine |

## 14. Best reading order if you are onboarding

If someone new joins the project, the most efficient reading order is:

1. Read `TFM_v1.md` sections for introduction, problem, and architecture.
2. Open `Attachments/` mentally through the figure references in `TFM_v1.md`.
3. Read `dominus-proto-definition/proto/dominus.proto`.
4. Read `dominus-broker/README.md`.
5. Read `dominus-broker/internal/bootstraps/bootstraps.go`.
6. Read `dominus-broker/doc/tradeoffs.md` and `doc/redis.md`.
7. Read `dominus-sdk/README.md` and `doc/overview.md`.

Why this order works:

- concept first;
- protocol second;
- runtime third;
- ergonomics fourth.

That sequence makes the implementation easier to understand.

## 15. Rebuild implications

If your goal is to rebuild this project as a new, stronger version, each item in `Referance` answers a different rebuild question:

| Rebuild question | Best source |
|---|---|
| What was the original problem? | `TFM_v1.md` |
| What was the intended architecture? | `TFM_v1.md` + `Attachments/` |
| What is the actual protocol surface? | `dominus-proto-definition/proto/dominus.proto` |
| How does the runtime really work? | `dominus-broker/` |
| How were clients expected to consume it? | `dominus-sdk/` |
| How do I recreate this environment elsewhere? | `clone-dominus-deps.sh` |

## 16. Final assessment of the folder

`Referance` is not a random dump.
It is a layered reference package with four distinct roles:

- **academic explanation**
- **visual explanation**
- **technical implementation**
- **environment restoration**

That makes it unusually valuable.

The main caution is that not every artifact has the same reliability level:

- most reliable for protocol truth: `dominus.proto`
- most reliable for runtime behavior: `dominus-broker` source
- most reliable for developer intent: broker and SDK docs together
- most useful for original rationale: `TFM_v1.md`
- least trustworthy in places: some README/template sections, especially in the proto repo and the tail of the TFM

If you use the folder with that hierarchy in mind, it becomes a very strong base for producing:

- a new Activity 1 state-of-the-art document;
- a cleaner project plan;
- a modernized implementation;
- a better defended TFM later.
