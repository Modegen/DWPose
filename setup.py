from setuptools import setup
import os

# Run shell command to install system dependencies

setup(
    name='dwpose',
    version='0.0.9b',
    install_requires=[
        'huggingface_hub==0.20.1',
        'matplotlib==3.6.2',
        'numpy==1.24.3',
        'onnxruntime', #==1.13.1',
        'onnxruntime_gpu', #==1.13.1',
        'opencv_python==4.7.0.68',
        'Pillow==10.2.0',
        'scikit_image==0.19.3',
        'scipy', #==1.11.4',
        'torch==2.1.1+cu118',
    ],
)
