from fastapi import FastAPI
from app.core.config import settings
from app.db.session import SessionLocal, engine
from app.api.v1.routes import property, tenants, lease, auth
from app.db.base_class import Base



Base.metadata.create_all(bind=engine)

   


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A system to manage rental properties, tenant records, and lease agreements.",
    version="1.0.0",
    contact={
        "name": "NZABERA Mike Peter",
        "email": "nzaberamikepeter@gmail.com",
    },
)
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(property.router, prefix="/api/v1/properties", tags=["Properties"])
app.include_router(tenants.router, prefix="/api/v1/tenants", tags=["Tenants"])
app.include_router(lease.router, prefix="/api/v1/leases", tags=["Leases"])