
from setuptools import setup, find_packages
import os

#Checking PulseAudio is installed or not
try:
    os.system("paplay --version")
    os.system("parecord --version")
except:
    print("Please install PulseAudio first.")
    exit()


setup(
    name="paudio",
    version="0.3.0",
    description="A Python wrapper for paplay and parecord to play and record audio using PulseAudio.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="afrhan-repo",
    author_email="afrhanhossain11@gmail.com",
    url="https://github.com/afrhan-repo/pAudio",  # Add your GitHub URL here
    packages=find_packages(),  # Automatically find and include packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
