from fastapi import FastAPI
from .api.db import metadata, database, engine
from .api.users import users

from starlette.middleware.cors import CORSMiddleware


metadata.create_all(engine)

app = FastAPI(title="User Profile Service Backend")
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users, prefix='/api/v1/users')
