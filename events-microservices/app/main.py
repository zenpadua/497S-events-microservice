from fastapi import FastAPI
from .api.events import events
from .api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/events/openapi.json", docs_url="/api/events/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(events, prefix='/api/events', tags=['events'])
