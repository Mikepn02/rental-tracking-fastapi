from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=True)

    property = relationship("Property", back_populates="tenants")  
    leases = relationship("Lease", back_populates="tenant")  
