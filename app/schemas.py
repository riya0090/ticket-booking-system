from pydantic import BaseModel
from datetime import datetime

# -------- Users --------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        from_attributes = True

# -------- Events --------
class EventCreate(BaseModel):
    name: str
    description: str
    date: datetime
    price: float
    total_tickets: int

class EventOut(EventCreate):
    id: int
    available_tickets: int
    class Config:
        from_attributes = True

# -------- Bookings --------
class BookingCreate(BaseModel):
    event_id: int
    tickets_booked: int

class BookingOut(BaseModel):
    id: int
    event_id: int
    tickets_booked: int
    total_price: float
    booking_date: datetime
    class Config:
        from_attributes = True

# -------- Auth --------
class Token(BaseModel):
    access_token: str
    token_type: str
