# Rust Web Scraper Platform

## Review of the Original Challenge

The original `03-Web-scrapping.md` describes a solid product idea, but it reads more like a product brief than an implementation guide. That is fine for brainstorming, but if you want to ship this as a portfolio project you need to tighten the technical direction.

### What is strong

- It covers real product concerns, not just scraping HTML.
- It includes authentication, job management, exports, logs, and documentation.
- It points toward a system that can grow into a SaaS-style platform.

### What is missing or too vague

- The file says "web scrapping"; the correct term is "web scraping".
- It does not define how selectors are stored.
- It does not define how jobs are executed in the background.
- It does not explain how retries, rate limiting, or job history should work.
- It does not define a data model.
- It does not mention legal and ethical scraping concerns such as `robots.txt`, site Terms of Service, or request throttling.
- It names Python and Node.js as examples, but Rust is a strong fit for this kind of IO-heavy backend.

### Portfolio-ready positioning

Instead of building "a scraper script", build **a backend-first scraping platform**:

- users authenticate
- users create scraping jobs
- a worker executes jobs asynchronously
- results are stored and exportable
- the API is documented
- a frontend can be added later without changing the core backend

That gives you a project that looks like a real product, not a tutorial clone.

---

## Recommended Project Direction

### Project name

Use a name that sounds like a product:

- `atlas-scrape`
- `forge-scraper`
- `harvest-rs`

I will use **`atlas-scrape`** in this guide.

### Why Rust for this project

Rust is a good choice because this system is:

- network-heavy
- concurrency-heavy
- reliability-sensitive
- likely to grow into multiple services later

Rust gives you:

- strong type safety
- efficient async execution with Tokio
- low memory overhead
- a clean path to split API and workers later

---

## Backend-First Architecture

Build the backend first, then grow into full stack.

### Phase 1

Single Rust backend application with:

- REST API
- PostgreSQL
- background worker loop
- scraping engine
- export endpoints

### Phase 2

Split responsibilities internally:

- API module
- worker module
- scraper module
- export module

Still one deployable binary, but cleaner boundaries.

### Phase 3

Grow into full stack:

- Rust API stays the source of truth
- Next.js, SvelteKit, or React frontend consumes the API
- frontend shows dashboard, logs, results, exports

This is the right order because the business logic belongs in the backend, not the UI.

---

## Recommended Rust Stack

### Core stack

- **Rust 2024 Edition**
  - https://doc.rust-lang.org/book/
- **Axum** for the HTTP API
  - https://docs.rs/axum/latest/axum/
- **Tokio** for async runtime and task scheduling
  - https://docs.rs/tokio/latest/tokio/
- **SQLx** for PostgreSQL access
  - https://docs.rs/sqlx/latest/sqlx/
- **Reqwest** for downloading pages
  - https://docs.rs/reqwest/latest/reqwest/
- **scraper** for CSS-selector based HTML parsing
  - https://docs.rs/scraper/latest/scraper/
- **Serde** for JSON serialization
  - https://docs.rs/serde/latest/serde/
- **Utoipa** for OpenAPI / Swagger docs
  - https://docs.rs/utoipa/latest/utoipa/
- **PostgreSQL**
  - https://www.postgresql.org/docs/current/index.html

### Helpful supporting crates

- `uuid` for IDs
- `chrono` for timestamps
- `thiserror` for typed errors
- `argon2` for password hashing
- `jsonwebtoken` for JWT auth
- `tracing` and `tracing-subscriber` for logs
- `csv` for CSV export
- `tower-http` for CORS, tracing, compression

---

## Product Features to Implement

### MVP

- sign up
- login
- create scraping job
- store selectors per job
- run a job manually
- save results
- export JSON and CSV

### Strong V1

- job schedules
- retries
- rate limits
- job logs
- job history
- user profile updates
- OpenAPI docs

### Full product direction

- MFA
- email notifications
- webhook delivery
- Google Sheets integration
- per-domain throttling
- proxy support
- headless browser support for JavaScript-heavy sites

Do not start with headless browsers. Start with plain HTML scraping first.

---

## Data Model

Use PostgreSQL from day one. This project has relationships, histories, and exports. SQL fits better than a document database here.

