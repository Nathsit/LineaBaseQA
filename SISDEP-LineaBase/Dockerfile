# Dockerfile para ejecutar pruebas con Playwright
# Equivalente al Dockerfile del proyecto Robot Framework

FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar navegadores de Playwright
RUN playwright install chromium
RUN playwright install-deps chromium

# Copiar el código del proyecto
COPY . .

# Crear directorios necesarios
RUN mkdir -p reports screenshots logs

# Comando por defecto (puede ser sobrescrito)
CMD ["pytest", "-v", "--html=reports/report.html", "--self-contained-html"]

