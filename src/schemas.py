from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Body

class SignUp(BaseModel):
    first : Annotated[str, Body(min_length=2)]
    last : Annotated[str, Body(min_length=2)]
    email : EmailStr
    password: Annotated[str, Body(min_length=6)]
    confirm: Annotated[str, Body(min_length=6)]
  
    
class SignUpIn(BaseModel):
    first : Annotated[str, Body(min_length=2)]
    last : Annotated[str, Body(min_length=2)]
    email: EmailStr
    password : str
    
    
    
    
class SignUpResponse(BaseModel):
    
    email : EmailStr
    
class TokenData(BaseModel):
    id : int | None = None
    
class Token(BaseModel):
    access_token:str
    token_type : str
    
    
# Images

class Image(BaseModel):
    url : str
    user_id : int
    
    
    
# Profile

class ProfileBase(BaseModel):
    bio : str | None = None
    college : str | None = None
    occupation : str | None = None
    looking_for : str | None = None
    
class Profile(ProfileBase):
    longitude : float
    latitude : float
    
    
class ProfileOut(ProfileBase):
    location : str
    

class ProfileIn(Profile):
    location:str
    user_id: int
    
    
    
    
    
