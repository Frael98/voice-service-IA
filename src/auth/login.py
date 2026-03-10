from fastapi import APIRouter
from auth.models import LoginRequest
from auth.jwt import create_access_token

router = APIRouter()

def login(data: LoginRequest):
    
    if data.username != "admin" or data.password != "123456":
        return {"error": "invalid credentials"}
    
    token = create_access_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }