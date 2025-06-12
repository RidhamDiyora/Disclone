# django-studybud

# 📢 Discord Clone

A full-stack web application inspired by **Discord**, built using **Django, HTML, CSS, and JavaScript**. The application allows users to register, create groups, manage profiles, and communicate within group chats. This project focuses on implementing key Discord-like features along with secure user authentication and database management.

---

## 🚀 Features

* User authentication (Registration, Login, Logout)
* User profile management with profile picture uploads
* Group creation and management functionality
* CRUD operations for groups and user data
* Image upload and storage support
* Responsive and user-friendly web interface
* Backend powered by Django ORM for efficient database operations

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django ORM
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (can be configured to use PostgreSQL/MySQL)
* **Version Control:** Git, GitHub

---

## 📦 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/discord-clone.git
   cd discord-clone
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📌 Future Improvements

* Real-time messaging using WebSockets (Django Channels)
* Direct messaging and group chat enhancements
* Notifications system
* Deployment to production environment

