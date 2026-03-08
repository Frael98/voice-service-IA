import ctranslate2
import os
import nvidia.cublas

print(ctranslate2.get_supported_compute_types("cuda"))

print(nvidia.cublas.__file__)