# CityScope

CityScope is an AI-powered event discovery platform designed to help users discover relevant events based on location, category, budget, preferences, and natural-language queries.

The project is being developed as a full-stack portfolio application with a React Native mobile client and a Python/FastAPI backend.

## Current Architecture

### Backend

- Python
- FastAPI
- Pydantic
- Layered architecture
  - Router
  - Service
  - Repository
  - Data source
- JSON-based event data for the initial development phase
- REST API
- Query parameter filtering
- Request validation
- CORS configuration
- Error handling

Current request flow:

```text
Client
  ↓
FastAPI Router
  ↓
Service
  ↓
Repository
  ↓
Event Data
```

### Available API Features

- Health check
- List all events
- Get event by ID
- Filter events by:
  - District
  - Category
  - Maximum price
- Input validation
- 404 handling for missing events

Example endpoints:

```text
GET /health

GET /api/v1/events

GET /api/v1/events/{event_id}

GET /api/v1/events?district=Kadikoy

GET /api/v1/events?category=music&max_price=700
```

## Mobile Application

The primary mobile application will be built with:

- React Native
- TypeScript
- Expo
- Clean Architecture principles
- REST API integration
- Turkish and English localization

Planned initial screens include:

- Explore
- Event Detail
- Search and Filters
- Favorites
- AI Event Concierge

The mobile application will consume event data exclusively through the backend API rather than importing local event JSON directly.

## AI Event Concierge

A major feature planned for CityScope is an AI-powered event recommendation assistant.

Example query:

```text
Cumartesi akşamı İstanbul'da 1000 TL altında sakin bir etkinlik öner.
```

The planned AI pipeline is:

```text
User Query
   ↓
LLM Intent Extraction
   ↓
Structured Filters
   ↓
Event Retrieval
   ↓
Ranking
   ↓
Grounded AI Recommendation
```

The LLM will not invent events. Recommendations will be grounded in events retrieved from the CityScope backend.

## Planned Backend Evolution

The initial JSON data source is intentionally temporary.

Planned backend improvements include:

- PostgreSQL
- Database migrations
- Persistent user data
- Favorites
- Venue data
- Event categories
- Authentication
- Pagination
- Improved filtering
- Search
- Production deployment
- Automated tests
- Structured logging
- API observability

## Planned AI / RAG Architecture

After the core mobile and REST functionality is stable, the AI layer is planned to evolve toward a retrieval-augmented architecture.

Planned technologies and concepts include:

- OpenAI API
- Structured LLM outputs
- Embeddings
- PostgreSQL + pgvector
- Semantic search
- Hybrid retrieval
- RAG
- Candidate reranking
- Retrieval evaluation
- AI observability

Structured properties such as price, district, category, and date will use conventional database filtering.

Semantic concepts such as:

- quiet
- romantic
- conversational
- energetic
- artistic

can later be handled through embedding-based semantic retrieval.

## Localization

CityScope is planned to support:

- Turkish
- English

User-facing strings will be organized in dedicated localization resources rather than being hardcoded throughout the application.

## Platform Roadmap

The first client will be the cross-platform React Native application.

Future platform-specific implementations are also planned:

- Native iOS application

  - Swift
  - SwiftUI

- Native Android application

  - Kotlin
  - Jetpack Compose

These native applications can consume the same CityScope backend and API contracts while allowing platform-specific architecture, UI, performance, and development practices to be explored independently.

## Development Roadmap

### Phase 1 — Backend Foundation

- [x] FastAPI project setup
- [x] Layered backend architecture
- [x] Event model
- [x] Event repository
- [x] Event service
- [x] Event router
- [x] List events
- [x] Get event by ID
- [x] Event filtering
- [x] Query validation
- [x] 404 handling
- [x] CORS configuration

### Phase 2 — React Native Application

- [ ] Mobile project architecture
- [ ] API client
- [ ] Event domain model
- [ ] Repository abstraction
- [ ] Remote data source
- [ ] Use cases
- [ ] Explore screen
- [ ] Event detail screen
- [ ] Search and filters
- [ ] Loading, empty, and error states
- [ ] Favorites
- [ ] Turkish / English localization

### Phase 3 — Production Backend

- [ ] Public backend deployment
- [ ] PostgreSQL
- [ ] Database repositories
- [ ] Pagination
- [ ] Testing
- [ ] Environment configuration
- [ ] Production logging

### Phase 4 — AI Features

- [ ] OpenAI API integration
- [ ] Natural-language event queries
- [ ] Structured intent extraction
- [ ] Grounded recommendation generation
- [ ] AI Event Concierge UI

### Phase 5 — Semantic Search and RAG

- [ ] Event embeddings
- [ ] pgvector
- [ ] Semantic search
- [ ] Hybrid retrieval
- [ ] Venue and editorial knowledge base
- [ ] RAG
- [ ] Retrieval evaluation
- [ ] AI observability

### Phase 6 — Native Applications

- [ ] Native iOS application with Swift / SwiftUI
- [ ] Native Android application with Kotlin / Jetpack Compose

## Project Status

CityScope is currently under active development.

The current focus is completing the initial REST backend and integrating it with the React Native mobile application.
