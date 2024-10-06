from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import timedelta
from core.config import settings
from models.models import User
from typing import Annotated
from database.db import get_db
from Controllers import AuthController, UsersController
from schemas import UsersSchema, AuthSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

auth_router = APIRouter(prefix="", tags=["User Authentication"])

auth_controller = AuthController()
users_controller = UsersController()

@auth_router.post("/login", response_model=AuthSchema.AccessTokenResponse)
async def user_login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = await auth_controller.is_user_authenticated(db, email=user_credentials.username, password=user_credentials.password)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    
    access_token = auth_controller.create_access_token(user.id)
    
    return {"access_token": access_token, "token_type": "bearer"}



@auth_router.post("/register")
async def create_user(*, db: Session = Depends(get_db), 
                      user_register: UsersSchema.UserCreate):
    # if the user alread exists, redirect the user to the login endpoint.
    user = await users_controller.get_user_by_email(db, email=user_register.email)
    
    if user:
        return RedirectResponse(url="/login", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    
    # create the user
    await users_controller.create_user(user_register, db)
    return {"message": "User created successfully"}

"""
@auth_router.post("/reset_password_request")
async def reset_password_request(*, db: Session = Depends(get_db), reset_email: schemas.PasswordResetRequest):
    user = await crud.get_user_by_email(db, email=reset_email.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    reset_token = security.create_reset_token(reset_email.email)
    return {"reset_token": reset_token}


@auth_router.post("/reset_password")
async def reset_password(*, db: Session = Depends(get_db), reset_token_and_password: schemas.ResetTokenAndPassword):
    email = security.verify_reset_token(reset_token_and_password.reset_token)
    print(f"email = {email}")
    if not email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
    user = await crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    new_password_hash = security.get_password_hash(reset_token_and_password.new_password)
    user.hashed_password = new_password_hash
    db.commit()
    return {"message": "Password updated successfully"}

"""
