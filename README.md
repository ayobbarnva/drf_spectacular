# 🚀 drf_spectacular

> A RESTful API built with Django and Django REST Framework, featuring a custom user model, JWT authentication, and interactive API documentation.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-ff1709?style=for-the-badge)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge)
![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=for-the-badge)

## ✨ About

A Django REST API project focused on backend development, authentication, CRUD operations, pagination, and automatic OpenAPI documentation.

### 🇮🇷 درباره پروژه

یک REST API ساخته‌شده با Django و Django REST Framework که برای تمرین و پیاده‌سازی مفاهیم واقعی Backend توسعه داده شده است.

## 🔥 Features | امکانات

- 👤 Custom User Model — مدل کاربر اختصاصی
- 🔐 JWT Authentication — احراز هویت JWT
- 📝 Articles & Comments — مدیریت مقاله و نظر
- 📢 Ads Module — مدیریت آگهی‌ها
- 📄 Pagination — صفحه‌بندی نتایج
- 🔄 CRUD — عملیات ایجاد، خواندن، ویرایش و حذف
- 📚 OpenAPI Schema — تولید خودکار مستندات
- 🧭 Swagger UI — مشاهده و تست API
- 🛡️ Authentication & Permissions — احراز هویت و دسترسی‌ها

## 🧰 Tech Stack | تکنولوژی‌ها

| Technology | کاربرد |
|---|---|
| 🐍 Python 3.13 | زبان برنامه‌نویسی |
| 🎯 Django 4.2 | Backend Framework |
| 🔌 Django REST Framework | ساخت REST API |
| 🔐 Simple JWT | احراز هویت |
| 📚 drf-spectacular | مستندسازی OpenAPI 3.0 |
| 🧪 Swagger UI | مشاهده و تست API |
| 🗄️ SQLite | پایگاه داده توسعه |

## 📖 API Documentation | مستندات API

Raw OpenAPI schema:

```text
/schema/
```

Interactive Swagger UI:

```text
/swagger/
```

## ⚙️ Installation | نصب و اجرا

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

در ویندوز برای فعال‌سازی محیط مجازی از `venv\Scripts\activate` استفاده کنید.

## 🔐 JWT Authentication | احراز هویت

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

برای درخواست‌های محافظت‌شده، Access Token را در Header بالا ارسال کنید.

## 🎯 Goal | هدف پروژه

This project is a practical exercise in Django REST API development, authentication, serializers, CRUD, pagination, and API documentation.

هدف پروژه تمرین توسعه Backend، طراحی REST API، Authentication، Serializer، CRUD، Pagination و مستندسازی API است.

## 👨‍💻 Author | سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ If you find it useful, give the repository a star.

⭐ اگر پروژه برایتان مفید بود، خوشحال می‌شوم به آن Star بدهید.
