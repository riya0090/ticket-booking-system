from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app import models, schemas
from app.database import get_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/", response_model=schemas.BookingOut)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == booking.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.available_tickets < booking.tickets_booked:
        raise HTTPException(status_code=400, detail="Not enough tickets")
    total_price = event.price * booking.tickets_booked
    event.available_tickets -= booking.tickets_booked
    db_booking = models.Booking(user_id=1, event_id=booking.event_id,
                                tickets_booked=booking.tickets_booked,
                                total_price=total_price)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
