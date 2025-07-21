# Feature: Autenticación de Usuario

## Descripción
Esta feature contiene todas las pruebas relacionadas con la autenticación de usuarios en el sistema SISDEP.

## Escenarios Cubiertos

### 1. Inicio de Sesión Exitoso
- **Archivo**: `login_exitoso.robot`
- **Descripción**: Verifica que un usuario con credenciales válidas pueda iniciar sesión correctamente
- **Tags**: `autenticacion`, `login`, `positivo`, `smoke`, `funcional`

### 2. Inicio de Sesión con Credenciales Incorrectas
- **Archivo**: `login_credenciales_invalidas.robot`
- **Descripción**: Verifica que el sistema muestre mensajes de error apropiados para credenciales inválidas
- **Tags**: `autenticacion`, `login`, `negativo`, `funcional`
- **Casos incluidos**:
  - Credenciales completamente inválidas
  - Usuario inválido con contraseña válida
  - Contraseña inválida con usuario válido

### 3. Cierre de Sesión
- **Archivo**: `logout.robot`
- **Descripción**: Verifica que el usuario pueda cerrar sesión correctamente
- **Tags**: `autenticacion`, `logout`, `funcional`

## Suite Principal
- **Archivo**: `autenticacion_suite.robot`
- **Descripción**: Suite que ejecuta todos los tests de autenticación organizados por tipo
- **Incluye**:
  - Smoke Tests (críticos)
  - Functional Tests (funcionales)
  - Regression Tests (regresión)

## Ejecución

### Ejecutar todos los tests de autenticación:
```bash
robot -d reports test_suites/features/autenticacion/autenticacion_suite.robot
```

### Ejecutar solo smoke tests:
```bash
robot -d reports --include smoke test_suites/features/autenticacion/autenticacion_suite.robot
```

### Ejecutar tests específicos:
```bash
# Solo login exitoso
robot -d reports test_suites/features/autenticacion/login_exitoso.robot

# Solo tests negativos
robot -d reports --include negativo test_suites/features/autenticacion/
```

## Dependencias
- `config/config.robot` - Configuración global
- `resources/common_keywords.robot` - Keywords comunes
- `page_objects/sisdep_login_page.robot` - Page Object del login
- `page_objects/sisdep_dashboard_page.robot` - Page Object del dashboard
- `data/sisdep_test_data.robot` - Datos de prueba

## Notas Importantes
- Los locators en los Page Objects deben ser actualizados con los valores reales de la aplicación
- Las credenciales de prueba están configuradas en `config/config.robot`
- Todos los tests incluyen capturas de pantalla como evidencia 