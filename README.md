# 🏛️ SISDEP - Pruebas Automatizadas

## 📋 Descripción

Este repositorio contiene las pruebas automatizadas para el **Sistema SISDEP** de la Alcaldía de Medellín, desarrolladas con **Robot Framework** y **SeleniumLibrary** bajo el patrón Page Object Model (POM). El objetivo es garantizar la calidad funcional del sistema y facilitar la integración continua.

---

## 🏗️ Estructura del Proyecto

```
sisdep/
├── README.md
├── config/
│   └── config.robot
├── data/
│   └── sisdep_test_data.robot
├── drivers/
│   ├── chromedriver.exe
│   └── geckodriver.exe
├── logs/
├── page_objects/
│   ├── sisdep_autorizaciones_page.robot
│   ├── sisdep_dashboard_page.robot
│   ├── sisdep_dominios_page.robot
│   ├── sisdep_grupos_page.robot
│   ├── sisdep_login_page.robot
│   ├── sisdep_modulos_page.robot
│   ├── sisdep_usuarios_page.robot
│   ├── sisdep_visitas_page.robot
│   ├── sisdep_venteros_page.robot
│   ├── sisdep_estudio_socioeconomico_page.robot
│   ├── sisdep_ofertas_institucionales_page.robot
│   └── sisdep_vehiculos_page.robot
├── reports/
│   ├── report.html
│   ├── log.html
│   ├── output.xml
│   └── screenshots/
├── resources/
│   └── common_keywords.robot
├── test_suites/
│   └── features/
│       ├── administracion/
│       │   ├── gestion_dominios.robot
│       │   ├── gestion_grupos_permisos.robot
│       │   ├── gestion_usuarios.robot
│       │   └── README.md
│       ├── autenticacion/
│       │   ├── autenticacion_suite.robot
│       │   ├── login_credenciales_invalidas/
│       │   │   └── login_credenciales_invalidas.robot
│       │   ├── login_exitoso/
│       │   │   └── login_exitoso.robot
│       │   ├── logout/
│       │   │   └── logout.robot
│       │   └── README.md
│       ├── regulaciones/
│       │   ├── asignacion_visitas.robot
│       │   ├── gestion_autorizaciones.robot
│       │   ├── gestion_modulos.robot
│       │   └── README.md
│       └── social/
│           ├── gestion_venteros.robot
│           ├── estudio_socioeconomico.robot
│           ├── gestion_ofertas_institucionales.robot
│           ├── gestion_vehiculos.robot
│           └── README.md
├── .github/
│   └── workflows/
│       └── robot-tests.yml
├── azure-pipelines.yml
└── .gitignore
```

---

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.7+
- Google Chrome (última versión)
- ChromeDriver compatible
- Git

### Instalación de dependencias

```sh
pip install robotframework robotframework-seleniumlibrary robotframework-pabot
```

### Configuración inicial

1. Clona el repositorio y entra al directorio:
   ```sh
   git clone <url>
   cd sisdep
   ```
2. Verifica que el driver de Chrome esté en la carpeta `drivers/` (o usa el workflow de CI).
3. Actualiza las credenciales y variables en `config/config.robot`.

---

## 🧪 Ejecución de Pruebas

### Ejecutar todos los features (incluyendo solo autenticacion_suite)

```sh
robot -d reports test_suites/features/administracion/ test_suites/features/regulaciones/ test_suites/features/social/ test_suites/features/autenticacion/autenticacion_suite.robot
```

### Ejecutar una feature específica

```sh
robot -d reports test_suites/features/regulaciones/gestion_modulos.robot
```

### Ejecutar por tags

```sh
robot -d reports --include smoke test_suites/features/
robot -d reports --include negativo test_suites/features/
```

### Ejecutar en paralelo (requiere robotframework-pabot)

```sh
pabot --outputdir reports test_suites/features/
```

---

## 📊 Reportes

- `reports/report.html`: Resumen visual de resultados.
- `reports/log.html`: Log detallado paso a paso.
- `reports/output.xml`: Salida en XML (para CI/CD).
- `reports/screenshots/`: Evidencia visual de fallos.

---

## 🏷️ Sistema de Tags

- `smoke`, `funcional`, `regression`, `positivo`, `negativo`
- Por feature: `autenticacion`, `modulos`, `venteros`, etc.
- Por prioridad: `alta`, `media`, `baja`

---

## 🔧 Configuración de Entornos

Variables principales en `config/config.robot`:

```robot
${BASE_URL}         https://www.medellin.gov.co
${SISDEP_URL}       ${BASE_URL}/sisdep/
${BROWSER}          chrome
${VALID_USERNAME}   admin
${VALID_PASSWORD}   EspacioPublico2024ep
```

---

## 📚 Features Implementadas

### Regulaciones
- **Gestión de Módulos:** Registrar, actualizar, eliminar módulos.
- **Gestión de Autorizaciones:** Flujos de autorización.
- **Asignación de Visitas:** Asignar y gestionar visitas.

### Social
- **Gestión de Venteros:** Registrar, actualizar, generar reporte Excel.
- **Estudio Socioeconómico:** Crear, firmar, generar PDF.
- **Ofertas Institucionales:** Registrar oferta, agregar/eliminar participantes.
- **Gestión de Vehículos:** Registrar y eliminar vehículos.

### Administración
- **Gestión de Dominios, Grupos, Usuarios:** CRUD y permisos.

### Autenticación
- **Login/Logout:** Casos positivos y negativos.

---

## ⚙️ Integración Continua (CI/CD)

### GitHub Actions

- Archivo: `.github/workflows/robot-tests.yml`
- Ejecuta pruebas automáticamente en cada push/PR.
- Instala Google Chrome y ChromeDriver compatible.
- Publica los reportes como artefactos.

### Azure DevOps

- Archivo: `azure-pipelines.yml`
- Pipeline para ejecución automática en ramas principales.
- Publica resultados y artefactos.

---

## 🛠️ Buenas Prácticas

- Usa Page Object Model para mantener los selectores centralizados.
- Keywords descriptivos y reutilizables en español.
- Documenta cada test y keyword.
- Usa tags para clasificar y filtrar pruebas.
- Actualiza los selectores cuando cambie la UI.
- Haz backup de reportes importantes antes de nuevas ejecuciones.

---

## 🤝 Contribución

1. Crea una rama para tu feature o fix.
2. Desarrolla siguiendo la estructura y buenas prácticas.
3. Ejecuta pruebas localmente antes de hacer push.
4. Haz Pull Request para revisión y merge.

---

## 📞 Soporte

- Consulta la documentación de cada feature (`README.md` en cada carpeta).
- Revisa los logs en `reports/log.html`.
- Verifica la configuración en `config/config.robot`.

---

**Desarrollado para la Alcaldía de Medellín**  
**Sistema SISDEP - Pruebas Automatizadas** 