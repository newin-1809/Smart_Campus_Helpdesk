# 🎓 Smart Campus Helpdesk API

A backend REST API for a **Smart Campus Helpdesk System** built using **Django** and **Django REST Framework**.

Students can raise issues (tickets), and administrators can manage and resolve them efficiently.

---

## 📌 Project Overview

This project implements a complete backend system featuring:

- CRUD operations
- JWT Authentication
- PostgreSQL integration
- Filtering, Ordering & Pagination
- Search functionality
- Clean RESTful API design
- Future-ready Redis caching structure

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT (JWT Authentication)
- Postman (API Testing)

---

## 📂 Project Structure

smart_campus_helpdesk/
│
├── manage.py
├── smart_campus_helpdesk/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tickets/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...

---

## 🗄 Database Configuration

PostgreSQL is used as the database.

Example configuration in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smart_campus_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
#🎫 Ticket Model

| Field       | Type          | Description                  |
| ----------- | ------------- | ---------------------------- |
| id          | AutoField     | Primary Key                  |
| title       | CharField     | Ticket title                 |
| description | TextField     | Detailed issue               |
| category    | CharField     | classroom / hostel / network |
| priority    | CharField     | low / medium / high          |
| status      | CharField     | open / in-progress / closed  |
| created_at  | DateTimeField | Auto timestamp               |
| updated_at  | DateTimeField | Auto timestamp               |


#🔐 Authentication Flow

1. User logs in using username and password.
2. JWT access and refresh tokens are generated.
3. Access token must be sent in request header:
   Authorization: Bearer <access_token>
4. Admin users can also log in via Django session authentication.


#🔗 API Endpoints
🔑 Authentication
| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Login                |
| POST   | `/api/token/refresh/` | Refresh access token |

🎫 Ticket APIs
| Method | Endpoint         | Description             |
| ------ | ---------------- | ----------------------- |
| POST   | `/tickets/`      | Create ticket           |
| GET    | `/tickets/`      | List tickets            |
| GET    | `/tickets/<id>/` | Retrieve ticket details |
| PATCH  | `/tickets/<id>/` | Update ticket status    |
| DELETE | `/tickets/<id>/` | Delete ticket           |

#📄 Ticket Listing Features

The GET /tickets/ endpoint supports:

#✅ Filtering

?category=classroom

?status=open

#✅ Ordering

?ordering=priority

?ordering=created_at

?ordering=-created_at

#✅ Search

?search=network
(Searches in title and description)

#✅ Pagination

Page-number based pagination

Configurable page size

Example:

GET /tickets/?category=network&ordering=-created_at&page=2

#🚀 Setup Instructions

1️⃣ Clone Repository
git clone <repository-url>
cd smart_campus_helpdesk

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate


5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Development Server
python manage.py runserver

Server URL:

http://127.0.0.1:8000/

#🧪 API Testing

All APIs were tested using Postman.

Include screenshots of:

Token generation

Ticket creation

Filtered results

Pagination output

Update and delete responses


👨‍💻 Author

Smart Campus Helpdesk Backend Assignment
Built with Django & Django REST Framework
by Newin Paul

---