### Tables

#### `users`

- `id UUID PRIMARY KEY`
- `email TEXT UNIQUE NOT NULL`
- `username TEXT UNIQUE NOT NULL`
- `password_hash TEXT NOT NULL`
- `created_at TIMESTAMPTZ NOT NULL`
- `updated_at TIMESTAMPTZ NOT NULL`

#### `scrape_jobs`

- `id UUID PRIMARY KEY`
- `user_id UUID NOT NULL`
- `name TEXT NOT NULL`
- `target_url TEXT NOT NULL`
- `status TEXT NOT NULL`
- `schedule_cron TEXT NULL`
- `rate_limit_per_minute INT NULL`
- `retry_limit INT NOT NULL DEFAULT 3`
- `selectors JSONB NOT NULL`
- `transform_rules JSONB NULL`
- `created_at TIMESTAMPTZ NOT NULL`
- `updated_at TIMESTAMPTZ NOT NULL`

#### `job_runs`

- `id UUID PRIMARY KEY`
- `job_id UUID NOT NULL`
- `status TEXT NOT NULL`
- `started_at TIMESTAMPTZ NULL`
- `finished_at TIMESTAMPTZ NULL`
- `error_message TEXT NULL`
- `attempt_number INT NOT NULL`
- `pages_fetched INT NOT NULL DEFAULT 0`

#### `scraped_records`

- `id UUID PRIMARY KEY`
- `job_run_id UUID NOT NULL`
- `payload JSONB NOT NULL`
- `created_at TIMESTAMPTZ NOT NULL`

#### `job_logs`

- `id BIGSERIAL PRIMARY KEY`
- `job_run_id UUID NOT NULL`
- `level TEXT NOT NULL`
- `message TEXT NOT NULL`
- `created_at TIMESTAMPTZ NOT NULL`

### Why this model works

- `scrape_jobs` defines the repeatable configuration.
- `job_runs` tracks each execution attempt.
- `scraped_records` stores extracted data separately from job definitions.
- `job_logs` gives you auditability and debugging.

That separation matters in interviews and portfolio reviews.

---

## How Selectors Should Be Stored

Do not hardcode extraction logic in Rust for each site. Store selectors in the database as JSON.

Example:

```json
[
  {
    "field": "title",
    "selector": "h1.product-title",
    "attribute": null
  },
  {
    "field": "price",
    "selector": ".price-current",
    "attribute": null
  },
  {
    "field": "product_url",
    "selector": "a.buy-now",
    "attribute": "href"
  }
]
```

This keeps the scraper generic and reusable.

---

## Suggested Project Structure

Project name:

```text
atlas-scrape
```

Workspace structure:

```text
atlas-scrape/
├── Cargo.toml
├── .env
├── migrations/
│   ├── 0001_init.sql
│   └── 0002_indexes.sql
├── src/
│   ├── main.rs
│   ├── config.rs
│   ├── state.rs
│   ├── error.rs
│   ├── models/
│   │   ├── mod.rs
│   │   ├── user.rs
│   │   ├── job.rs
│   │   ├── run.rs
│   │   └── record.rs
│   ├── routes/
│   │   ├── mod.rs
│   │   ├── auth.rs
│   │   ├── profile.rs
│   │   ├── jobs.rs
│   │   └── exports.rs
│   ├── services/
│   │   ├── mod.rs
│   │   ├── auth_service.rs
│   │   ├── scraper_service.rs
│   │   ├── worker_service.rs
│   │   └── export_service.rs
│   ├── middleware/
│   │   ├── mod.rs
│   │   └── auth.rs
│   └── docs.rs
└── README.md
```

This is portfolio-friendly because it looks intentional and scalable.

---

## Step-by-Step Build Guide

## Step 1: Create the Rust Project

Create the project:

```powershell
cargo new atlas-scrape
cd atlas-scrape
```

### `Cargo.toml`

File: `atlas-scrape/Cargo.toml`

