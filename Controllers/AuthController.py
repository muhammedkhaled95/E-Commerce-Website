from .BaseController import BaseController
from sqlalchemy.orm import Session
from schemas import UsersSchema, AuthSchema
from typing import Any, Union
from datetime import datetime, timedelta, timezone
from core.config import settings
from jose import jwt
from fastapi import Depends
from models.models import User
from passlib.context import CryptContext

class AuthController(BaseController):
    def __init__(self):
        super().__init__()
        # Creates a CryptContext object for handling password hashing and verification using the pbkdf2_sha256 algorithm.
        self.pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

    async def is_user_authenticated(self, db: Session, email: str, password: str):
        # Implement authentication logic here
        from Controllers.UsersController import UsersController
        user = await UsersController().get_user_by_email(db, email)
        
        if not user:
            return None
        
        if not self.verify_password(password, user.password):
            return None
        
        return user
    
    
    def create_access_token(subject: Union[int, Any], expires_delta: timedelta = None):
        if expires_delta:
            print(f"type of expires_delta = {type(expires_delta)}")
            print(f"type of timezone = {datetime.now(timezone.utc)}")
            expire = datetime.now(timezone.utc) + timedelta(expires_delta)
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=float(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
            
        to_encode = {"exp": expire, "sub": str(subject)}
        
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        return encoded_jwt
            
        
    async def verify_password(self, plain_password, hashed_password) -> bool:
        # Implement password verification logic here
        return self.pwd_context.verify(plain_password, hashed_password)
        
    
    def hash_password(self, password) -> str:
        # Implement password hashing logic here
        hashed_password = self.pwd_context.hash(password)
        return hashed_password

    def logout(self):
        # Implement logout logic here
        pass

    def register(self, username, password, email):
        # Implement registration logic here
        pass