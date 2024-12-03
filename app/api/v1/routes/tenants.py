from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.tenants import Tenant
from app.models.property import Property
from app.db.session import get_db
from app.schemas.tenants import TenantCreate, TenantUpdate
# from app.dependencies.auth import admin_required

router = APIRouter()

@router.post("/")
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    existing_tenant = db.query(Tenant).filter(Tenant.email == tenant.email).first()
    if existing_tenant:
        raise HTTPException(status_code=400, detail="Tenant with this email already exists")
    new_tenant = Tenant(**tenant.dict())
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

@router.get("/")
def list_tenants(db: Session = Depends(get_db)):
    return db.query(Tenant).all()

@router.get("/{tenant_id}")
def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@router.put("/{tenant_id}")
def update_tenant(tenant_id: int, tenant: TenantUpdate, db: Session = Depends(get_db)):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    for key, value in tenant.dict(exclude_unset=True).items():
        setattr(db_tenant, key, value)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

@router.delete("/{tenant_id}")
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    db.delete(db_tenant)
    db.commit()
    return {"message": "Tenant deleted"}