```toml
[package]
name = "atlas-scrape"
version = "0.1.0"
edition = "2024"

[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
sqlx = { version = "0.8", features = ["runtime-tokio-rustls", "postgres", "uuid", "chrono", "json"] }
reqwest = { version = "0.12", default-features = false, features = ["rustls-tls", "json", "gzip", "brotli"] }
scraper = "0.24"
uuid = { version = "1", features = ["v4", "serde"] }
chrono = { version = "0.4", features = ["serde"] }
thiserror = "2"
argon2 = "0.5"
jsonwebtoken = "9"
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
tower-http = { version = "0.6", features = ["cors", "trace", "compression-full"] }
csv = "1"
utoipa = { version = "5", features = ["axum_extras", "chrono", "uuid"] }
utoipa-swagger-ui = { version = "9", features = ["axum"] }
dotenvy = "0.15"
```

### Why these crates

- `axum` keeps the API clean.
- `sqlx` works well with Postgres and is production-grade.
- `reqwest` plus `scraper` handles the first version of scraping without a browser engine.
- `utoipa` makes your API self-documenting.

---

## Step 2: Add Environment Configuration

File: `atlas-scrape/.env`

```env
DATABASE_URL=postgres://postgres:postgres@localhost:5432/atlas_scrape
APP_HOST=127.0.0.1
APP_PORT=3000
JWT_SECRET=replace_me_with_a_long_random_secret
```

File: `atlas-scrape/src/config.rs`

```rust
use std::env;

#[derive(Clone, Debug)]
pub struct Config {
    pub database_url: String,
    pub app_host: String,
    pub app_port: u16,
    pub jwt_secret: String,
}

impl Config {
    pub fn from_env() -> Self {
        Self {
            database_url: env::var("DATABASE_URL").expect("DATABASE_URL is required"),
            app_host: env::var("APP_HOST").unwrap_or_else(|_| "127.0.0.1".to_string()),
            app_port: env::var("APP_PORT")
                .ok()
                .and_then(|value| value.parse().ok())
                .unwrap_or(3000),
            jwt_secret: env::var("JWT_SECRET").expect("JWT_SECRET is required"),
        }
    }
}
```

---

## Step 3: Create the Database Schema

File: `atlas-scrape/migrations/0001_init.sql`

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE scrape_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    target_url TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft',
    schedule_cron TEXT NULL,
    rate_limit_per_minute INT NULL,
    retry_limit INT NOT NULL DEFAULT 3,
    selectors JSONB NOT NULL,
    transform_rules JSONB NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE job_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID NOT NULL REFERENCES scrape_jobs(id) ON DELETE CASCADE,
    status TEXT NOT NULL DEFAULT 'queued',
    started_at TIMESTAMPTZ NULL,
    finished_at TIMESTAMPTZ NULL,
    error_message TEXT NULL,
    attempt_number INT NOT NULL DEFAULT 1,
    pages_fetched INT NOT NULL DEFAULT 0
);

