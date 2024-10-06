from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr = None

    class Config:
        from_attributes = True
        
        
class UserCreate(BaseModel):
    email: EmailStr = None
    password: str

    class Config:
        from_attributes = True
        
        
class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True
        
