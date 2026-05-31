# 📰 Core — Blog & Comment REST API

A full-featured Blog and Comment REST API built with **Django** and **Django REST Framework**, containerized with Docker.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2, Django REST Framework |
| Database | PostgreSQL 15 |
| Auth | JWT (SimpleJWT) + Djoser |
| API Docs | drf-spectacular (Swagger / Redoc) |
| Email | django-templated-email + smtp4dev |
| Task Queue | Celery + Redis |
| Scheduler | django-celery-beat |
| Cache | django-redis |
| Testing | pytest + pytest-django + Faker |

---

## 📁 Project Structure

```
core/
├── accounts/        # User auth (register, login, reset password)
├── blog/            # Blog posts
├── comment/         # Comments on posts
├── core/            # Django project settings & Celery config
├── templates/       # HTML & email templates
├── static/          # Static files
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

---

## ⚙️ Getting Started

### Prerequisites

- Docker & Docker Compose installed

### 1. Clone the repository

```bash
git clone https://github.com/amirmad2007/core.git
cd core
```

### 2. Create `.env` file

```env
SECRET_KEY=django-insecure-testkey123
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,backend 

# Database
POSTGRES_DB=django_db
POSTGRES_USER=django
POSTGRES_PASSWORD=django
```

### 3. Run with Docker

```bash
docker-compose up --build
```

### 4. Apply migrations

```bash
docker-compose exec backend python manage.py migrate
```

### 5. Create superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

---

## 🌐 Services & Ports

| Service | URL |
|---|---|
| Django API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/api/schema/swagger-ui/ |
| Redoc | http://localhost:8000/api/schema/redoc/ |
| smtp4dev (Email UI) | http://localhost:3000 |
| Redis | localhost:6379 |

---

## 📬 API Endpoints

### Accounts
| Method | Endpoint | Description |
|---|---|---|
| POST | `/accounts/api/v1/register/` | Register new user |
| POST | `accounts/api/v1/jwt/create/` | Login & get JWT token |
| POST | `/accounts/api/v1/jwt/refresh/` | Refresh JWT token |
| POST | `/accounts/api/v1/request-to-rest-password/` | Request password reset |
| GET | `/accounts/api/v1/profile/` | Get user profile |

### Blog
| Method | Endpoint | Description |
|---|---|---|
| GET | `/blog/api/v1/post/` | List all posts |
| POST | `/blog/api/v1/post/` | Create a post |
| GET | `/blog/api/v1/post/{id}/` | Retrieve a post |
| PUT | `/blog/api/v1/post/{id}/` | Update a post |
| DELETE | `/blog/api/v1/post/{id}/` | Delete a post |

### Comments
| Method | Endpoint | Description |
|---|---|---|
| GET | `/comment/api/v1/comment/` | List all comments |
| POST | `/comment/api/v1/comment/` | Create a comment |
| GET | `/comment/api/v1/comment/{id}/` | Retrieve a comment |
| PUT | `/comment/api/v1/comment/{id}/` | Update a comment |
| DELETE | `/comment/api/v1/comment/{id}/` | Delete a comment |

---

## 🧪 Running Tests

```bash
# Run all tests
docker-compose exec backend pytest

# With verbose output
docker-compose exec backend pytest -v

# Specific app
docker-compose exec backend pytest accounts/tests/
```

---

## 🔧 Celery Workers

```bash
# Worker
docker-compose exec worker celery -A core worker --loglevel=info

# Beat Scheduler
docker-compose exec beat celery -A core beat --loglevel=info
```

---

## 📄 License

MIT License — Copyright (c) 2026 amirmad2007