CREATE TABLE scraped_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_run_id UUID NOT NULL REFERENCES job_runs(id) ON DELETE CASCADE,
    payload JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE job_logs (
    id BIGSERIAL PRIMARY KEY,
    job_run_id UUID NOT NULL REFERENCES job_runs(id) ON DELETE CASCADE,
    level TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

This schema is enough to support:

- users
- jobs
- runs
- records
- logs

That is already much stronger than a basic scraper repo.

---

## Step 4: Build Shared App State

File: `atlas-scrape/src/state.rs`

```rust
use reqwest::Client;
use sqlx::PgPool;

use crate::config::Config;

#[derive(Clone)]
pub struct AppState {
    pub config: Config,
    pub db: PgPool,
    pub http_client: Client,
}
```

---

## Step 5: Create the HTTP Server

File: `atlas-scrape/src/main.rs`

```rust
mod config;
mod state;

use axum::{routing::get, Router};
use reqwest::Client;
use sqlx::postgres::PgPoolOptions;
use tokio::net::TcpListener;
use tower_http::{cors::CorsLayer, trace::TraceLayer};
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

use crate::{config::Config, state::AppState};

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    dotenvy::dotenv().ok();

    tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::new("info"))
        .with(tracing_subscriber::fmt::layer())
        .init();

    let config = Config::from_env();

    let db = PgPoolOptions::new()
        .max_connections(10)
        .connect(&config.database_url)
        .await?;

    let http_client = Client::builder()
        .user_agent("atlas-scrape/0.1")
        .build()?;

    let state = AppState {
        config: config.clone(),
        db,
        http_client,
    };

    let app = Router::new()
        .route("/health", get(|| async { "ok" }))
        .layer(CorsLayer::permissive())
        .layer(TraceLayer::new_for_http())
        .with_state(state);

    let addr = format!("{}:{}", config.app_host, config.app_port);
    let listener = TcpListener::bind(&addr).await?;

    tracing::info!("listening on {}", addr);
    axum::serve(listener, app).await?;

    Ok(())
}
```

### Important note

The snippet uses `anyhow::Result`, so add:

```toml
anyhow = "1"
```

to `Cargo.toml`.

---

## Step 6: Implement Authentication First

Do this before scraping. A real portfolio backend needs ownership and access control.

### Auth flow

1. user signs up
2. password is hashed with Argon2
3. user logs in
4. API returns a JWT
5. protected routes read the current user from the token

### DTOs

File: `atlas-scrape/src/routes/auth.rs`

```rust
use axum::{extract::State, http::StatusCode, Json};
use serde::{Deserialize, Serialize};
use sqlx::PgPool;

use crate::state::AppState;

#[derive(Deserialize)]
pub struct SignupRequest {
    pub email: String,
    pub username: String,
    pub password: String,
}

#[derive(Serialize)]
pub struct AuthResponse {
    pub message: String,
}

pub async fn signup(
    State(state): State<AppState>,
    Json(payload): Json<SignupRequest>,
) -> Result<(StatusCode, Json<AuthResponse>), StatusCode> {
    let password_hash = hash_password(&payload.password).map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    sqlx::query!(
        r#"
        INSERT INTO users (email, username, password_hash)
        VALUES ($1, $2, $3)
        "#,
        payload.email,
        payload.username,
        password_hash
    )
    .execute(&state.db)
    .await
    .map_err(|_| StatusCode::BAD_REQUEST)?;

    Ok((
        StatusCode::CREATED,
        Json(AuthResponse {
            message: "user created".to_string(),
        }),
    ))
}

fn hash_password(password: &str) -> Result<String, argon2::password_hash::Error> {
    use argon2::{
        password_hash::{rand_core::OsRng, PasswordHasher, SaltString},
        Argon2,
    };

    let salt = SaltString::generate(&mut OsRng);
    Argon2::default()
        .hash_password(password.as_bytes(), &salt)
        .map(|hash| hash.to_string())
}
```

### Why start here

If you skip auth and add it later, you will have to retrofit ownership checks across every route. That is wasted effort.

---

## Step 7: Define Job Creation

This is the heart of the platform.

### Job payload

File: `atlas-scrape/src/models/job.rs`

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
pub struct SelectorRule {
    pub field: String,
    pub selector: String,
    pub attribute: Option<String>,
}

#[derive(Debug, Deserialize)]
pub struct CreateJobRequest {
    pub name: String,
    pub target_url: String,
    pub schedule_cron: Option<String>,
    pub rate_limit_per_minute: Option<i32>,
    pub retry_limit: i32,
    pub selectors: Vec<SelectorRule>,
}
```

### Create job route

File: `atlas-scrape/src/routes/jobs.rs`

```rust
use axum::{extract::State, http::StatusCode, Json};
use serde::Serialize;
use serde_json::json;
use uuid::Uuid;

use crate::{models::job::CreateJobRequest, state::AppState};

#[derive(Serialize)]
pub struct JobCreatedResponse {
    pub id: Uuid,
    pub message: String,
}

pub async fn create_job(
    State(state): State<AppState>,
    Json(payload): Json<CreateJobRequest>,
) -> Result<(StatusCode, Json<JobCreatedResponse>), StatusCode> {
    let job_id = Uuid::new_v4();

    sqlx::query!(
        r#"
        INSERT INTO scrape_jobs (
            id,
            user_id,
            name,
            target_url,
            schedule_cron,
            rate_limit_per_minute,
            retry_limit,
            selectors
        )
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        "#,
        job_id,
        Uuid::nil(),
        payload.name,
        payload.target_url,
        payload.schedule_cron,
        payload.rate_limit_per_minute,
        payload.retry_limit,
        json!(payload.selectors)
    )
    .execute(&state.db)
    .await
    .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    Ok((
        StatusCode::CREATED,
        Json(JobCreatedResponse {
            id: job_id,
            message: "job created".to_string(),
        }),
    ))
}
```

### Important improvement

The snippet uses `Uuid::nil()` as a placeholder. In the real implementation, replace that with the authenticated user ID from JWT middleware.

Do not leave ownership fake in the final portfolio version.

---

## Step 8: Build the Scraping Engine

This should live in a service module, not in the route handler.

File: `atlas-scrape/src/services/scraper_service.rs`

```rust
use reqwest::Client;
use scraper::{Html, Selector};
use serde_json::{Map, Value};

use crate::models::job::SelectorRule;

pub async fn scrape_page(
    client: &Client,
    target_url: &str,
    selectors: &[SelectorRule],
) -> anyhow::Result<Value> {
    let html = client.get(target_url).send().await?.text().await?;
    let document = Html::parse_document(&html);

    let mut result = Map::new();

    for rule in selectors {
        let selector = Selector::parse(&rule.selector)?;

        if let Some(element) = document.select(&selector).next() {
            let value = match &rule.attribute {
                Some(attribute) => element.value().attr(attribute).unwrap_or("").to_string(),
                None => element.text().collect::<Vec<_>>().join(" ").trim().to_string(),
            };

            result.insert(rule.field.clone(), Value::String(value));
        } else {
            result.insert(rule.field.clone(), Value::Null);
        }
    }

    Ok(Value::Object(result))
}
```

### Why this design is good

- routes stay thin
- scraping logic is isolated
- the service can later support pagination, multiple pages, proxies, or headless browser fallback

---

## Step 9: Add a Background Worker

Do not perform long scraping tasks inside the request-response cycle. Queue a run, then let a worker process it.

### Simple first version

When a user clicks "run job":

1. insert a row in `job_runs` with status `queued`
2. a worker loop polls queued jobs
3. worker marks run `running`
4. worker executes scraping
5. worker stores results
6. worker marks run `completed` or `failed`

### Worker skeleton

File: `atlas-scrape/src/services/worker_service.rs`

```rust
use std::time::Duration;

use serde_json::from_value;
use tokio::time::sleep;
use uuid::Uuid;

use crate::{
    models::job::SelectorRule,
    services::scraper_service::scrape_page,
    state::AppState,
};

pub async fn run_worker(state: AppState) {
    loop {
        if let Err(error) = process_one_queued_run(&state).await {
            tracing::error!("worker error: {}", error);
        }

        sleep(Duration::from_secs(3)).await;
    }
}

async fn process_one_queued_run(state: &AppState) -> anyhow::Result<()> {
    let queued = sqlx::query!(
        r#"
        SELECT jr.id, sj.target_url, sj.selectors
        FROM job_runs jr
        JOIN scrape_jobs sj ON sj.id = jr.job_id
        WHERE jr.status = 'queued'
        ORDER BY jr.started_at NULLS FIRST
        LIMIT 1
        "#
    )
    .fetch_optional(&state.db)
    .await?;

    let Some(run) = queued else {
        return Ok(());
    };

    sqlx::query!(
        "UPDATE job_runs SET status = 'running', started_at = NOW() WHERE id = $1",
        run.id
    )
    .execute(&state.db)
    .await?;

    let selectors: Vec<SelectorRule> = from_value(run.selectors)?;
    let payload = scrape_page(&state.http_client, &run.target_url, &selectors).await?;

    sqlx::query!(
        "INSERT INTO scraped_records (job_run_id, payload) VALUES ($1, $2)",
        run.id,
        payload
    )
    .execute(&state.db)
    .await?;

    sqlx::query!(
        "UPDATE job_runs SET status = 'completed', finished_at = NOW() WHERE id = $1",
        run.id
    )
    .execute(&state.db)
    .await?;

    Ok(())
}
```

### Better later

Later, replace polling with:

- `FOR UPDATE SKIP LOCKED`
- a proper queue table
- or a dedicated worker service

For a portfolio MVP, polling is acceptable if the architecture is clearly explained.

---

## Step 10: Add Export Endpoints

Exports make the product feel complete.

### JSON export

File: `atlas-scrape/src/routes/exports.rs`

```rust
use axum::{extract::{Path, State}, http::StatusCode, Json};
use serde_json::Value;
use uuid::Uuid;

use crate::state::AppState;

pub async fn export_json(
    Path(job_id): Path<Uuid>,
    State(state): State<AppState>,
) -> Result<Json<Vec<Value>>, StatusCode> {
    let rows = sqlx::query!(
        r#"
        SELECT sr.payload
        FROM scraped_records sr
        JOIN job_runs jr ON jr.id = sr.job_run_id
        WHERE jr.job_id = $1
        ORDER BY sr.created_at DESC
        "#,
        job_id
    )
    .fetch_all(&state.db)
    .await
    .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;

    let payloads = rows.into_iter().map(|row| row.payload).collect();
    Ok(Json(payloads))
}
```

### CSV export strategy

For CSV, flatten JSON fields into columns. In V1, assume one stable schema per job.

Example response flow:

1. fetch records for a job
2. infer columns from selector rules
3. write CSV rows with the `csv` crate
4. return `text/csv`

This is a strong portfolio detail because it shows you thought about shape consistency.

---

## Step 11: Add OpenAPI Docs

API documentation is explicitly required in the challenge. Do not skip it.

### Why it matters

- shows professionalism
- improves developer experience
- makes your backend easy to test with Swagger UI

### Recommended route set

- `POST /signup`
- `POST /login`
- `GET /profile`
- `PUT /profile`
- `POST /jobs`
- `GET /jobs`
- `GET /jobs/:id`
- `PUT /jobs/:id`
- `DELETE /jobs/:id`
- `POST /jobs/:id/run`
- `GET /jobs/:id/runs`
- `GET /jobs/:id/export/json`
- `GET /jobs/:id/export/csv`

---

## Step 12: Handle Errors Properly

Do not return vague `500` responses everywhere.

Create an application error type.

File: `atlas-scrape/src/error.rs`

```rust
use axum::{
    http::StatusCode,
    response::{IntoResponse, Response},
    Json,
};
use serde::Serialize;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum AppError {
    #[error("not found")]
    NotFound,
    #[error("unauthorized")]
    Unauthorized,
    #[error("validation error: {0}")]
    Validation(String),
    #[error("internal server error")]
    Internal,
}

#[derive(Serialize)]
struct ErrorBody {
    error: String,
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let status = match self {
            AppError::NotFound => StatusCode::NOT_FOUND,
            AppError::Unauthorized => StatusCode::UNAUTHORIZED,
            AppError::Validation(_) => StatusCode::BAD_REQUEST,
            AppError::Internal => StatusCode::INTERNAL_SERVER_ERROR,
        };

        let body = Json(ErrorBody {
            error: self.to_string(),
        });

        (status, body).into_response()
    }
}
```

This improves the API immediately.

---

## Step 13: Add Logging and Observability

For scraping systems, logs are not optional.

Track:

- job created
- job queued
- job started
- page fetched
- selector failed
- export requested
- retry triggered

Also store important job-level events in `job_logs`.

This lets you build a dashboard later without changing the worker logic.

---

## Step 14: Add Retries and Rate Limiting

These are core scraping concerns.

### Retry strategy

Retry when:

- request times out
- remote server returns `5xx`
- transient network error occurs

Do not retry forever. Use exponential backoff.

Example:

- attempt 1: immediately
- attempt 2: after 5 seconds
- attempt 3: after 15 seconds

### Rate limiting strategy

Store per-job or per-domain limits:

- `rate_limit_per_minute`

Then apply a sleep or token-bucket strategy in the worker.

This protects both your app and the target site.

---

## Step 15: Respect Scraping Ethics

A serious scraping portfolio project should mention this clearly.

### Add these rules to your README

- respect `robots.txt` where applicable
- obey site Terms of Service
- identify your client with a user agent
- avoid aggressive request bursts
- never scrape personal data irresponsibly

Even if not fully automated in MVP, stating this shows maturity.

---

## Step 16: Testing Strategy

Do not leave the project untested.

### Unit tests

Test:

- password hashing
- selector parsing
- HTML extraction logic
- export formatting

### Integration tests

Test:

- signup and login
- create job
- queue run
- export results

### Good Rust testing direction

- `cargo test`
- `#[tokio::test]` for async logic
- sample HTML fixtures for scraper tests

