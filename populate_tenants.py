from faker import Faker
from app.models.tenants import Tenant
from app.db.session import get_db
from sqlalchemy.orm import Session
import random

# Initialize the Faker instance
fake = Faker()

# Create a function to generate a unique email
def generate_unique_email(db: Session) -> str:
    """Generate a unique email that doesn't exist in the tenants table."""
    while True:
        email = fake.email()  # Generate random email
        if not db.query(Tenant).filter(Tenant.email == email).first():  # Check if email already exists
            return email  # Return email if it's unique

# Create a function to generate and insert tenants with unique emails
def generate_tenants(db: Session, num_tenants: int = 1000):
    tenants = []
    for _ in range(num_tenants):
        name = fake.name()
        email = generate_unique_email(db)  # Ensure unique email
        phone = fake.phone_number()
        property_id = random.choice([None, random.randint(2002, 3001)])  # Adjusted to match valid property IDs
        
        # Create tenant instance
        new_tenant = Tenant(
            name=name,
            email=email,
            phone=phone,
            property_id=property_id
        )
        
        tenants.append(new_tenant)

    # Bulk insert tenants
    db.bulk_save_objects(tenants)
    db.commit()  # Commit once after inserting all tenants
    print(f"{num_tenants} fake tenants inserted into the database.")

# Call the function to insert 1000 tenants
def main():
    db = next(get_db())  # Get the database session
    generate_tenants(db, num_tenants=1000)

if __name__ == "__main__":
    main()
