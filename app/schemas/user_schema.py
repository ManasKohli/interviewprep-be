from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    google_id: str
    name: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    google_id: str
    name: str

    model_config = {
        "from_attributes": True
    }