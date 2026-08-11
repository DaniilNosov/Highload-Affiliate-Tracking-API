# Highload Affiliate Tracking API (TDS & Postback Microservice)

A high-performance, asynchronous Traffic Delivery System (TDS) and Postback processing microservice built for iGaming and affiliate marketing networks. Designed to handle high volumes of incoming traffic with minimal latency using non-blocking I/O and deferred background tasks.

---

## 🚀 Key Features

* **Traffic Delivery System (TDS):** Instantly generates unique tracking IDs (`click_id`), caches metadata in memory, and performs fast HTTP redirects to advertisers.
* **Asynchronous Architecture:** Built on **FastAPI** and **SQLAlchemy (AsyncIO)** for maximum concurrency and throughput.
* **Low-Latency Caching:** Utilizes **Redis** to store active click sessions with automatic expiration.
* **Server-to-Server (S2S) Postbacks:** Handles conversion tracking asynchronously, instantly responding to advertisers while delegating database writes to background workers.
* **Background Processing:** Powered by **Celery** to safely update financial balances and write conversions without blocking the main event loop.
* **Containerized Environment:** Fully dockerized with `docker-compose`, including health checks and isolated networking.
* **Admin Management:** Dedicated endpoints for managing advertising offers and tracking performance.

---

## Tech Stack

* **Backend:** Python, FastAPI, Pydantic (v2)
* **Database & ORM:** PostgreSQL, SQLAlchemy (Async), Alembic (migrations)
* **Broker & Queue:** Redis, Celery
* **Infrastructure:** Docker, Docker Compose, pgAdmin
📂 Project Structure

```text
├── api/                  # FastAPI routers (TDS, Postbacks, Offers)
├── core/                 # Configuration, database session, and core settings
├── models/               # SQLAlchemy database models
├── workers/              # Celery configuration and background tasks
├── .env                  # Environment variables (not tracked in git)
├── Dockerfile            # Container definition for API & Celery
├── docker-compose.yml    # Multi-container orchestration setup
└── main.py               # Application entry point
⚙️ Getting Started & Installation

1. Clone the repository
Bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
2. Configure Environment Variables
Create a .env file in the root directory and specify your configuration:

3. Run with Docker Compose
Build and start all services in detached mode:

Bash
docker-compose up --build -d
🔌 API Endpoints Overview
GET /click — Captures incoming traffic, generates a unique click_id, logs metadata to Redis, and redirects the user to the advertiser.

POST /s2s/postback — Receives conversion data from advertisers and triggers background processing.

POST /admin/offers/ — Admin endpoint to create new advertising campaigns.

GET /docs — Interactive API documentation (Swagger UI).

Accessing Services
Swagger Documentation: http://localhost:8000/docs

pgAdmin Database UI: http://localhost:5050 (Login with credentials defined in docker-compose)