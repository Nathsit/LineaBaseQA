# 🏛️ SISDEP - Sistema de Pruebas Automatizadas

## 📋 Descripción del Proyecto

Este proyecto contiene las pruebas automatizadas para el **Sistema SISDEP** de la Alcaldía de Medellín. Las pruebas están desarrolladas usando **Robot Framework** con **Selenium** para automatización web, siguiendo las mejores prácticas de código limpio y organización por features.

## 🎯 Objetivo

Automatizar las pruebas funcionales del sistema SISDEP para garantizar la calidad del software y facilitar la detección temprana de errores en el proceso de desarrollo.

## 🏗️ Estructura del Proyecto

```
sisdep/
├── README.md                           # Este archivo - Documentación principal
├── config/                             # Configuraciones globales
│   └── config.robot                    # Variables y configuraciones del proyecto
├── resources/                          # Recursos reutilizables
│   └── common_keywords.robot           # Keywords comunes para todos los tests
├── page_objects/                       # Page Object Model
│   ├── sisdep_login_page.robot         # Page Object para login
│   └── sisdep_dashboard_page.robot     # Page Object para dashboard
├── data/                               # Datos de prueba
│   └── sisdep_test_data.robot          # Datos específicos de SISDEP
├── test_suites/                        # Casos de prueba organizados por features
│   └── features/                       # Features del sistema
│       └── autenticacion/              # Feature: Autenticación de Usuario
│           ├── README.md               # Documentación específica de la feature
│           ├── autenticacion_suite.robot    # Suite principal de autenticación
│           ├── login_exitoso.robot     # Test de login exitoso
│           ├── login_credenciales_invalidas.robot  # Tests de credenciales inválidas
│           └── logout.robot            # Test de cierre de sesión
├── reports/                            # Reportes de ejecución
│   ├── report.html                     # Reporte principal
│   ├── log.html                        # Log detallado
│   ├── output.xml                      # Salida en XML
│   └── screenshots/                    # Capturas de pantalla
├── drivers/                            # Drivers de navegadores
│   └── chromedriver.exe                # Driver de Chrome
└── logs/                               # Logs de ejecución
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.7 o superior
- Chrome Browser
- Git

### Instalación de Dependencias
```bash
pip install robotframework
pip install robotframework-seleniumlibrary
pip install robotframework-requests
```

### Configuración1Clona el repositorio
2. Navega al directorio del proyecto: `cd sisdep`
3. Verifica que el chromedriver esté en la carpeta `drivers/`
4. Actualiza las credenciales en `config/config.robot`

## 🧪 Ejecución de Pruebas

### Comandos Principales

#### Ejecutar todas las pruebas
```bash
robot -d reports test_suites/
```

#### Ejecutar una feature específica
```bash
# Feature de autenticación completa
robot -d reports test_suites/features/autenticacion/autenticacion_suite.robot

# Solo tests de login
robot -d reports test_suites/features/autenticacion/login_exitoso.robot
```

#### Ejecutar por tags
```bash
# Solo smoke tests
robot -d reports --include smoke test_suites/

# Solo tests negativos
robot -d reports --include negativo test_suites/

# Solo tests de autenticación
robot -d reports --include autenticacion test_suites/
```

#### Ejecutar tests específicos
```bash
# Test específico por nombre
robot -d reports --testInicio De Sesion Exitoso" test_suites/

# Excluir tests específicos
robot -d reports --excluderegression" test_suites/
```

## 📊 Reportes

Después de la ejecución, los reportes se generan en la carpeta `reports/`:

- **report.html**: Reporte visual con resumen de resultados
- **log.html**: Log detallado paso a paso
- **output.xml**: Salida en formato XML (útil para CI/CD)
- **screenshots/**: Capturas de pantalla de cada test

## 🏷️ Sistema de Tags

### Tags por Tipo de Test
- `smoke`: Tests críticos que deben pasar siempre
- `funcional`: Tests funcionales completos
- `regression`: Tests de regresión
- `positivo`: Tests con casos exitosos
- `negativo`: Tests con casos de error

### Tags por Feature
- `autenticacion`: Tests de autenticación
- `login`: Tests específicos de login
- `logout`: Tests específicos de logout

### Tags por Prioridad
- `alta`: Tests de alta prioridad
- `media`: Tests de prioridad media
- `baja`: Tests de prioridad baja

## 🔧 Configuración de Entornos

### Variables de Entorno
Las configuraciones principales están en `config/config.robot`:

```robot
${BASE_URL}                    https://www.medellin.gov.co
${SISDEP_URL}                  ${BASE_URL}/sisdep/
${BROWSER}                     Chrome
${VALID_USERNAME}              admin
${VALID_PASSWORD}              EspacioPublico2024ep
```

### Configuración de Navegador
- **Browser**: Chrome (configurable)
- **Headless**: False (configurable)
- **Timeouts**: Configurables por escenario
- **Screenshots**: Automáticas en cada test

## 📚 Features Implementadas

### ✅ Feature: Autenticación de Usuario
- **Escenarios cubiertos**:
  - Inicio de sesión exitoso
  - Inicio de sesión con credenciales incorrectas
  - Cierre de sesión
- **Archivos**: `test_suites/features/autenticacion/`
- **Documentación**:README de Autenticación](test_suites/features/autenticacion/README.md)

### 🔄 Próximas Features (Pendientes)
- Gestión de Usuarios
- Reportes y Consultas
- Configuración del Sistema
- Administración de Datos

## 🛠️ Mantenimiento

### Agregar Nueva Feature
1. Crear carpeta en `test_suites/features/nueva_feature/`
2. Crear Page Objects necesarios en `page_objects/`3ar datos de prueba en `data/`
4. Crear README específico
5. Actualizar este README general

### Actualizar Locators
Los locators están centralizados en los Page Objects:
- `page_objects/sisdep_login_page.robot`
- `page_objects/sisdep_dashboard_page.robot`

### Agregar Keywords Comunes
Nuevos keywords reutilizables van en `resources/common_keywords.robot`

## 🤝 Contribución

### Estándares de Código
- Usar Page Object Model
- Keywords descriptivos en español
- Documentación en cada test
- Tags apropiados para clasificación
- Capturas de pantalla como evidencia

### Flujo de Trabajo
1. Crear branch para nueva feature
2. Desarrollar tests siguiendo la estructura
3. Ejecutar pruebas localmente
4. Crear Pull Request
5. Revisión y merge

## 📞 Soporte

Para dudas o problemas:
- Revisar la documentación específica de cada feature
- Consultar los logs en `reports/log.html`
- Verificar la configuración en `config/config.robot`

## 📝 Notas Importantes

- **Credenciales**: Actualizar en `config/config.robot` según el entorno
- **Drivers**: Mantener actualizado el chromedriver
- **Locators**: Actualizar cuando cambie la interfaz de usuario
- **Backup**: Hacer backup de reportes importantes antes de nuevas ejecuciones

---

**Desarrollado para la Alcaldía de Medellín** 🏛️  
**Sistema SISDEP - Pruebas Automatizadas** 🧪 