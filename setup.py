from setuptools import setup
import os
import sys

# Check if CUDA is available
try:
    import torch
    cuda_available = torch.cuda.is_available()
except ImportError:
    cuda_available = False

# Run shell command to install system dependencies

setup(
    name='dwpose',
    version='0.0.9b',
    install_requires=[
        'huggingface_hub',#==0.20.1',
        'matplotlib',#==3.6.2',
        'numpy',#==1.24.3',
        'onnxruntime',#==1.13.1',
        'onnxruntime_gpu' if cuda_available,
        'opencv_python',#==4.7.0.68',
        'Pillow',#==10.2.0',
        'scikit_image',#==0.19.3',
        'scipy',#==1.11.4',
        'torch',#==2.1.1+cu118',
    ],
)
