# Usar imagen base de Python
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    xvfb \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome (versión específica)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable=138.0.7204.168-1 \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Descargar ChromeDriver compatible con Chrome 138
RUN wget -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/138.0.7204.168/linux64/chromedriver-linux64.zip" \
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

# Comando por defecto (sin headless)
CMD ["robot", "-d", "reports", "test_suites/features/"] 