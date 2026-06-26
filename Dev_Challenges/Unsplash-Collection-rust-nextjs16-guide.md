# Unsplash Collections

## Portfolio Guide: Rust Backend + Next.js 16 Frontend

This guide turns the challenge brief into a portfolio-quality full-stack project with:

- a **Rust backend** for the API and collection storage
- a **Next.js 16 frontend** for the product UI
- a structure that is realistic to build in stages
- features that look polished without becoming unreasonably large

As of **June 25, 2026**, the official Next.js docs list **16.2.9** as the latest App Router docs version, so this guide targets **Next.js 16 with the App Router**.

Core references:

- Next.js docs: https://nextjs.org/docs
- Next.js installation: https://nextjs.org/docs/app/getting-started/installation
- Next.js layouts and pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- Next.js Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
- Unsplash API docs: https://unsplash.com/documentation
- Rust Book: https://doc.rust-lang.org/book/
- Axum docs: https://docs.rs/axum/latest/axum/
- SQLx docs: https://docs.rs/sqlx/latest/sqlx/
- Reqwest docs: https://docs.rs/reqwest/latest/reqwest/
- PostgreSQL docs: https://www.postgresql.org/docs/current/index.html

---

## 1. Read the Challenge Correctly

The challenge is not just:

- search Unsplash
- click an image
- save it to a collection

It is really a small product with three major flows:

1. **Discovery**: search and browse Unsplash images
2. **Curation**: create and manage collections
3. **Asset management**: store image references locally and make them easy to revisit

That means your portfolio project should feel like a real application, not a thin API wrapper.

---

## 2. Best Product Framing

Use a product name that sounds intentional. Good options:

- `Frameboard`
- `Museum`
- `Shelf for Unsplash`
- `Atlas Collections`

This guide will use:

```text
frameboard
```

### Portfolio positioning

Describe it like this:

> Frameboard is a full-stack curation platform for Unsplash images. Users can search images, inspect image metadata, organize images into custom collections, remove images from collections, and browse curated sets from a dedicated collections view. The frontend is built with Next.js 16 App Router, while the backend is a Rust API that handles collection persistence, collection search, and collection membership management.

That sounds stronger than:

> I made an Unsplash clone.

---

## 3. Recommended Architecture

## Backend-first, frontend-rich

The best implementation order is:

1. Rust API
2. database schema
3. Unsplash integration service
4. collection CRUD
5. image-to-collection operations
6. Next.js frontend
7. caching, polish, deployment

This gives you a stable backend contract before you design UI around it.

### Stack

#### Frontend

- **Next.js 16 App Router**
- **TypeScript**
- **Tailwind CSS**
- **Zustand** for lightweight client state
- **TanStack Query** for server state and mutation flow

#### Backend

- **Rust**
- **Axum**
- **Tokio**
- **SQLx**
- **Reqwest**
- **Serde**
- **PostgreSQL**

#### Why this stack works

- Next.js 16 gives you excellent routing and server/client composition.
- Rust handles API reliability and type-safe data flow well.
- PostgreSQL fits collection relationships better than a document database here.
- TanStack Query makes add/remove collection actions much cleaner than manual fetch state.

---

## 4. What to Build

These are the required features translated into product behavior.

### Pages

- homepage
- image details page
- collections index page
- collection details page

### Core actions

- search Unsplash images by keyword
- open a specific image details page
- show author and published date
- show collections that contain this image
- add image to a collection
- search collections when adding
- hide collections the image already belongs to
- remove image from collections
- download the image
- browse collections and view their images

---

## 5. Strong but Implementable Portfolio Features

These are worth adding because they improve the project visibly without turning it into a research project.

### Recommended extras

- empty states with helpful copy
- optimistic UI for add/remove collection actions
- collection cover image chosen automatically from the first item
- debounced search input on homepage
- keyboard Enter submit on search
- image detail side panel or modal on desktop, full page on mobile
- copy share link button for image and collection pages
- collection search modal with instant filtering
- loading skeletons
- toast notifications for add/remove operations
- pagination or infinite scroll for search results
- responsive masonry-style search grid

### Very good backend extras

- store a local snapshot of image metadata when added to a collection
- prevent duplicate image membership with a database constraint
- expose collection search endpoint
- add request-level caching for repeated image detail requests
- add structured logs

### Do not add in MVP

