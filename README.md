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
```
---
## Usage

Follow these steps to use the Ticket Booking System API:

1. **Sign Up**
   - Create a new user account via the signup endpoint or registration page.
   
2. **Login**
   - Login with your credentials to receive a **JWT token**.
   - Include this token in the Authorization header for any protected requests:
     ```
     Authorization: Bearer <your_token>
     ```

3. **Browse Events**
   - View the list of available events.
   - Check event details such as date, time, location, price, and available tickets.

4. **Book Tickets**
   - Select an event and specify the number of tickets to book.
   - Booking will automatically update the available tickets.

5. **Make Payments**
   - Complete the payment for your booked tickets (simulated payment integration).
   - Check the status of your payments (success/pending).

6. **Admin Actions (Optional)**
   - If logged in as an admin, you can manage events:
     - Create new events
     - Update existing events
     - Delete events
   - Admins can also view user and booking reports.

**Tip:**  
- Always keep your JWT token safe and include it in requests that require authentication.
- Users can view their own bookings and payment history at any time.

---

## Future Enhancements

Planned improvements to make the Ticket Booking System even more powerful:

1. **Real Payment Gateway Integration**  
   - Integrate with Stripe, Razorpay, or PayPal for live payments.

2. **Email & SMS Notifications**  
   - Send confirmation emails or SMS for bookings, cancellations, and reminders.

3. **Event Search and Filtering**  
   - Allow users to search events by name, date, location, or category.

4. **User Roles & Permissions**  
   - Implement more granular roles (e.g., event organizers, moderators) with restricted access.

5. **Frontend Interface**  
   - Build a user-friendly web or mobile interface for easier navigation.

6. **Reporting & Analytics**  
   - Provide dashboards for admin to track bookings, revenue, and user activity.

7. **Multi-language Support**  
   - Add localization to support multiple languages for users worldwide.

