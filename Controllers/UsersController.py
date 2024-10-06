from .BaseController import BaseController
from sqlalchemy.orm import Session
from models.models import User
from schemas.UsersSchema import UserCreate
from database.db import get_db
from fastapi import Depends
class UsersController(BaseController):
    def __init__(self):
        super().__init__()

    async def get_user_by_email(self, db: Session, email: str):
        # Implement get user by email logic here
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            return None
        
        return user
    
    async def get_user_by_id(self, db: Session, user_id: int):
        # Implement get user by id logic here
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            return None
        
        return user
    
    
    async def create_user(self, user_create_info: UserCreate, 
                          db: Session = Depends(get_db)):
        # Logic to create a new user
        from Controllers.AuthController import AuthController
        hashed_password: str = AuthController().hash_password(user_create_info.password)
        print(f"hashed_password = {hashed_password}")
        print(f"user_create_info.email = {user_create_info.email}")
        new_user = User(email=user_create_info.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        

    def update_user(self, user_id, user_data):
        # Logic to update an existing user
        pass

    def delete_user(self, user_id):
        # Logic to delete a user
        pass