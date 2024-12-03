from getpass import getuser
from fastapi import APIRouter, Depends, HTTPException,status
from app.db import session
from app.schemas.user import UserLogin, Token,UserCreate,UserResponse,UserUpdate
from app.services.auth_service import create_access_token, create_user, get_password_hash, get_user_by_email, verify_password
from app.models.user import User

router = APIRouter()

@router.get("/users",response_model=list[UserResponse])
async def get_all_users(db:session=Depends(session.get_db)):
    users=db.query(User).all()
    return users


@router.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    
    user = await getuser(user_login.email)
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=UserResponse)
async def signup(user_create: UserCreate, db: session = Depends(session.get_db)):
    existing_user = get_user_by_email(db, email=user_create.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed_password = get_password_hash(user_create.password)


    new_user = create_user(db, user_create=user_create, hashed_password=hashed_password)

    return new_user


@router.put("/update/{user_id}", response_model=UserResponse)
async def update_user_details(user_id: int, user_update: UserUpdate, db: session = Depends(session.get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

  
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        user.hashed_password = get_password_hash(user_update.password)
    if user_update.is_active is not None:
        user.is_active = user_update.is_active
    if user_update.is_superuser is not None:
        user.is_superuser = user_update.is_superuser
    
    db.commit()
    db.refresh(user)
    
    return user

@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_account(user_id: int, db: session = Depends(session.get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


