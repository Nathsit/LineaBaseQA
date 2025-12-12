"""
Setup file para el proyecto SISDEP - Playwright
"""
from setuptools import setup, find_packages

setup(
    name="sisdep-playwright",
    version="1.0.0",
    description="Pruebas automatizadas para SISDEP usando Playwright",
    packages=find_packages(),
    install_requires=[
        "playwright==1.40.0",
        "pytest==7.4.3",
        "pytest-html==4.1.1",
        "pytest-playwright==0.4.3",
        "pytest-xdist==3.5.0",
        "python-dotenv==1.0.0",
    ],
    python_requires=">=3.8",
)

