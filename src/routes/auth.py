from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from .. import schemas, models
from .. import utils
from .. import oauth2

from ..exceptions import exception
router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.post('/login',response_model=schemas.Token,status_code=status.HTTP_200_OK)
async def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        return exception.HTTPUnauthenticatedException(msg= "Not Authenticated")

    if not utils.verify(user_credentials.password, user.password):
        return exception.HTTPUnauthenticatedException(msg= "Not Authenticated")
     
     ##create a token
     
    access_token = oauth2.create_access_token(data={"user_id":user.id})
     
     ##return a token
    return {"access_token": access_token, "token_type" : "bearer"}