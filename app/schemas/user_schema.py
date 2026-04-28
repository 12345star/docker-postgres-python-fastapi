from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Schema for creating a new user (Request Body)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Schema for updating a user (Optional fields)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

# Schema for returning user data (Response Body)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        # This tells Pydantic to read data from an ORM object
        from_attributes = True 

# Schema for listing multiple users
class UserListResponse(BaseModel):
    users: List[UserResponse]
