# SISDEP - Pruebas Automatizadas

Proyecto de pruebas automatizadas para el sistema SISDEP de la Alcaldía de Medellín utilizando Robot Framework y SeleniumLibrary.

## 🚀 Ejecución con Docker

### Prerrequisitos
- Docker
- Docker Compose

### Ejecución Local con Docker

```bash
# Construir y ejecutar todas las pruebas
docker-compose --profile local up --build

# Ejecutar solo una suite específica
docker run --rm -v $(pwd)/reports:/app/reports sisdep-robot-tests robot --outputdir reports test_suites/features/autenticacion/

# Ejecutar un test case específico
docker run --rm -v $(pwd)/reports:/app/reports sisdep-robot-tests robot --outputdir reports -t "Login Exitoso" test_suites/features/autenticacion/autenticacion_suite.robot
```

### Ejecución en CI/CD

```bash
# Para entornos de CI/CD (sin screenshots)
docker-compose --profile ci up --build
```

### Comandos Docker Útiles

```bash
# Construir imagen
docker build -t sisdep-robot-tests .

# Ejecutar contenedor interactivo
docker run -it --rm sisdep-robot-tests bash

# Ver logs en tiempo real
docker-compose logs -f robot-tests
```

## 📁 Estructura del Proyecto

```
sisdep/
├── config/                 # Configuraciones
├── data/                   # Datos de prueba
├── drivers/               # Drivers de navegador
├── logs/                  # Logs de ejecución
├── page_objects/          # Page Objects
├── reports/               # Reportes generados
├── resources/             # Recursos comunes
├── test_suites/          # Casos de prueba
│   └── features/
│       ├── administracion/
│       ├── autenticacion/
│       ├── regulaciones/
│       └── social/
├── Dockerfile             # Configuración Docker
├── docker-compose.yml     # Orquestación Docker
├── requirements.txt       # Dependencias Python
└── README.md
```

## 🧪 Ejecución Local (Sin Docker)

### Prerrequisitos
- Python 3.8+
- Google Chrome
- ChromeDriver

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Descargar ChromeDriver (Windows)
# Descargar desde: https://chromedriver.chromium.org/
# Colocar en la carpeta drivers/
```

### Comandos de Ejecución

```bash
# Ejecutar todas las pruebas
robot -d reports test_suites/features/

# Ejecutar suite específica
robot -d reports test_suites/features/autenticacion/autenticacion_suite.robot

# Ejecutar test case específico
robot -d reports -t "Login Exitoso" test_suites/features/autenticacion/autenticacion_suite.robot

# Ejecutar por tags
robot -d reports --include autenticacion test_suites/features/
```

## 📊 Reportes

Los reportes se generan en la carpeta `reports/`:
- `report.html` - Reporte principal
- `log.html` - Log detallado
- `output.xml` - Resultados en formato XML
- `screenshots/` - Capturas de pantalla

## 🏷️ Tags Disponibles

- `autenticacion` - Pruebas de login/logout
- `administracion` - Gestión de usuarios, dominios, grupos
- `regulaciones` - Módulos, autorizaciones, visitas
- `social` - Venteros, estudios socioeconómicos, ofertas
- `positivo` - Casos de éxito
- `negativo` - Casos de error
- `funcional` - Pruebas funcionales

## 🔧 Configuración

### Variables de Entorno

```bash
# config/config.robot
${SISDEP_URL}              https://sisdep.medellin.gov.co
${VALID_USERNAME}           tu_usuario
${VALID_PASSWORD}           tu_password
${BROWSER}                  chrome
${IMPLICIT_WAIT}           10s
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

### Administración
- ✅ Gestión de usuarios (CRUD)
- ✅ Gestión de dominios
- ✅ Gestión de grupos y permisos

### Regulaciones
- ✅ Gestión de módulos
- ✅ Gestión de autorizaciones
- ✅ Asignación de visitas

### Social
- ✅ Gestión de venteros
- ✅ Estudio socioeconómico
- ✅ Gestión de ofertas institucionales
- ✅ Gestión de vehículos

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

Para soporte técnico o preguntas sobre el proyecto, contacta al equipo de QA.

---

**Nota**: Este proyecto utiliza Docker para garantizar consistencia entre entornos de desarrollo y CI/CD. Se recomienda usar Docker para ejecutar las pruebas. 