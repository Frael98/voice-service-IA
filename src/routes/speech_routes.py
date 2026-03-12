from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from fastapi import HTTPException
from src.routes.models import TextRequest
from src.services import tts_services, whisper_service
import tempfile
import logging

import soundfile as sf
from fastapi.responses import StreamingResponse
import io

""" Inicialización de FastAPI Router """
router = APIRouter(prefix="/v1", tags=["Voice AI"])

""" Inicialización de modelos """
tts_model = tts_services.TTSService()
whisper_model = whisper_service.WhisperService()

""" Logs """
logger = logging.getLogger(__name__)

@router.post("/speech/text-to-voice")
async def text_to_voice(data: TextRequest):
    """ Convierte los textos enviados por el body en formato JSON a voz
        usando TTS

        Args
            data: {
                "text": "Este es un texto de prueba"
            }
    """

    text = data.text
    
    try:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_file = temp_audio.name

            logger.info("Generando texto desde audio")
            tts_model.voice_to_file(
                text=text,
                file_path=temp_audio,
                # language="es"
            )
    
    except Exception as e:
        logger.error(f"Ocurrio un error {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    

    return FileResponse(
        temp_file,
        media_type="audio/wav",
        filename="speech.wav"
    )


@router.post("/transcription/voice-to-text")
async def voice_to_text(file: UploadFile):
    """ Convierte los audios .wav a texto
        
        Args
            - file de tipo UploadFile 
     """

    try:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(await file.read())
            temp_path = temp_audio.name

        logger.info("Transcribiendo voz a texto")
        segments, _ = whisper_model.transcribe(temp_path, language="es", beam_size=1)
        text = " ".join([s.text for s in segments])
    
    except Exception as e:
        logger.error(f"Ocurrio un error {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"text": text}


@router.post("/speech/text-to-voice-streaming")
def text_to_voice_streaming(data: TextRequest):
    """ Genera audio en memoria, baja la latencia """

    # generar audio en memoria
    wav = tts_model.synthesize(
        text=data.text,
        #language="es"
    )

    buffer = io.BytesIO()

    # escribir wav en memoria
    sf.write(buffer, wav, 22050, format="WAV")
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="audio/wav"
    )