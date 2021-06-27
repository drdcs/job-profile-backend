import databases
from .models import ProfileIn, ProfileOut, ProfileUpdate
from .db import JobProfile, database


async def add_profile(payload: ProfileIn):
    query = JobProfile.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_profiles(id):
    query = JobProfile.select().where(JobProfile.c.id==id)
    return await database.fetch_one(query=query)

async def get_all_profiles():
    query = JobProfile.select()
    return await database.fetch_all(query=query)

async def delete_profiles(id):
    query = JobProfile.delete().where(JobProfile.c.id==id)
    await database.execute(query)
    return {"message": "JobProfile with id: {} deleted successfully!".format(id)}