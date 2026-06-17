from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserResponse
)
from app.services.user_service import (
    get_or_create_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def create_user_route(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    return get_or_create_user(
        db=db,
        email=payload.email,
        google_id=payload.google_id,
        name=payload.name
    )
