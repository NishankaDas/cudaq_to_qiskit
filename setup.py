from setuptools import setup, find_packages

setup(
    name="cudaq_to_qiskit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "qiskit",
    ],
    author="Your Name",
    description="A library to convert CUDA-Q programs to Qiskit.",
    url="https://github.com/yourusername/cudaq_to_qiskit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
