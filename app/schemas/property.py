from pydantic import BaseModel
from typing import Optional

class PropertyBase(BaseModel):
    name: str
    address: str
    rent: float

class PropertyCreate(PropertyBase):
    owner_id: Optional[int] = None 

class PropertyUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    rent: Optional[float]
    owner_id: Optional[int]
