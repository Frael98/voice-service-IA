from fastapi import FastAPI
from routes import speech_routes
from auth import login

app = FastAPI(title="Voice AI API", 
        #docs_url=None,        # desactiva Swagger
        #redoc_url="/docs"     # usa ReDoc
    )

@app.get("/")
def home():
    """ Ruta de Salud! """
    return {"message": "AI voice API running"}

""" Agregamos las rutas """
app.include_router(login.router)
app.include_router(speech_routes.router)