- authentication
- collaborative collections
- comments
- drag-and-drop reordering

Those are valid later, but they are not necessary for this challenge.

---

## 6. System Design

## Key idea

Do **not** store full Unsplash image binaries in your database.

Store:

- the Unsplash image ID
- metadata snapshot
- links you need for display/download
- collection membership

That keeps your app fast, compliant, and easier to maintain.

### Data ownership split

#### Unsplash remains source of truth for

- live search results
- current image details
- download links

#### Your app remains source of truth for

- collection names
- collection descriptions
- collection membership
- locally stored metadata snapshot for display stability

---

## 7. Recommended Database Schema

Use PostgreSQL.

### Tables

#### `collections`

- `id UUID PRIMARY KEY`
- `name TEXT NOT NULL UNIQUE`
- `slug TEXT NOT NULL UNIQUE`
- `description TEXT NULL`
- `cover_unsplash_id TEXT NULL`
- `created_at TIMESTAMPTZ NOT NULL`
- `updated_at TIMESTAMPTZ NOT NULL`

#### `images`

- `id UUID PRIMARY KEY`
- `unsplash_id TEXT NOT NULL UNIQUE`
- `slug TEXT NOT NULL UNIQUE`
- `description TEXT NULL`
- `alt_description TEXT NULL`
- `author_name TEXT NOT NULL`
- `author_username TEXT NOT NULL`
- `published_at TIMESTAMPTZ NULL`
- `width INT NOT NULL`
- `height INT NOT NULL`
- `thumb_url TEXT NOT NULL`
- `small_url TEXT NOT NULL`
- `regular_url TEXT NOT NULL`
- `full_url TEXT NOT NULL`
- `download_url TEXT NOT NULL`
- `html_url TEXT NOT NULL`
- `created_at TIMESTAMPTZ NOT NULL`
- `updated_at TIMESTAMPTZ NOT NULL`

#### `collection_images`

- `collection_id UUID NOT NULL`
- `image_id UUID NOT NULL`
- `added_at TIMESTAMPTZ NOT NULL`
- unique constraint on `(collection_id, image_id)`

### Why store an `images` table

Because when a user adds an image to a collection, you want:

- fast collection rendering
- stable historical data
- no need to refetch everything from Unsplash every time

This is much cleaner than storing only Unsplash IDs.

---

## 8. API Design

Use the challenge endpoints, but improve them slightly for frontend ergonomics.

### Public API routes

#### Unsplash proxy routes

- `GET /api/search/images?q=mountains&page=1`
- `GET /api/images/:unsplashId`

These call Unsplash through the Rust backend instead of exposing your secret directly to the browser.

#### Collections routes

- `GET /api/collections`
- `POST /api/collections`
- `GET /api/collections/:collectionId`
- `PATCH /api/collections/:collectionId`
- `DELETE /api/collections/:collectionId`
- `GET /api/collections/search?q=travel`

#### Collection membership routes

- `GET /api/collections/:collectionId/images`
- `POST /api/collections/:collectionId/images`
- `DELETE /api/collections/:collectionId/images/:imageId`

#### Image membership support

- `GET /api/images/:unsplashId/collections`

This route is not in the original brief, but it is extremely useful for the image page because it directly answers:

- which collections already contain this image

That removes frontend guesswork.

---

## 9. Recommended Monorepo Structure

Use a simple full-stack workspace:

```text
frameboard/
├── apps/
│   ├── web/
│   └── api/
├── docs/
│   ├── architecture.md
│   ├── api-contract.md
│   └── ui-notes.md
├── .env.example
├── README.md
└── docker-compose.yml
```

### Frontend structure

```text
apps/web/
├── app/
│   ├── page.tsx
│   ├── image/
│   │   └── [unsplashId]/
│   │       └── page.tsx
│   ├── collections/
│   │   ├── page.tsx
│   │   └── [slug]/
│   │       └── page.tsx
│   ├── layout.tsx
│   ├── loading.tsx
│   └── globals.css
├── components/
│   ├── search/
│   ├── gallery/
│   ├── collections/
│   ├── image/
│   └── ui/
├── lib/
│   ├── api.ts
│   ├── env.ts
│   ├── query-client.ts
│   └── format.ts
├── stores/
│   └── ui-store.ts
└── types/
```

### Backend structure

