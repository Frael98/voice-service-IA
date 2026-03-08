from fastapi import APIRouter, UploadFile
from routes.models import TextRequest
from fastapi.responses import FileResponse
from faster_whisper import WhisperModel
import tempfile

router = APIRouter()
model = WhisperModel(
    "large-v3",
    # Inicializamos el modelo con CUDA
    device="cuda",
    compute_type="float16"
)

@router.post("/text-to-speech")
def text_to_speech(data: TextRequest):
    
    text = data.text

    return text

@router.get("/speech-to-text")
def speech_to_text():

    return {"message": "Testing..."}

@router.post("/voice-to-text")
async def voice_to_text(file: UploadFile):
    """ Convierte los audios .wav a texto
        Args:
            - file de tipo UploadFile 
     """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(await file.read())
        temp_path = temp_audio.name

    segments, _ = model.transcribe(temp_path, language="es", beam_size=1)
    text = " ".join([s.text for s in segments])

    return {"text": text}