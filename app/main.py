from fastapi import FastAPI, HTTPException
from app.db import init_db, get_engine
from app.models import Reservation
from app.crud import create_reservation, cancel_reservation
from pydantic import BaseModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

class ReservationCreate(BaseModel):
    unit_id: str
    requester: str
    start_time: str
    end_time: str

@app.post("/reservations")
def post_reservation(data: ReservationCreate):
    from datetime import datetime
    try:
        res = Reservation(
            unit_id=data.unit_id,
            requester=data.requester,
            start_time=datetime.fromisoformat(data.start_time),
            end_time=datetime.fromisoformat(data.end_time)
        )
        return create_reservation(get_engine(), res)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reservations/{id}/cancel")
def cancel(id: int):
    try:
        return cancel_reservation(get_engine(), id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
