from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Reservation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    unit_id: str
    requester: str
    start_time: datetime
    end_time: datetime
    status: str = Field(default="active")  # "active" or "cancelled"
