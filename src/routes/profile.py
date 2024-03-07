
from fastapi import APIRouter
from ..exceptions import exception
from .. import models, utils, schemas
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix="Profile",
    tags=["Profile"]
)
