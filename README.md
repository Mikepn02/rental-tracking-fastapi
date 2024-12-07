# Freelance Management System


The Rental Management System isapplication designed to streamline property and lease management for landlords, property managers, and tenants. It enables users to manage properties, track rental properties, create and maintain lease agreements, and monitor payments. The system includes features such as secure user authentication, property listing management, tenant registration, lease agreement tracking Built with robust backend and frontend technologies, it ensures scalability, security, and ease of use.

## Features

- User Authentication: Secure login and registration for landlords, tenants, and property managers.
- Property Management: Create, update, and manage property listings.
- Rental Property Tracking: Track which properties are available for rent and those currently leased.
- Lease Agreement Management: Create, update, and track lease agreements, including start and end dates, and terms.
- Tenant Management: Register and manage tenant profiles.


#### Tech Stack

-  Backend: FastAPI
-  Database: PostgreSQL
-  Authentication: JWT (JSON Web Token)
-  ORM: SQLAlchemy
-  Password Hashing: Passlib
-  Environment Variables: python-dotenv

### Installation

Follow these steps to set up the project locally:

#### Prerequisites

1. Python 3.7 or above
2. PostgreSQL Database (Instructions for setting up a PostgreSQL database can be found here: [link to PostgreSQL documentation])

#### Setup

Clone the repository:

```shell
https://github.com/BertinKimberly/fms_fastapi.git

cd fms_fastapi

```

install dependencies

```shell
pip install -r requirements.txt
```

#### Set up the PostgreSQL database:

-  Create a new database in PostgreSQL.

-  Add the database URL to your `.env` file:

```js
DATABASE_URL=postgresql://user:password@localhost/dbname
```

#### run migrations

```shell
 alembic init migrations
```

#### Run the application

Use uvicorn

```shell
 uvicorn app.main:app --reload
```

for tseting, navigate to `/docs` or `/redoc`