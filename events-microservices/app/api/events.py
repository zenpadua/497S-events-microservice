from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import EventOut, EventIn, EventUpdate
from app.api import db_manager

events = APIRouter()

@events.post('/', response_model=EventOut, status_code=201)
async def create_event(payload: EventIn):
    event_id = await db_manager.add_event(payload)

    response = {
        'id': event_id,
        **payload.dict()
    }
    return response

@events.get('/{id}/', response_model=EventOut)
async def get_event(id: int):
    event = await db_manager.get_event(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

