from pydantic import BaseModel, Extra


class User(BaseModel, extra=Extra.forbid):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel, extra=Extra.forbid):
    url: str
    text: str


class UserResponse(BaseModel, extra=Extra.forbid):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]
    support: Support
