from pydantic import BaseModel


class User(BaseModel):
    name: str
    job: str


class UserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
