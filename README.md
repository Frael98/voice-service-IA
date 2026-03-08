# AI Speech Service

Instalar CUDA toolkit, solo funciona con la 12 el Faster-Whisper
    [CUDA Toolkit 12.4 Downloads](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)


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
