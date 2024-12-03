from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.lease import Lease
from app.models.tenants import Tenant
from app.models.property import Property
from app.db.session import get_db
from app.schemas.lease import LeaseCreate, LeaseUpdate
# from app.dependencies.auth import admin_required

router = APIRouter()

@router.post("/")
def create_lease(lease: LeaseCreate, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == lease.tenant_id).first()
    property = db.query(Property).filter(Property.id == lease.property_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    new_lease = Lease(**lease.dict())
    db.add(new_lease)
    db.commit()
    db.refresh(new_lease)
    return new_lease

@router.get("/")
def list_leases(db: Session = Depends(get_db)):
    return db.query(Lease).all()

@router.get("/{lease_id}")
def get_lease(lease_id: int, db: Session = Depends(get_db)):
    lease = db.query(Lease).filter(Lease.id == lease_id).first()
    if not lease:
        raise HTTPException(status_code=404, detail="Lease not found")
    return lease

@router.put("/{lease_id}")
def update_lease(lease_id: int, lease: LeaseUpdate, db: Session = Depends(get_db)):
    db_lease = db.query(Lease).filter(Lease.id == lease_id).first()
    if not db_lease:
        raise HTTPException(status_code=404, detail="Lease not found")
    for key, value in lease.dict(exclude_unset=True).items():
        setattr(db_lease, key, value)
    db.commit()
    db.refresh(db_lease)
    return db_lease

@router.delete("/{lease_id}")
def delete_lease(lease_id: int, db: Session = Depends(get_db)):
    db_lease = db.query(Lease).filter(Lease.id == lease_id).first()
    if not db_lease:
        raise HTTPException(status_code=404, detail="Lease not found")
    db.delete(db_lease)
    db.commit()
    return {"message": "Lease deleted"}
