from fastapi import APIRouter, HTTPException
from typing import List

from starlette import responses

from .models import ProfileIn, ProfileOut, ProfileUpdate
from .db_manager import get_all_profiles, get_profiles, add_profile, delete_profiles

profiles = APIRouter()


@profiles.post('/', response_model=ProfileOut, status_code=201)
async def create_profile(payload: ProfileIn):
    profile_id = await add_profile(payload)
    response = {
        'id': profile_id,
        **payload.dict()
    }

    return response

@profiles.get('/{id}/', response_model=ProfileOut)
async def get_cast(id: int):
    profile = await get_profiles(id)
    if not profile:
        raise HTTPException(status_code=404, details='profile not found')
    return profile

@profiles.delete('/{id}/', response_model=None)
async def get_cast(id: int):
    profile = await delete_profiles(id)
    if not profile:
        raise HTTPException(status_code=404, details='profile not found')
    return profile

@profiles.get('/', response_model=List[ProfileOut])
async def get_cast():
    profile = await get_all_profiles()
    if not profile:
        raise HTTPException(status_code=404, details='profile not found')
    return profile