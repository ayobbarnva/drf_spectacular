# 🚀 drf_spectacular

> یک RESTful API ساخته‌شده با Django و Django REST Framework، با Custom User، احراز هویت JWT و مستندسازی تعاملی API.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-REST%20Framework-ff1709?style=for-the-badge)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge)
![Swagger](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=for-the-badge)

---

## ✨ درباره پروژه

این پروژه یک REST API با Django و Django REST Framework است که برای تمرین و پیاده‌سازی مفاهیم واقعی توسعه Backend ساخته شده است.

در پروژه مفاهیمی مانند Custom User، احراز هویت JWT، CRUD، Pagination، مدیریت Article و Comment، مدیریت Advertisement و مستندسازی خودکار API پیاده‌سازی شده‌اند.

## 🔥 امکانات

- 👤 Custom User Model
- 🔐 احراز هویت JWT
- 📝 مدیریت Article
- 💬 مدیریت Comment
- 📢 مدیریت Advertisement
- 📄 Pagination
- 🔄 عملیات CRUD
- 📚 تولید خودکار OpenAPI Schema
- 🧭 Swagger UI برای مشاهده و تست API
- 🛡️ Authentication و Permission

## 🧰 تکنولوژی‌ها

| تکنولوژی | کاربرد |
|---|---|
| 🐍 Python 3.13 | زبان برنامه‌نویسی |
| 🎯 Django 4.2 | Backend Framework |
| 🔌 Django REST Framework | ساخت REST API |
| 🔐 Simple JWT | احراز هویت |
| 📚 drf-spectacular | مستندسازی OpenAPI 3.0 |
| 🧪 Swagger UI | مشاهده و تست API |
| 🗄️ SQLite | پایگاه داده توسعه |

## 📖 مستندات API

پس از اجرای پروژه، مستندات تعاملی API در دسترس هستند:

```text
/schema/
```

و:

```text
/swagger/
```

## ⚙️ نصب و اجرا

```bash
git clone https://github.com/ayobbarnva/drf_spectacular.git
cd drf_spectacular
```

ساخت محیط مجازی:

```bash
python -m venv venv
source venv/bin/activate
```

نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

ساخت و اجرای Migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

ساخت Superuser:

```bash
python manage.py createsuperuser
```

اجرای سرور:

```bash
python manage.py runserver
```

سپس API در آدرس زیر در دسترس خواهد بود:

```text
http://127.0.0.1:8000/
```

## 🔐 احراز هویت JWT

برای دریافت Token:

```http
POST /api/token/
```

نمونه درخواست:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

سپس Access Token را در Header ارسال کنید:

```http
Authorization: Bearer <your_access_token>
```

## 🎯 هدف پروژه

هدف پروژه، تمرین توسعه Backend، طراحی REST API، Authentication، Serializer، CRUD، Pagination و مستندسازی API با Django REST Framework است.

## 👨‍💻 سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ اگر پروژه برایتان مفید بود، می‌توانید به Repository Star بدهید.

## ⚠️ توجه

این پروژه با هدف آموزشی و توسعه Backend ساخته شده است.
