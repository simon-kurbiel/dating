from passlib.context import CryptContext
from fastapi import UploadFile
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# check that images are valid
def images_are_valid(images:list[UploadFile]):
    message = {"success":True}
    for image in images:
        if image.size > 200_000 or image.content_type.startswith("image") == False:
            message = {"success": False}
        
        
    return message
    
