from sqlalchemy import Column,Integer, String , Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Lease(Base):
    __tablename__= "leases"
    id= Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    terms = Column(String, nullable=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    tenant = relationship("Tenant", back_populates="leases")
    property = relationship("Property", back_populates="leases")