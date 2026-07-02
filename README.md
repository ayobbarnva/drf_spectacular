# 🚀 drf_spectacular

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A RESTful API built with **Django** and **Django REST Framework (DRF)**, featuring a custom user model, JWT-based authentication, and auto-generated interactive API documentation.

## ✨ Features

- **Custom User Model** — extends `AbstractBaseUser` for flexible, project-specific authentication
- **JWT Authentication** — secure token-based auth powered by `djangorestframework-simplejwt`
- **Articles & Comments** — CRUD endpoints for articles and their comments
- **Ads Module** — endpoints for managing advertisement listings with pagination
- **Auto-generated API Schema** — OpenAPI 3.0 schema generated automatically with `drf-spectacular`
- **Interactive Swagger UI** — browse and test all endpoints directly from the browser

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.13 |
| Framework | Django 4.2 |
| API | Django REST Framework |
| Auth | djangorestframework-simplejwt |
| API Docs | drf-spectacular (OpenAPI 3.0) |
| Database | SQLite (development) |

## 📖 API Documentation

This project uses `drf-spectacular` to automatically generate an OpenAPI 3.0 schema directly from the codebase — no manual documentation needed. Interactive docs are available out of the box:

- **Schema (raw)**: `/schema/`
- **Swagger UI**: `/swagger/`

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ayobbarnva/drf_spectacular.git
cd drf_spectacular
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`, with interactive docs at `http://127.0.0.1:8000/swagger/`.

## 🔐 Authentication

This project uses JWT authentication. To obtain a token:

```
POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}
```

Use the returned `access` token in the `Authorization` header for authenticated requests:

```
Authorization: Bearer <your_access_token>
```

## 📄 License

This project is open source and available for personal and educational use.
