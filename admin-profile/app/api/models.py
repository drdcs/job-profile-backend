from pydantic import BaseModel
from typing import Optional


class ProfileIn(BaseModel):
    name: str
    experience: str
    location: Optional[str]
    details: Optional[str]


class ProfileOut(ProfileIn):
    id: int

class ProfileUpdate(ProfileIn):
    name: Optional[str] = None