---

## Step 17: Backend-First Roadmap to Full Stack

Once the backend is stable, add the frontend.

### Best frontend growth path

Use a separate frontend app:

```text
atlas-scrape/
├── backend/
└── frontend/
```

### Frontend pages

- login page
- register page
- dashboard
- create job form
- edit job form
- job history view
- logs view
- export controls

### Why this is growable

The frontend becomes a client of a stable API instead of mixing business logic into UI code.

That is the right full stack architecture for a project you may evolve later.

---

## Recommended Portfolio Story

When you present this project, describe it like this:

> I built a backend-first web scraping platform in Rust using Axum, SQLx, Reqwest, and PostgreSQL. Users can authenticate, configure scraping jobs with CSS selectors, execute jobs asynchronously, inspect run history, and export extracted data as JSON or CSV. The architecture separates API routes, background workers, and scraping services so the system can grow into a full stack product with dashboards, scheduling, and third-party integrations.

That framing is stronger than saying:

> I built a scraper in Rust.

---

## Suggested API Contract

### `POST /signup`

Request:

```json
{
  "email": "demo@example.com",
  "username": "demo",
  "password": "StrongPassword123"
}
```

### `POST /jobs`

Request:

```json
{
  "name": "Books to Scrape homepage",
  "target_url": "https://books.toscrape.com/",
  "schedule_cron": null,
  "rate_limit_per_minute": 20,
  "retry_limit": 3,
  "selectors": [
    {
      "field": "title",
      "selector": "article.product_pod h3 a",
      "attribute": "title"
    },
    {
      "field": "price",
      "selector": "article.product_pod .price_color",
      "attribute": null
    }
  ]
}
```

