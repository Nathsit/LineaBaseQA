# SISDEP - Pruebas Automatizadas con Playwright

Proyecto de pruebas automatizadas para el sistema SISDEP de la Alcaldía de Medellín utilizando Playwright y Python.

## 🚀 Ejecución con Docker

### Prerrequisitos
- Docker
- Docker Compose

### Ejecución Local con Docker

```bash
# Construir y ejecutar todas las pruebas de autenticación
docker-compose --profile local up --build

# Ejecutar solo una suite específica
docker run --rm -v $(pwd)/reports:/app/reports sisdep-playwright-tests pytest -v tests/features/autenticacion/

# Ejecutar un test case específico
docker run --rm -v $(pwd)/reports:/app/reports sisdep-playwright-tests pytest -v tests/features/autenticacion/test_login_exitoso.py::test_inicio_de_sesion_exitoso_con_credenciales_validas
```

### Ejecución en CI/CD

```bash
# Para entornos de CI/CD (sin screenshots)
docker-compose --profile ci up --build
```

### Comandos Docker Útiles

```bash
# Construir imagen
docker build -t sisdep-playwright-tests .

# Ejecutar contenedor interactivo
docker run -it --rm sisdep-playwright-tests bash

# Ver logs en tiempo real
docker-compose logs -f playwright-tests
```

## 📁 Estructura del Proyecto

```
SISDEP-LineaBase/
├── config/                 # Configuraciones
│   └── config.py
├── data/                   # Datos de prueba
│   └── test_data.py
├── page_objects/          # Page Objects
│   ├── login_page.py
│   └── dashboard_page.py
├── utils/                 # Utilidades comunes
│   └── common_helpers.py
├── tests/                 # Casos de prueba
│   └── features/
│       └── autenticacion/
│           ├── test_login_exitoso.py
│           ├── test_login_credenciales_invalidas.py
│           ├── test_logout.py
│           └── test_autenticacion_suite.py
├── Dockerfile             # Configuración Docker
├── docker-compose.yml     # Orquestación Docker
├── requirements.txt       # Dependencias Python
├── pytest.ini            # Configuración pytest
├── conftest.py           # Fixtures de pytest
└── README.md
```

## 🧪 Ejecución Local (Sin Docker)

### Prerrequisitos
- Python 3.8+
- Playwright

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Instalar navegadores de Playwright
playwright install chromium
```

### Comandos de Ejecución

```bash
# Ejecutar todas las pruebas
pytest -v

# Ejecutar suite específica
pytest -v tests/features/autenticacion/

# Ejecutar test case específico
pytest -v tests/features/autenticacion/test_login_exitoso.py::test_inicio_de_sesion_exitoso_con_credenciales_validas

# Ejecutar por tags/markers
pytest -v -m "smoke and autenticacion"
pytest -v -m "login and negativo"
pytest -v -m "funcional"

# Ejecutar con reporte HTML
pytest -v --html=reports/report.html --self-contained-html
```

## 📊 Reportes

Los reportes se generan en la carpeta `reports/`:
- `report.html` - Reporte principal HTML
- `screenshots/` - Capturas de pantalla

## 🏷️ Markers Disponibles (Tags)

- `@pytest.mark.autenticacion` - Pruebas de login/logout
- `@pytest.mark.administracion` - Gestión de usuarios, dominios, grupos
- `@pytest.mark.positivo` - Casos de éxito
- `@pytest.mark.negativo` - Casos de error
- `@pytest.mark.smoke` - Pruebas críticas
- `@pytest.mark.funcional` - Pruebas funcionales
- `@pytest.mark.regression` - Pruebas de regresión

## 🔧 Configuración

### Variables de Entorno

```python
# config/config.py
SISDEP_URL = "https://www.medellin.gov.co/sisdep"
VALID_USERNAME = "admin"
VALID_PASSWORD = "tu_password"
BROWSER = "chromium"  # chromium, firefox, webkit
BROWSER_HEADLESS = False
```

## 🚀 CI/CD

### Azure DevOps
Configuración de pipeline para ejecutar pruebas en contenedores Docker.

## 📝 Casos de Prueba Implementados

### Autenticación
- ✅ Login exitoso
- ✅ Login con credenciales inválidas
- ✅ Logout
- ✅ Usuario inactivo

## 🔄 Migración desde Robot Framework

Este proyecto es una migración del proyecto original de Robot Framework a Playwright. Se mantiene la misma estructura de carpetas y lógica de negocio.

### Equivalencias

| Robot Framework | Playwright |
|----------------|------------|
| `*** Settings ***` | `conftest.py` + `pytest.ini` |
| `*** Variables ***` | `config.py` o `test_data.py` |
| `*** Keywords ***` | Funciones en `common_helpers.py` |
| `*** Test Cases ***` | Funciones `test_*.py` |
| `[Tags]` | `@pytest.mark.tag_name` |
| `[Setup]` / `[Teardown]` | `@pytest.fixture` |
| Page Objects `.robot` | Clases Python |

## 📚 Documentación Adicional

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)

