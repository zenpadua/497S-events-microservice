from pydantic import BaseModel
from typing import List, Optional

class EventIn(BaseModel):
    title: str
    description: str
    people: List[str]


class EventOut(EventIn):
    id: int


class EventUpdate(EventIn):
    name: Optional[str] = None
    description: Optional[str] = None
    people: Optional[List[str]] = None