### `POST /jobs/:id/run`

Behavior:

- create a `job_runs` record with status `queued`
- return `202 Accepted`

This is better than blocking the client while scraping runs.

---

## What to Build First, in Order

If you want the correct build order, use this:

1. project bootstrapping
2. database schema
3. auth
4. job CRUD
5. manual run endpoint
6. worker loop
7. scraping service
8. result storage
9. JSON export
10. CSV export
11. logs
12. OpenAPI docs
13. scheduling
14. frontend

This order minimizes rewrites.

---

## What to Avoid

- Do not start with a frontend.
- Do not start with browser automation unless you need it.
- Do not mix scraping logic directly into route handlers.
- Do not store raw HTML forever unless you have a reason.
- Do not skip authentication ownership checks.
- Do not ignore retries and logging.

---

## Final Recommendation

For a portfolio-quality implementation, aim for:

- one Rust backend repo
- clean modules
- PostgreSQL schema with history tables
- background worker loop
- generic selector-driven scraping
- JSON and CSV exports
- Swagger/OpenAPI docs
- a clear README explaining architecture and ethics

That combination is practical, interview-friendly, and strong enough to evolve into a real full stack application later.

---

## Documentation Links

- Rust Book: https://doc.rust-lang.org/book/
- Cargo Book: https://doc.rust-lang.org/cargo/
- Axum docs: https://docs.rs/axum/latest/axum/
- Tokio docs: https://docs.rs/tokio/latest/tokio/
- SQLx docs: https://docs.rs/sqlx/latest/sqlx/
- Reqwest docs: https://docs.rs/reqwest/latest/reqwest/
- scraper crate docs: https://docs.rs/scraper/latest/scraper/
- Serde docs: https://docs.rs/serde/latest/serde/
- Utoipa docs: https://docs.rs/utoipa/latest/utoipa/
- PostgreSQL docs: https://www.postgresql.org/docs/current/index.html

---

## Next Best Upgrade After MVP

If you want this project to stand out even more, the best next upgrade is:

- add a scheduler
- add a polished frontend dashboard
- add site-specific extraction templates
- add webhook notifications
- add a headless browser fallback for JavaScript-rendered pages

But build the stable Rust backend first.
