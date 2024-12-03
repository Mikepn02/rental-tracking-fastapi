from pydantic import BaseModel, EmailStr
from typing import Optional

# Base User schema
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

# Schema for creating a new user
class UserCreate(UserBase):
    password: str

# Schema for updating user details
class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]

# Schema for responses
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# Schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str        