# Project_for_App_integrated_IA :

![Capture d’écran 2024-06-18 025048](https://github.com/GDIATTA/Project_for_-App_integrated_IA/assets/147615966/1b46be79-3a05-45ae-98c2-236363e3ad09)

## Project Goals :
> **1) Backend foundations (your current scope, improved)** <br>

>> Build and maintain a backend to store product data (name, price, category, tags, description, image) in MongoDB.<br>

>> Ensure reliable image upload, storage, and retrieval with validation and safe file handling. <br>

>> Standardize API responses and errors, and introduce input validation for form/API payloads. <br>

> **2) AI-ready data and feature storage** <br>

>> Enrich each product at ingestion time with AI features: <br>

>>> Text embedding from (name + description + tags + category) <br>

>>> Optional: extracted keywords, normalized category, metadata <br>

>>> Store AI features in MongoDB (embedding, ai_tags, ai_category_confidence, etc.). <br>

> **3) AI capabilities integrated into the backend** <br>

>> Implement AI endpoints/services to support: <br>

>>> Semantic search (“smart search” beyond keywords) <br>

>>> Similar products recommendations (kNN / cosine similarity over embeddings) <br>

>>> Auto-tagging / category suggestion from description (optional) <br>

>>> Integrate AI into the existing posting flow (/posting/) so that AI enrichment happens automatically after insert. <br>

> **4) Secure and scalable AI inference** <br>

>> Load AI models efficiently (single load at startup, caching). <br>

>> Add security controls: <br>

>>> file upload security (type/size checks) <br>

>>> rate limiting / basic auth token (if exposed) <br>

>>> sanitization and safe redirects <br>

>>> Prepare scalability path (vector index later: Atlas Vector Search / FAISS / pgvector). <br>

> **5) AI workflow, testing, and CI/CD readiness** <br>

>> Create a reproducible workflow for: <br>

>>> model selection/versioning <br>

>>> evaluation of search quality (basic metrics) <br>

>>> regression tests for AI endpoints <br>

>> Ensure CI/CD includes: <br>

>>> unit tests + integration tests <br>

>>> security checks <br>

>>> environment-based configuration <br>

## Deliverables :
> **A) Refactored project structure (Blueprint-based)** <br>

>> Deliver a clean architecture: <br> 

>> routes/items.py for product routes <br>

>> routes/ai.py for AI routes <br>

>> services/ai/ for embedding + search logic <br>

>> services/db.py for Mongo connection <br>

> **B) AI Feature Implementation (Core)** <br>

>> Embedding generation <br>

>> A module that generates an embedding for each product text <br>

>> Stored in MongoDB as embedding: [float, float, ...] <br>

>> Semantic Search endpoint <br>

>> GET /ai/search?q=... → returns top N most relevant items <br>

>> Similar Products endpoint <br>

>> GET /ai/similar/<item_id> → returns similar items <br>

> **C) Optional AI Enhancements** <br>

>> Auto category suggestion: <br>

>>> POST /ai/suggest-category from description <br>

>> Tag suggestion: <br>

>>> POST /ai/suggest-tags <br>

>>> Content moderation for uploaded images (basic filtering) <br>

> **D) Quality, Security, and Performance** <br>

>> Validation layer for form fields <br>

>> Centralized error handling + logging <br>

>> Performance optimizations: <br>

>>> model caching <br>

>>> limit returned fields <br>

>>> avoid returning embeddings in responses <br>

> **E) Testing + Documentation** <br>

>> Unit tests: <br>

>> embedding generation <br>

>> cosine similarity ranking <br>

>> AI endpoints status + correctness <br>

## Documentation:

> API endpoints (routes + payloads) <br>

> setup guide (env vars, run, docker) <br>

> AI design note (how embeddings work, limitations) <br>

 ## Required Technical Skills :
> ETL, CI/CD, AI, MLOps, Backend Development<br>

## Storage Systems Needed :
> Data Warehouse, Data Lake<br>

## Tools and Technologies :
> Python, SQL, Apache Spark (Streaming), Kafka Connect and Kafka Streaming, MongoDB, PostgreSQL, Apache Airflow, AWS, Microsoft Azure, Power BI, GitHub Actions, DVC, Docker, Flask<br>
