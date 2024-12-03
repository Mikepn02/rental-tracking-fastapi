from pydantic import BaseModel
from datetime import date

class LeaseBase(BaseModel):
    start_date: date
    end_date: date
    terms: str
    tenant_id: int
    property_id: int

class LeaseCreate(LeaseBase):
    pass

class LeaseUpdate(LeaseBase):
    pass
