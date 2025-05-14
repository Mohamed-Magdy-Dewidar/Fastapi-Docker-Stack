# 🚀 FastAPI Docker Stack

A production-ready FastAPI application scaffolded with Docker, PostgreSQL, Redis, and optional Nginx reverse proxy. This stack supports scalable backend development with service isolation, environment configuration, and container orchestration using Docker Compose.

---

## 📦 Features

- ⚡ **FastAPI** — High-performance Python web framework for building APIs
- 🐳 **Docker & Compose** — Containerized architecture for development and deployment
- 🐘 **PostgreSQL** — Robust, scalable SQL database
- 🚀 **Redis** — In-memory caching and task/message queuing
- 🌐 **Nginx (optional)** — Reverse proxy setup for production environments
- 🔧 Easy local development and deployment

---

## 🛠️ Stack Overview

| Service     | Role                       | Port        |
|-------------|----------------------------|-------------|
| `web`       | FastAPI app using Uvicorn  | `6000`      |
| `db`        | PostgreSQL database        | `5432`      |
| `cache`     | Redis in-memory store      | `6379`      |
| `proxy`     | Nginx reverse proxy (opt)  | `80` → `6000` |

---


## 📁 Project Structure
.
├── app/
│ ├── main.py # FastAPI entrypoint
│ └── ...
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build for FastAPI
├── docker-compose.yml # Multi-container setup
└── README.md # You’re here!

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fastapi-docker-stack.git

cd fastapi-docker-stack

2. Start Services

run the command : docker-compose up --build






🧪 Testing
Use the following methods to test the FastAPI app:




✅ CURL
curl -v http://localhost/
{
  "message": "Welcome to the FastAPI application!"
}
curl -v http://localhost/redis
{
    "redis_value": "Hello from Redis!"
}
curl -v http://localhost/postgres
{
  "postgres_status": "Connected successfully"
}


✅ Browser
Open http://localhost/ in your browser.

