from fastapi import FastAPI
from routes import speech_routes

app = FastAPI(title="Voice AI API")

@app.get("/")
def home():
    """ Ruta de Salud! """
    return {"message": "AI voice API running"}

""" Agregamos las rytas """
app.include_router(speech_routes.router)