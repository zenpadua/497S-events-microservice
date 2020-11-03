from typing import List
from fastapi import APIRouter, HTTPException

from .models import EventOut, EventIn, EventUpdate
from ..api import db_manager

events = APIRouter()

### Gets all events in the database
@events.get('/')
async def hello_world():
    return {"Hello: World"}
'''
### Gets all events in the database 
@events.get('/')
async def get_events():
    return await db_manager.get_all_events()


### Gets a specific event based on id given, else returns 404
@events.get('/{id}/', response_model=EventOut)
async def get_event(id: int):
    event = await db_manager.get_event(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

### Creates an event
@events.post('/', response_model=EventOut, status_code=201)
async def create_event(payload: EventIn):
    event_id = await db_manager.add_event(payload)

    response = {
        'id': id,
        **payload.dict()
    }
    return response

### Updates an event based on id given, else returns 404 
@events.put('/{id}')
async def update_event(id:int, payload: EventIn):
    event = await db_manager.get_event(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    update_data = payload.dict(exclude_unset=True)
    event_in_db = EventIn(**event)

    updated_event = event_in_db.copy(update=update_data)
    return await db_manager.update_event(id, updated_event)

### Deletes an event based on id given, else returns 404
@events.delete('/{id}', response_model=None)
async def delete_event(id: int):
    event = await db_manager.get_event(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return await db_manager.delete_event(id)'''