from faster_whisper import WhisperModel

whisper_model = WhisperModel(
    "large-v3",
    # Inicializamos el modelo con CUDA
    device="cuda",
    compute_type="float16"
)

class WhisperService:

    def __init__(self):
        self.whisper = whisper_model

    def transcribe(self, temp_path, language="es", beam_size=1):
        
        return self.whisper.transcribe(temp_path, language=language, beam_size=beam_size)