```text
apps/api/
├── Cargo.toml
├── migrations/
├── src/
│   ├── main.rs
│   ├── config.rs
│   ├── state.rs
│   ├── error.rs
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   └── dto/
└── .env
```

This structure is straightforward and portfolio-friendly.

---

## 10. Step-by-Step Build Plan

## Step 1: Set up the repository

Create the folders:

```powershell
mkdir frameboard
cd frameboard
mkdir apps
mkdir docs
```

Create:

- `apps/api`
- `apps/web`

Add a `README.md` early and keep it updated.

---

## Step 2: Build the Rust backend first

Create the API:

```powershell
cd apps
cargo new api
```

### `apps/api/Cargo.toml`

```toml
[package]
name = "frameboard-api"
version = "0.1.0"
edition = "2024"

[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
sqlx = { version = "0.8", features = ["runtime-tokio-rustls", "postgres", "uuid", "chrono", "json"] }
reqwest = { version = "0.12", default-features = false, features = ["rustls-tls", "json", "gzip", "brotli"] }
uuid = { version = "1", features = ["v4", "serde"] }
chrono = { version = "0.4", features = ["serde"] }
thiserror = "2"
anyhow = "1"
dotenvy = "0.15"
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
tower-http = { version = "0.6", features = ["cors", "trace", "compression-full"] }
```

### Why this stack

- `axum` for clean route composition
- `sqlx` for Postgres
- `reqwest` for Unsplash API calls
- `tower-http` for cross-cutting middleware

---

## Step 3: Add environment configuration

File: `apps/api/.env`

```env
DATABASE_URL=postgres://postgres:postgres@localhost:5432/frameboard
APP_HOST=127.0.0.1
APP_PORT=8080
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
UNSPLASH_API_BASE=https://api.unsplash.com
FRONTEND_ORIGIN=http://localhost:3000
```

File: `apps/api/src/config.rs`

```rust
use std::env;

#[derive(Clone, Debug)]
pub struct Config {
    pub database_url: String,
    pub app_host: String,
    pub app_port: u16,
    pub unsplash_access_key: String,
    pub unsplash_api_base: String,
    pub frontend_origin: String,
}

impl Config {
    pub fn from_env() -> Self {
        Self {
            database_url: env::var("DATABASE_URL").expect("DATABASE_URL is required"),
            app_host: env::var("APP_HOST").unwrap_or_else(|_| "127.0.0.1".to_string()),
            app_port: env::var("APP_PORT")
                .ok()
                .and_then(|v| v.parse().ok())
                .unwrap_or(8080),
            unsplash_access_key: env::var("UNSPLASH_ACCESS_KEY").expect("UNSPLASH_ACCESS_KEY is required"),
            unsplash_api_base: env::var("UNSPLASH_API_BASE")
                .unwrap_or_else(|_| "https://api.unsplash.com".to_string()),
            frontend_origin: env::var("FRONTEND_ORIGIN")
                .unwrap_or_else(|_| "http://localhost:3000".to_string()),
        }
    }
}
```

---

## Step 4: Create the database schema

