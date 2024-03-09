from passlib.context import CryptContext
from fastapi import UploadFile
from geopy.geocoders import Nominatim
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


# get city and country
def get_location(long:float, lat:float):
    concat_lat_long = f'{lat}, {long}'
    geolocator = Nominatim(user_agent="dating_app")
    location = geolocator.reverse(concat_lat_long, exactly_one=True)
    return location.raw



    
    
    
    
