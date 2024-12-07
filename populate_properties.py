from sqlalchemy.orm import Session
from faker import Faker
from app.models.property import Property
from app.db.session import get_db
from app.main import app
import random

# Initialize Faker
fake = Faker()

def generate_fake_properties(db: Session, num_records: int = 1000):
    properties = []
    for _ in range(num_records):
        fake_property = Property(
            name=fake.company(),
            address=fake.address(),
            rent=round(random.uniform(500, 5000), 2), 
        )
        properties.append(fake_property)

    # Bulk insert
    db.bulk_save_objects(properties)
    db.commit()
    print(f"{num_records} fake properties inserted into the database.")

# Entry point for the script
if __name__ == "__main__":
    # Create a DB session manually
    from app.db.session import SessionLocal

    db = SessionLocal()  # Create a new session
    try:
        generate_fake_properties(db)  # Pass the session to the function
    finally:
        db.close()  # Always close the session
