from pydantic import BaseModel, EmailStr
from typing import Optional

class TenantBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    property_id: Optional[int] = None


class TenantCreate(TenantBase):
    pass

class TenantUpdate(TenantBase):
    pass