from typing import List
from fastapi import APIRouter, HTTPException
from starlette import responses
from .models import UserIn, UserOut
from .db_manager import add_user, get_all_users, get_user, delete_user
from .service import is_jobs_present


users = APIRouter()

@users.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    # for job_id in payload.jobs_id:
    if not is_jobs_present(payload.jobs_id):
        raise HTTPException(status_code=404)
    
    job = await add_user(payload=payload)
    response = {
        'id': job,
        **payload.dict()
    }
    return response

@users.get('/', response_model=List[UserOut])
async def get_users():
    return await get_all_users()
