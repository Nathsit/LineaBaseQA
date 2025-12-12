# Pipelines de Azure DevOps para SISDEP

Este directorio contiene los archivos YAML para configurar pipelines de CI/CD en Azure DevOps para ejecutar las pruebas automatizadas del proyecto SISDEP.

## Estructura de Pipelines

### Pipelines por Módulo

1. **01-autenticacion.yml** - Ejecuta pruebas del módulo de autenticación
   - Login exitoso
   - Login con credenciales inválidas
   - Logout

2. **02-administracion.yml** - Ejecuta pruebas del módulo de administración
   - Gestión de usuarios
   - Gestión de grupos y permisos
   - Gestión de dominios

3. **03-regulaciones.yml** - Ejecuta pruebas del módulo de regulaciones
   - Gestión de autorizaciones
   - Gestión de módulos
   - Asignación de visitas

4. **04-social.yml** - Ejecuta pruebas del módulo social
   - Gestión de venteros
   - Gestión de vehículos
   - Gestión de ofertas institucionales
   - Estudio socioeconómico

### Pipeline Principal

5. **00-all-modules.yml** - Ejecuta todas las pruebas de todos los módulos en paralelo
   - Configura el entorno una vez
   - Ejecuta todos los módulos en paralelo
   - Consolida y publica todos los reportes

## Configuración en Azure DevOps

### Crear un Pipeline

1. Ve a **Pipelines** > **New Pipeline** en Azure DevOps
2. Selecciona tu repositorio
3. Selecciona **Existing Azure Pipelines YAML file**
4. Selecciona la ruta del archivo YAML (ej: `SISDEP-LineaBase/pipelines/01-autenticacion.yml`)
5. Guarda y ejecuta

### Variables de Entorno

Los pipelines utilizan las siguientes variables por defecto:
- `pythonVersion: '3.11'` - Versión de Python
- `moduleName` - Nombre del módulo (automático según el pipeline)

### Triggers

Los pipelines se ejecutan automáticamente cuando:
- Se hace push a las ramas: `LineaBase`, `main`, `master`
- Se modifican archivos relacionados con el módulo correspondiente

### Reportes

Cada pipeline genera:
- **Reporte HTML**: `reports/{modulo}/report.html`
- **Reporte JUnit XML**: `reports/{modulo}/junit.xml` (para integración con Azure DevOps)

Los reportes se publican como artefactos de build y están disponibles en la pestaña **Artifacts** de cada ejecución del pipeline.

## Ejecución Manual

También puedes ejecutar los pipelines manualmente desde Azure DevOps:
1. Ve a **Pipelines**
2. Selecciona el pipeline que deseas ejecutar
3. Haz clic en **Run pipeline**

## Notas

- Los pipelines están configurados para continuar aunque algunos tests fallen (`continueOnError: true`)
- Los reportes se publican como artefactos para su descarga
- Los resultados de pruebas se integran con el dashboard de Azure DevOps Test Plans

