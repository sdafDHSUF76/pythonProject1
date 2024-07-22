from pydantic import BaseModel, Extra


class User(BaseModel, extra=Extra.forbid):
    name: str
    job: str


class UserResponse(BaseModel, extra=Extra.forbid):
    name: str
    job: str
    id: str
    createdAt: str
