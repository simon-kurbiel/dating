
from fastapi import APIRouter, status, Depends
from ..exceptions import exception
from .. import models, utils, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProfileOut,response_model_exclude_none=True)
async def complete_profile(profile:schemas.Profile, db:Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    
    location = utils.get_location(profile.longitude, profile.latitude)
    if location is None:
        return exception.HTTPBadRequestException(msg="Unknown Address")
    address = location["address"]
    city, county,state, country = (address.get(info) for info in ["city", "county", "state", "country"])
    place = f'{city}, {state}' if city else  f'{county}, {state}'
    filtered_value = {key:value for key, value in profile.dict().items() if value is not None and value != ""}
    
    profile_out = schemas.ProfileOut(**filtered_value, location=place)
    values_in_db = {key : value for key,value in filtered_value.items() if key not in ["longitude", "latitude"]}
    profile_in_db = models.Profile(**values_in_db, location = place,
                                   longitude= profile.longitude, latitude = profile.latitude, user_id = current_user["id"])
    db.add(profile_in_db)
    db.commit()
    print(values_in_db)
    return profile_out
    
   






