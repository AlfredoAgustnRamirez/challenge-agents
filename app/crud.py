from sqlmodel import Session, select
from app.models import Reservation
from datetime import datetime
import json

def load_inventory():
    with open("inventory.json", "r") as f:
        return {item["id"]: item for item in json.load(f)}

def create_reservation(engine, reservation_data):
    inventory = load_inventory()
    if reservation_data.unit_id not in inventory:
        raise ValueError("Unidad no válida")
    
    if not reservation_data.requester.strip():
        raise ValueError("Solicitante no puede estar vacío")
    
    if reservation_data.start_time >= reservation_data.end_time:
        raise ValueError("Fecha de inicio debe ser anterior a la de fin")

    with Session(engine) as session:
        # Verificar superposición
        statement = select(Reservation).where(
            Reservation.unit_id == reservation_data.unit_id,
            Reservation.status == "active",
            Reservation.start_time < reservation_data.end_time,
            Reservation.end_time > reservation_data.start_time
        )
        existing = session.exec(statement).first()
        if existing:
            raise ValueError("Superposición de horario")
        
        session.add(reservation_data)
        session.commit()
        session.refresh(reservation_data)
        return reservation_data

def cancel_reservation(engine, reservation_id):
    with Session(engine) as session:
        res = session.get(Reservation, reservation_id)
        if not res:
            raise ValueError("Reserva no encontrada")
        res.status = "cancelled"
        session.add(res)
        session.commit()
        return res
