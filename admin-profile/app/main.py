
from fastapi import FastAPI
from .api.db import metadata, database, engine
from .api.job_profile import profiles

from starlette.middleware.cors import CORSMiddleware


metadata.create_all(engine)

app = FastAPI(
    title="profile-admin-page-backend", 
    )

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"]
    )


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(profiles, prefix='/api/v1/jobs')

