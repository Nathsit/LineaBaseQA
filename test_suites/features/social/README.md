# Gestión de Venteros (Social)

Este módulo contiene la suite de pruebas automatizadas para la feature **Gestión de Venteros** en SISDEP.

## Escenarios cubiertos

1. **Registrar un nuevo ventero**
   - Navega a la opción de "Registro ventero".
   - Llena todos los campos requeridos en el formulario.
   - Hace clic en "Guardar".
   - Verifica que el registro se crea exitosamente.

2. **Actualizar la información de un ventero**
   - Selecciona los detalles de un ventero existente.
   - Modifica los campos deseados y guarda los cambios.
   - Verifica que la información se actualiza correctamente.

3. **Generar reporte de venteros en Excel**
   - Accede al menú "Persona".
   - Aplica filtros de búsqueda.
   - Hace clic en el botón "Excel".
   - Verifica que se descarga el reporte en formato Excel con los venteros filtrados.

## Estructura de archivos

- `gestion_venteros.robot`: Suite de pruebas con los escenarios principales.
- `../../page_objects/sisdep_venteros_page.robot`: Page Object con los selectores y keywords reutilizables.

## Ejecución de las pruebas

Desde la raíz del proyecto, ejecuta:

```sh
robot -d reports test_suites/features/social/gestion_venteros.robot
```

Para ejecutar un caso de prueba específico:

```sh
robot -d reports --test "Registrar Nuevo Ventero" test_suites/features/social/gestion_venteros.robot
```

# Estudio Socioeconómico (Social)

Este módulo contiene la suite de pruebas automatizadas para la feature **Estudio Socioeconómico** en SISDEP.

## Escenarios cubiertos

1. **Crear un nuevo estudio socioeconómico**
   - Selecciona una visita asignada.
   - Elige el causal del estudio.
   - Completa todos los formularios requeridos y guarda.
   - Verifica que se crea el estudio asociado a la visita.

2. **Firmar un estudio socioeconómico completo**
   - Accede a un estudio socioeconómico completo.
   - Hace clic en el botón "Firmar".
   - Verifica que el estado cambia a "Firmado".

3. **Generar el PDF de un estudio socioeconómico**
   - Accede a un estudio socioeconómico.
   - Hace clic en el botón "PDF".
   - Verifica que se genera y muestra el PDF con la información del estudio.

## Estructura de archivos

- `estudio_socioeconomico.robot`: Suite de pruebas con los escenarios principales.
- `../../page_objects/sisdep_estudio_socioeconomico_page.robot`: Page Object con los selectores y keywords reutilizables.

## Ejecución de las pruebas

Desde la raíz del proyecto, ejecuta:

```sh
robot -d reports test_suites/features/social/estudio_socioeconomico.robot
```

Para ejecutar un caso de prueba específico:

```sh
robot -d reports --test "Crear Nuevo Estudio Socioeconomico" test_suites/features/social/estudio_socioeconomico.robot
```

# Gestión de Vehículos

Este módulo contiene la suite de pruebas automatizadas para la feature **Gestión de Vehículos** en SISDEP.

## Escenarios cubiertos

1. **Registrar un nuevo vehículo**
   - Navega al módulo de "Vehículos".
   - Hace clic en "Agregar" y completa el formulario del vehículo.
   - Hace clic en "Guardar".
   - Verifica que el vehículo es registrado en el sistema.

2. **Eliminar un vehículo no utilizado**
   - Navega al módulo de "Vehículos".
   - Selecciona un vehículo no utilizado.
   - Hace clic en "Remover" y confirma la acción.
   - Verifica que el vehículo es eliminado.

## Estructura de archivos

- `gestion_vehiculos.robot`: Suite de pruebas con los escenarios principales.
- `../../page_objects/sisdep_vehiculos_page.robot`: Page Object con los selectores y keywords reutilizables.

## Ejecución de las pruebas

Desde la raíz del proyecto, ejecuta:

```sh
robot -d reports test_suites/features/social/gestion_vehiculos.robot
```

Para ejecutar un caso de prueba específico:

```sh
robot -d reports --test "Registrar Nuevo Vehiculo" test_suites/features/social/gestion_vehiculos.robot
```

## Notas
- Los selectores y keywords deben ser completados según la implementación real de la aplicación.
- Los reportes se generan en la carpeta `reports`.
