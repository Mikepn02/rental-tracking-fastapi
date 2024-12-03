from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.property import Property
from app.db.session import get_db
from app.schemas.property import PropertyCreate, PropertyUpdate
# from app.dependencies.auth import admin_required

router = APIRouter()

@router.post("/")
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    new_property = Property(**property.dict())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

@router.get("/")
def list_properties(db: Session = Depends(get_db)):
    return db.query(Property).all()

@router.get("/{property_id}")
def get_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@router.put("/{property_id}")
def update_property(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    for key, value in property.dict(exclude_unset=True).items():
        setattr(db_property, key, value)
    db.commit()
    db.refresh(db_property)
    return db_property

@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(db_property)
    db.commit()
    return {"message": "Property deleted"}
