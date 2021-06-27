from pydantic import BaseModel
from typing import Optional, List


class UserIn(BaseModel):
    name: str
    gender: str
    email: str
    jobs_id: int

class UserOut(BaseModel):
    id: int
    name: str
    gender: str
    email: str
    jobs_id: int
