# 🚀 drf_spectacular

> یک RESTful API ساخته‌شده با Django و Django REST Framework، با Custom User، احراز هویت JWT و مستندسازی تعاملی API.

## ✨ درباره پروژه

این پروژه برای تمرین و پیاده‌سازی مفاهیم واقعی توسعه Backend ساخته شده است و شامل Authentication، CRUD، Pagination و مستندسازی خودکار OpenAPI است.

## 🔥 امکانات

- 👤 مدل کاربر اختصاصی
- 🔐 احراز هویت JWT
- 📝 مدیریت Article و Comment
- 📢 مدیریت Advertisement
- 📄 Pagination
- 🔄 عملیات CRUD
- 📚 OpenAPI Schema
- 🧭 Swagger UI
- 🛡️ Authentication و Permission

## 🧰 تکنولوژی‌ها

| تکنولوژی | کاربرد |
|---|---|
| 🐍 Python 3.13 | زبان برنامه‌نویسی |
| 🎯 Django 4.2 | Backend Framework |
| 🔌 Django REST Framework | ساخت REST API |
| 🔐 Simple JWT | احراز هویت |
| 📚 drf-spectacular | مستندسازی OpenAPI |
| 🧪 Swagger UI | مشاهده و تست API |
| 🗄️ SQLite | پایگاه داده توسعه |

## 📖 مستندات API

```text
/schema/
/swagger/
```

## ⚙️ نصب و اجرا

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

در Windows برای فعال‌سازی محیط مجازی:

```powershell
venv\Scripts\activate
```

## 🔐 احراز هویت JWT

```http
POST /api/token/
```

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

برای درخواست‌های محافظت‌شده:

```http
Authorization: Bearer <access_token>
```

## 🎯 هدف پروژه

تمرین توسعه Backend، طراحی REST API، Authentication، Serializer، CRUD، Pagination و مستندسازی API با Django REST Framework.

## 👨‍💻 سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ اگر پروژه برایتان مفید بود، به Repository Star بدهید.

## توضیح درباره استفاده از هوش مصنوعی

