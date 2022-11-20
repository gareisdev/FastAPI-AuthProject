from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    username: str
    password: str
    email_address: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: bool = True


class UserResponse(BaseModel):
    id: int
    username: str
    email_address: str
    first_name: Optional[str]
    last_name: Optional[str]
