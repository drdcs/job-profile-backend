from .models import UserIn, UserOut
from .db import users, database

async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)

async def get_user(id: int):
    query = users.select().where(users.c.id==id)
    return await database.fetch_one(query=query)

async def delete_user(id: int):
    query = users.delete().where(users.c.id==id)
    return await database.execute(query=query)