File: `apps/api/migrations/0001_init.sql`

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE collections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    description TEXT NULL,
    cover_unsplash_id TEXT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE images (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    unsplash_id TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    description TEXT NULL,
    alt_description TEXT NULL,
    author_name TEXT NOT NULL,
    author_username TEXT NOT NULL,
    published_at TIMESTAMPTZ NULL,
    width INT NOT NULL,
    height INT NOT NULL,
    thumb_url TEXT NOT NULL,
    small_url TEXT NOT NULL,
    regular_url TEXT NOT NULL,
    full_url TEXT NOT NULL,
    download_url TEXT NOT NULL,
    html_url TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE collection_images (
    collection_id UUID NOT NULL REFERENCES collections(id) ON DELETE CASCADE,
    image_id UUID NOT NULL REFERENCES images(id) ON DELETE CASCADE,
    added_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (collection_id, image_id)
);
```

### Important note

Use the join-table primary key to prevent duplicates automatically.

---

## Step 5: Build the Unsplash service

Your frontend should not call Unsplash directly with a secret key.

Create a service that:

- searches photos
- fetches a single photo
- normalizes the response shape for your app

File: `apps/api/src/services/unsplash_service.rs`

```rust
use anyhow::Result;
use reqwest::Client;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct UnsplashSearchResponse {
    pub results: Vec<UnsplashPhoto>,
}

#[derive(Debug, Deserialize)]
pub struct UnsplashPhoto {
    pub id: String,
    pub description: Option<String>,
    pub alt_description: Option<String>,
    pub created_at: Option<String>,
    pub width: i32,
    pub height: i32,
    pub urls: UnsplashUrls,
    pub links: UnsplashLinks,
    pub user: UnsplashUser,
}

#[derive(Debug, Deserialize)]
pub struct UnsplashUrls {
    pub thumb: String,
    pub small: String,
    pub regular: String,
    pub full: String,
}

#[derive(Debug, Deserialize)]
pub struct UnsplashLinks {
    pub html: String,
    pub download: String,
}

#[derive(Debug, Deserialize)]
pub struct UnsplashUser {
    pub username: String,
    pub name: String,
}

pub async fn search_images(
    client: &Client,
    base_url: &str,
    access_key: &str,
    query: &str,
    page: u32,
) -> Result<UnsplashSearchResponse> {
    let response = client
        .get(format!("{base_url}/search/photos"))
        .query(&[("query", query), ("page", &page.to_string())])
        .header("Authorization", format!("Client-ID {}", access_key))
        .send()
        .await?
        .error_for_status()?
        .json::<UnsplashSearchResponse>()
        .await?;

    Ok(response)
}
```

### Why a service layer matters

It keeps Unsplash-specific logic out of route handlers and makes later testing easier.

---

## Step 6: Implement collections CRUD

Build these first:

- create collection
- list collections
- get collection details
- search collections by name

### Suggested payload

#### `POST /api/collections`

```json
{
  "name": "Editorial Interiors",
  "description": "Warm minimalist interior references"
}
```

### Backend behavior

- create a slug from the name
- reject duplicate names
- return created collection metadata

### Why add search

Because the image page needs collection search when the user clicks `Add to Collection`.

Without a dedicated search endpoint, your UI ends up downloading too much and filtering client-side.

---

## Step 7: Implement image persistence on add-to-collection

When a user adds an Unsplash image to a collection:

1. frontend sends the selected collection ID and image payload
2. backend checks whether the image already exists locally
3. backend inserts it into `images` if missing
4. backend inserts `(collection_id, image_id)` into `collection_images`
5. backend returns updated membership info

### Why send a metadata snapshot

Because the image already came from search or image details.

That means you can persist:

- ID
- author
- dates
- dimensions
- image URLs

without needing a second external fetch every time.

### Suggested request body

```json
{
  "unsplashId": "abc123",
  "description": "Architectural light",
  "altDescription": "Sunlight inside a concrete building",
  "authorName": "Jane Doe",
  "authorUsername": "janedoe",
  "publishedAt": "2024-01-11T10:45:22Z",
  "width": 3000,
  "height": 2000,
  "thumbUrl": "https://images.unsplash.com/...",
  "smallUrl": "https://images.unsplash.com/...",
  "regularUrl": "https://images.unsplash.com/...",
  "fullUrl": "https://images.unsplash.com/...",
  "downloadUrl": "https://images.unsplash.com/...",
  "htmlUrl": "https://unsplash.com/photos/abc123"
}
```

---

## Step 8: Implement remove-from-collection

This is simpler than add, but still important.

### Backend behavior

- delete the row from `collection_images`
- if the image no longer belongs to any collection, optionally keep it in `images`

### Recommended choice

Keep the image row.

Why:

- simpler
- avoids race conditions
- preserves metadata stability

You can add garbage collection later if needed.

---

## Step 9: Create the Next.js 16 app

Create the frontend:

```powershell
npx create-next-app@latest apps/web --ts --tailwind --eslint --app
```

This guide assumes:

- TypeScript
- App Router
- Tailwind

### Frontend environment

File: `apps/web/.env.local`

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8080
```

---

## Step 10: Plan the frontend routes

Use App Router pages that match the product clearly.

### Route map

```text
/
/image/[unsplashId]
/collections
/collections/[slug]
```

### Why this works

- `/` handles discovery
- `/image/[unsplashId]` handles deep-linkable image details
- `/collections` handles browsing
- `/collections/[slug]` handles curated collection views

This is clean and good for demos.

---

## Step 11: Homepage implementation

The homepage should feel premium, not generic.

### Homepage sections

- large editorial hero with search input
- keyword hint chips
- results heading
- masonry or balanced responsive image grid

### User flow

1. user types a keyword
2. presses Enter
3. if the query is non-empty, results render
4. each result card links to `/image/[unsplashId]`

### Search UX details worth implementing

- block empty queries
- persist the latest query in the URL, for example `/?q=interior`
- show a useful empty state before the first search
- show a "no results" state when nothing is returned

### Recommended component split

- `SearchHero`
- `SearchInput`
- `ImageGrid`
- `ImageCard`
- `SearchEmptyState`

---

## Step 12: Image page implementation

This is the most important page in the project.

### What the page should show

- large image preview
- image description or fallback title
- author name
- published date
- dimensions
- list of collections containing the image
- add to collection button
- download button

### Data needed

From backend:

- Unsplash image details
- collections already containing this image

### Good UI layout

Desktop:

- left: large image
- right: metadata and collection actions

Mobile:

- image first
- metadata blocks stacked
- action bar below

### `Add to Collection` interaction

Use a modal or slide-over panel with:

- collection search input
- filtered collection results
- only collections that do not already include the image
- inline create collection action

This feels much better than dumping a long list into the page.

---

## Step 13: Collections page implementation

This page should feel like a curation library.

### Collections index

Show:

- collection card grid
- cover image
- collection title
- item count
- short description

### Collection details page

Show:

- collection title
- description
- item count
- responsive image grid

### Good extra

Sort collections by:

- most recently updated

That makes the UI feel alive as you demo it.

---

## Step 14: Use Server Components and Client Components correctly

This is important in Next.js 16.

### Use Server Components for

- initial page shells
- route-level data fetching where no client interactivity is needed
- collection page first render

### Use Client Components for

- search input
- Enter-to-search behavior
- modal open/close state
- add/remove collection mutations
- toasts

### Practical rule

Keep pages mostly server-rendered, then isolate interactivity into small client islands.

That is the right App Router architecture.

---

## Step 15: Add TanStack Query and Zustand

### Use TanStack Query for

- search requests
- image details fetches
- collections fetches
- add/remove mutations
- cache invalidation

### Use Zustand for

- UI-only state
- modal visibility
- selected collection search text
- temporary panel state

### Why not use Zustand for everything

Because server state and UI state are different concerns.

That separation improves code quality.

---

## Step 16: Suggested frontend API client

File: `apps/web/lib/api.ts`

```ts
const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL!;

export async function apiGet<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "GET",
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`GET ${path} failed`);
  }

  return response.json() as Promise<T>;
}

export async function apiPost<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(`POST ${path} failed`);
  }

  return response.json() as Promise<T>;
}

export async function apiDelete(path: string): Promise<void> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`DELETE ${path} failed`);
  }
}
```

Simple is fine here.

---

## Step 17: UI style direction that looks portfolio-worthy

Avoid a plain "image search app" look.

### Good design direction

- editorial typography
- large whitespace
- warm neutral palette
- soft borders instead of loud shadows
- image-first composition
- clean metadata blocks

### Visual system suggestion

- background: warm off-white
- text: near-black
- accent: muted forest or muted rust
- cards: thin border and subtle elevation only on hover

### Typography suggestion

- display font for headings: something expressive but readable
- clean sans serif for interface text

The UI should feel more like a gallery manager than a tutorial app.

---

## Step 18: Download behavior

The challenge requires image download.

### Frontend behavior

Provide a `Download image` button on the image page.

### Recommended implementation

- link to the stored `downloadUrl`
- open in a new tab or trigger a download flow

### Important note

Review Unsplash API guidelines and attribution expectations in their docs while implementing this, especially around download tracking and usage requirements.

Source:

- https://unsplash.com/documentation

---

## Step 19: Error handling and edge cases

Add these deliberately.

### Frontend states

- empty search
- loading results
- no results
- failed search
- failed add to collection
- failed remove from collection
- collection not found
- image not found

### Backend checks

- invalid collection ID
- duplicate collection name
- duplicate image membership
- invalid Unsplash payload
- missing query string

These make the app feel finished.

---

## Step 20: Testing plan

### Backend tests

Test:

- collection creation
- duplicate collection rejection
- image add to collection
- duplicate membership prevention
- image removal
- collection search filtering

### Frontend tests

Test:

- homepage Enter search
- image details render
- add to collection modal filtering
- remove from collection action
- collections page renders collection images

### Recommended tools

- backend: `cargo test`
- frontend unit/component tests: `vitest` or `jest`
- end-to-end tests: `playwright`

---

## Step 21: Deployment plan

### Recommended deployment

#### Frontend

- deploy `apps/web` to Vercel

#### Backend

- deploy Rust API to Railway, Fly.io, or Render

#### Database

- PostgreSQL on Neon, Supabase, Railway, or Render

### Why this is good

- fast to set up
- easy demo links
- clean separation between frontend and API

---

## Step 22: README sections that make the project stand out

Your `README.md` should include:

- product overview
- screenshots or GIFs
- architecture diagram
- stack choices and why
- local setup
- environment variables
- API summary
- deployment links
- known tradeoffs
- future improvements

### Good tradeoffs section example

- no authentication because the challenge does not require it
- backend proxies Unsplash to protect the API key
- image metadata is snapshotted locally when saved to collections for faster collection rendering

That shows engineering judgment.

---

## 23. Suggested implementation order

If you want the cleanest build order, do it like this:

1. create repo structure
2. create Rust API
3. create PostgreSQL schema
4. implement `GET /api/collections`
5. implement `POST /api/collections`
6. implement `GET /api/collections/search`
7. implement Unsplash search proxy
8. implement single image detail proxy
9. implement add image to collection
10. implement image membership lookup
11. implement remove image from collection
12. scaffold Next.js 16 app
13. build homepage search
14. build image page
15. build add-to-collection modal
16. build collections index page
17. build collection details page
18. add loading, errors, toasts
19. deploy backend
20. deploy frontend
21. record demo and polish README

This order avoids rework.

---

## 24. Suggested endpoint shapes

### `GET /api/search/images?q=interior&page=1`

Response:

```json
{
  "query": "interior",
  "page": 1,
  "results": [
    {
      "unsplashId": "abc123",
      "description": "Minimal room",
      "altDescription": "Sunlit living room",
      "authorName": "Jane Doe",
      "authorUsername": "janedoe",
      "publishedAt": "2024-01-11T10:45:22Z",
      "width": 3000,
      "height": 2000,
      "thumbUrl": "https://images.unsplash.com/...",
      "smallUrl": "https://images.unsplash.com/...",
      "regularUrl": "https://images.unsplash.com/...",
      "fullUrl": "https://images.unsplash.com/...",
      "downloadUrl": "https://images.unsplash.com/...",
      "htmlUrl": "https://unsplash.com/photos/abc123"
    }
  ]
}
```

### `GET /api/images/:unsplashId/collections`

Response:

```json
{
  "unsplashId": "abc123",
  "collections": [
    {
      "id": "3a4d8b7d-8b1b-4f7d-8c4b-95e64b89a2c2",
      "name": "Editorial Interiors",
      "slug": "editorial-interiors"
    }
  ]
}
```

### `POST /api/collections/:collectionId/images`

Response:

```json
{
  "message": "image added to collection",
  "collectionId": "3a4d8b7d-8b1b-4f7d-8c4b-95e64b89a2c2",
  "unsplashId": "abc123"
}
```

These response shapes are straightforward for a Next.js frontend.

---

## 25. Best full-stack story for interviews

When you present the project, emphasize these decisions:

- you protected the Unsplash key by proxying through the Rust API
- you normalized external image data into a local relational schema
- you designed collection membership as a join table with uniqueness protection
- you used Next.js 16 App Router with server/client separation instead of making everything a client app
- you kept the project backend-first so the UI was built on stable contracts

That is exactly the kind of explanation that makes the project feel intentional.

---

## 26. Final recommendation

If you want this challenge to look strong in a portfolio, aim for:

- polished homepage search
- excellent image details page
- clean collection management flow
- Rust API with proper relational modeling
- Next.js 16 App Router frontend with disciplined state handling
- responsive design that feels editorial rather than generic

That gives you a project that is clearly implementable, clearly full-stack, and clearly better than a basic challenge submission.

---

## 27. Nice follow-up upgrades after submission

If you want to extend it later:

- add collection cover customization
- add reordering inside collections
- add local notes per saved image
- add theme variants
- add shareable public collection pages with OG metadata
- add server-side caching for popular searches

These are all strong phase-two upgrades.
