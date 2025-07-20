from fastapi import FastAPI
from app.database import engine
from app import models
from routers import users, events, bookings, payments

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Ticket Booking System",
    description="Production-ready ticket booking API with JWT authentication",
    version="1.0.0",
)

# Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(bookings.router, prefix="/bookings", tags=["Bookings"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

@app.get("/")
def root():
    return {"message": "Ticket Booking API is running"}
