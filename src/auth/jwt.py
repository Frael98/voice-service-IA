from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "THISISMYSECRETKEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    """ Crea un Token de acceso

        Args
            - data: Diccionario con los datos 
     """

    to_encode = data.copy()
    
    # Tiempo de expiracion
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Time expiration added to data
    to_encode.update({"exp": expire})
    # JWT data encoded with Secret Key and Algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


