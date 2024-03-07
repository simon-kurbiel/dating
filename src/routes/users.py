from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils, models, schemas

from ..exceptions import exception

router = APIRouter(
    prefix='/users',
    tags= ['Users']
)



@router.post("/signup",status_code=status.HTTP_201_CREATED,response_model=schemas.SignUpResponse)
async def signup(user:schemas.SignUp, db:Session = Depends(get_db)):
    
    ## see if email exists
    
    email_exists = db.query(models.User).filter(models.User.email == user.email).first()
    if(email_exists):
        return exception.HTTPConflictException(msg="Email Already Exists! Please Login")
    
    if(user.password != user.confirm):
        return exception.HTTPBadRequestException(msg="Passwords Do Not Match")
    
    #hashpassword
    user.password = utils.hash(user.password)
    
    new_user = schemas.SignUpIn(**user.dict())
    new_user = models.User(**new_user.dict())
    
    db.add(new_user)
    db.commit()

    return new_user
    
    