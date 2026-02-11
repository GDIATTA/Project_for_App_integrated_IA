# Project_for_App_integrated_IA :

![Capture d’écran 2024-06-18 025048](https://github.com/GDIATTA/Project_for_-App_integrated_IA/assets/147615966/1b46be79-3a05-45ae-98c2-236363e3ad09)

## Project Goals and Deliverables :
Updated Project Goals
1) Backend foundations (your current scope, improved) <br>

Build and maintain a backend to store product data (name, price, category, tags, description, image) in MongoDB.<br>

Ensure reliable image upload, storage, and retrieval with validation and safe file handling. <br>

Standardize API responses and errors, and introduce input validation for form/API payloads. <br>

2) AI-ready data and feature storage <br>

Enrich each product at ingestion time with AI features: <br>

Text embedding from (name + description + tags + category) <br>

Optional: extracted keywords, normalized category, metadata <br>

Store AI features in MongoDB (embedding, ai_tags, ai_category_confidence, etc.). <br>

3) AI capabilities integrated into the backend <br>

Implement AI endpoints/services to support: <br>

Semantic search (“smart search” beyond keywords) <br>

Similar products recommendations (kNN / cosine similarity over embeddings) <br>

Auto-tagging / category suggestion from description (optional) <br>

Integrate AI into the existing posting flow (/posting/) so that AI enrichment happens automatically after insert. <br>

4) Secure and scalable AI inference <br>

Load AI models efficiently (single load at startup, caching). <br>

Add security controls: <br>

file upload security (type/size checks) <br>

rate limiting / basic auth token (if exposed) <br>

sanitization and safe redirects <br>

Prepare scalability path (vector index later: Atlas Vector Search / FAISS / pgvector). <br>

5) AI workflow, testing, and CI/CD readiness <br>

Create a reproducible workflow for: <br>

model selection/versioning

evaluation of search quality (basic metrics)

regression tests for AI endpoints

Ensure CI/CD includes:

unit tests + integration tests

security checks

environment-based configuration

Updated Deliverables
A) Refactored project structure (Blueprint-based)

Deliver a clean architecture:

routes/items.py for product routes

routes/ai.py for AI routes

services/ai/ for embedding + search logic

services/db.py for Mongo connection

B) AI Feature Implementation (Core)

Embedding generation

A module that generates an embedding for each product text

Stored in MongoDB as embedding: [float, float, ...]

Semantic Search endpoint

GET /ai/search?q=... → returns top N most relevant items

Similar Products endpoint

GET /ai/similar/<item_id> → returns similar items

C) Optional AI Enhancements

Auto category suggestion:

POST /ai/suggest-category from description

Tag suggestion:

POST /ai/suggest-tags

Content moderation for uploaded images (basic filtering)

D) Quality, Security, and Performance

Validation layer for form fields

Centralized error handling + logging

Performance optimizations:

model caching

limit returned fields

avoid returning embeddings in responses

E) Testing + Documentation

Unit tests:

embedding generation

cosine similarity ranking

AI endpoints status + correctness

Documentation:

API endpoints (routes + payloads)

setup guide (env vars, run, docker)

AI design note (how embeddings work, limitations)

 ## Required Technical Skills :
> ETL, CI/CD, AI, MLOps, Backend Development<br>

## Storage Systems Needed :
> Data Warehouse, Data Lake<br>

## Tools and Technologies :
> Python, SQL, Apache Spark (Streaming), Kafka Connect and Kafka Streaming, MongoDB, PostgreSQL, Apache Airflow, AWS, Microsoft Azure, Power BI, GitHub Actions, DVC, Docker, Flask<br>
