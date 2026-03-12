## Tests
Para tu API de voz con FastAPI (Whisper + TTS + JWT), las pruebas unitarias normalmente se hacen con:

pytest → framework de testing
httpx / TestClient → para probar endpoints
mocking → para no ejecutar modelos pesados (Whisper/TTS)

    📌 Nota: Necesario poner el archivo __init__.py en todos los modulos para usar pytest
    📌 Nota: si los imports cambiaron de "auth.routes" a "src.auth.routes" ejecutar y correr la API desde el directorio raíz indicando 
    

## Errores

- RuntimeError: cuBLAS failed with status CUBLAS_STATUS_NOT_SUPPORTED

**Solución**:

- No usar:
    compute_type="int8",
    compute_type="int8_float16",
    compute_type="int8_float32",

    Porque en muchas GPUs nuevas provoca exactamente:

    CUBLAS_STATUS_NOT_SUPPORTED

    ```PYTHON
    model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16"
    )
    ```
"# voice-service-IA" 