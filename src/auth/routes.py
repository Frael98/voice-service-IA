from fastapi import APIRouter, HTTPException
from auth.models import LoginRequest
from auth.jwt import create_access_token

router = APIRouter(prefix="/v1", tags=["Authentication"])

@router.post("/auth/login")
def login(data: LoginRequest):
    """  Endpoint para iniciar sesión en la API

        Args
            - data: LoginRequest
    """
    
    if data.username != "admin" or data.password != "123456":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/auth/logout")
def logout():

    pass