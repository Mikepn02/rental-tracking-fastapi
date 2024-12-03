from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt



def verify_password(plain_password , hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_email(db: Session,email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_create: UserCreate, hashed_password: str):
    db_user = User(email=user_create.email, hashed_password= hashed_password, is_active=user_create.is_active, is_superuser=user_create.is_superuser)
    db.add(db_user)
    db.commit()
    db.refresh()
    return db.user



def update_user(db: Session, user_id: int, user_update: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if user_update.email:
            user.email = user_update.email
        if user_update.is_active is not None:
            user.is_active = user_update.is_active
        if user_update.is_superuser is not None:
            user.is_superuser = user_update.is_superuser

        db.commit()
        db.refresh()

    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit
    