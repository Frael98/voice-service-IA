from TTS.api import TTS

# tts_model_cuda = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
tts_model_cuda = ''
tts_model = TTS(model_name="tts_models/es/css10/vits")

class TTSService:

    def __init__(self, isCuda = False):
        self.isCuda = isCuda

        if isCuda:
            self.tts = tts_model_cuda
        else: 
            self.tts = tts_model

    def synthesize(self, text: str, language: str = "es"):
        
        if self.isCuda:
            return self.tts.tts(text=text, language=language)
        
        return self.tts.tts(text=text)
    
    def voice_to_file(self, text: str, file_path: str, language: str ="es"):
        
        if self.isCuda:
            return self.tts.tts_to_file(text=text, file_path=file_path, language=language)
        
        return self.tts.tts_to_file(text=text, file_path=file_path)