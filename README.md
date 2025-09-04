# Ticket Booking System (FastAPI + SQLite)

A production-ready **Ticket Booking System API** built with **FastAPI** and **SQLite**.  
It supports **user authentication (JWT), event management, bookings, and payments** — designed for scalability and easy deployment.

---

## Features
- **User Registration & Login** (JWT-based authentication)
- **Create & Manage Events** (organizers can add/update events)
- **Book Tickets** for events
- **Track Payments** for bookings
- **SQLite Database** (lightweight and easy to run locally)
- Organized project structure with modular routers and models

---

## Tech Stack
- **Backend**: Python, FastAPI
- **Database**: SQLite (via SQLAlchemy)
- **Authentication**: JWT (JSON Web Tokens)
- **Server**: Uvicorn (ASGI)

---

## Installation and Setup

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd ticket-booking-system


2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables (Optional for JWT/Secrets)**

   ```bash
   export SECRET_KEY="your_secret_key"    # Linux/Mac
   set SECRET_KEY="your_secret_key"       # Windows
   ```

5. **Run the Application**

   ```bash
   uvicorn main:app --reload
   ```

After running, you can access the API documentation at:

* Swagger UI: `http://127.0.0.1:8000/docs`
* Redoc: `http://127.0.0.1:8000/redoc`

---

## Database Setup

- This project uses **SQLite** as the database for simplicity and easy deployment.
- **SQLAlchemy ORM** is used to manage database models and interactions.
- Database tables included:

1. **Users Table**
   - Stores user information: id, username, email, first_name, last_name, hashed_password.
   - Handles authentication and roles (user/admin).

2. **Events Table**
   - Stores event details: id, name, description, date, time, location, price, available_tickets.
   - Supports CRUD operations for event management.

3. **Bookings Table**
   - Stores booking information: id, user_id, event_id, number_of_tickets, booking_date.
   - Links users to the events they have booked.

4. **Payments Table**
   - Stores payment details: id, booking_id, amount, status, payment_date.
   - Tracks successful and pending payments.

**Initializing the Database:**
- The database is automatically created on first run using SQLAlchemy `Base.metadata.create_all(bind=engine)`.
- You can also manually initialize the database via a Python script if needed:

```python
from database import Base, engine
from models import Users, Events, Bookings, Payments

Base.metadata.create_all(bind=engine)
print("Database initialized successfully!")
