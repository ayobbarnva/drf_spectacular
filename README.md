# 🚀 drf_spectacular

> A RESTful API built with Django and Django REST Framework, featuring a custom user model, JWT authentication, and interactive API documentation.

🇬🇧 [English](README.md) | 🇮🇷 [فارسی](README.fa.md)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-ff1709?style=for-the-badge)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge)
![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=for-the-badge)

---

## ✨ About

A Django REST API project focused on backend development, authentication, CRUD operations, pagination, and automatic OpenAPI documentation.

## 🔥 Features

- 👤 Custom User Model
- 🔐 JWT Authentication
- 📝 Articles & Comments
- 📢 Ads Module
- 📄 Pagination
- 🔄 CRUD operations
- 📚 Automatic OpenAPI Schema
- 🧭 Swagger UI
- 🛡️ Authentication & Permissions

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| 🐍 Python 3.13 | Programming language |
| 🎯 Django 4.2 | Backend framework |
| 🔌 Django REST Framework | REST API development |
| 🔐 Simple JWT | Authentication |
| 📚 drf-spectacular | OpenAPI documentation |
| 🧪 Swagger UI | API testing and documentation |
| 🗄️ SQLite | Development database |

## 📖 API Documentation

Raw OpenAPI schema:

```text
/schema/
```

Interactive Swagger UI:

```text
/swagger/
```

## ⚙️ Installation

```bash
git clone https://github.com/ayobbarnva/drf_spectacular.git
cd drf_spectacular
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

On Windows:

```powershell
venv\Scripts\activate
```

## 🔐 JWT Authentication

Get a token with:

```http
POST /api/token/
```

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Use the access token:

```http
Authorization: Bearer <access_token>
```

## 🎯 Goal

This project is a practical exercise in Django REST API development, authentication, serializers, CRUD, pagination, and API documentation.

## 👨‍💻 Author

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ If you find it useful, give the repository a star.
