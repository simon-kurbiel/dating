from fastapi import APIRouter, Depends, UploadFile, Body
from ..database import get_db
from sqlalchemy.orm import Session
from typing import Annotated
import os
from ..exceptions import exception
from ..config import settings
import boto3
from .. import utils, models, schemas, oauth2

router = APIRouter(
    prefix= '/images',
    tags = ['images']
)



@router.post("/complete")
async def complete_images(images:list[UploadFile] = None, db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    
 
    
    message = utils.images_are_valid(images=images)
    if message["success"] == False:
        return exception.HTTPBadRequestException(msg="Must be a valid image and less than 200,000")
   
    images_to_s3 = [(image.file,f'images/{current_user["id"]}_{image.filename}' ) for image in images]
    
    try:
        for image in images:
            
            s3 = boto3.resource("s3")
            bucket =s3.Bucket(settings.BUCKET_NAME)
            image_name = f'images/{current_user["id"]}_{image.filename}'
            bucket.upload_fileobj(image.file,image_name)
            
            image_url= f'https://{settings.BUCKET_NAME}.s3.amazonaws.com/{image_name}'
            
            new_image = schemas.Image(user_id=current_user["id"],url=image_url)
            new_image = models.Images(**new_image.dict())
            db.add(new_image)
            db.commit()
    
        
        

        
    except Exception as e:
        print(e)
        return exception.HTTPBadRequestException(msg="Error happened")
    
    return "Uplaoded Image"
        
    
    
    # Upload to s3


@router.get("/complete/{id}")
async def images_complete(id:int,db:Session = Depends(get_db)):
    
    num_images = db.query(models.Images).filter(models.Images.user_id == id).count()
    
    if num_images == 3:
        return {"success" : True, "hits": num_images}
    
    return {"success" : False, "hits": num_images}

    