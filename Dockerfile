# Usar imagen base de Python
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    xvfb \
    curl \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# --- CORRECCIÓN FINAL ---
# Definimos las variables para las versiones de Chrome
# La versión del paquete .deb a veces incluye un "-1" al final
ENV CHROME_VERSION="127.0.6533.72"
ENV CHROME_DEB_VERSION="127.0.6533.72-1"

# Descargar el paquete .deb directamente e instalarlo con apt
# Esto es más seguro que buscar en el repositorio
RUN wget -q "https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_DEB_VERSION}_amd64.deb" \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_${CHROME_DEB_VERSION}_amd64.deb --no-install-recommends \
    && rm google-chrome-stable_${CHROME_DEB_VERSION}_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Descargar el ChromeDriver que corresponde a la versión de Chrome
# Esta parte ya estaba bien
RUN wget -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip /tmp/chromedriver.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/ \
    && rm -rf /tmp/chromedriver.zip /tmp/chromedriver-linux64 \
    && chmod +x /usr/local/bin/chromedriver

# Crear directorio para reportes
RUN mkdir -p reports

# Variables de entorno para Chrome
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROMEDRIVER_PATH=/usr/local/bin/chromedriver

# Comando por defecto
CMD ["robot", "-d", "reports", "test_suites/features/"]