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
