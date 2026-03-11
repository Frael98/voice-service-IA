from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWSError
from jwt import ALGORITHM, SECRET_KEY

security = HTTPBearer()

# This function verfy_token use on endpoints - Dependency(very_token)
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """ Verifica si el token de las credenciales es valido 

        Args
            - credentials: Credenciales que se envian mediante HTTP Header

    """
    
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload
    except JWSError:
        raise HTTPException(status_code=401, detail="Invalid token")