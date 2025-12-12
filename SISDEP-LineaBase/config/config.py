"""
Configuración del proyecto SISDEP - Playwright
Equivalente a config/config.robot
"""

# URLs de la aplicación SISDEP
BASE_URL = "https://base.innovacion.it.com/sisdep"
SISDEP_URL = BASE_URL
LOGIN_URL = SISDEP_URL
SECURE_AREA_URL = SISDEP_URL

# Configuración del navegador
BROWSER = "chromium"  # chromium, firefox, webkit
BROWSER_HEADLESS = False
IMPLICIT_WAIT = 10000  # en milisegundos
EXPLICIT_WAIT = 30000  # en milisegundos
PAGE_LOAD_TIMEOUT = 60000  # en milisegundos

# Credenciales de prueba SISDEP
VALID_USERNAME = "admin"
VALID_PASSWORD = "prueba123"
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "invalid_password"

# Rutas de archivos
REPORTS_PATH = "reports"
SCREENSHOT_DIR = f"{REPORTS_PATH}/screenshots"
LOGS_PATH = "logs"
DATA_PATH = "data"

# Configuración de reportes
LOG_LEVEL = "INFO"

