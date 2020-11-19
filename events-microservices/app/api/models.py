from pydantic import BaseModel
from typing import List, Optional

class EventIn(BaseModel):
    title: str
    description: str
    people: List[str]
    start_time: str
    end_time: str


class EventOut(EventIn):
    id: int


class EventUpdate(EventIn):
    title: Optional[str] = None
    description: Optional[str] = None
    people: Optional[List[str]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None