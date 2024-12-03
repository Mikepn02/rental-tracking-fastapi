from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    rent = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Relationships
    owner = relationship("User", back_populates="properties")  # Existing relationship
    tenants = relationship("Tenant", back_populates="property")  # Existing relationship
    leases = relationship("Lease", back_populates="property")  # Add this line
