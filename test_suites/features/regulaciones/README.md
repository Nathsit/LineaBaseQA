# 🏛️ Features de Regulaciones SISDEP

Este directorio contiene las suites automatizadas para las funcionalidades de regulaciones en SISDEP.

## 📋 Features cubiertas

### 1. Gestión de Autorizaciones
- Creación de una nueva solicitud de autorización para un ventero
- Agregar una visita administrativa a una autorización
- Agregar una resolución a una solicitud de autorización
- Eliminar una autorización
- Generar reporte de autorizaciones en Excel

## 🏠 Feature: Asignación de Visitas Domiciliarias

Esta feature automatiza la gestión de visitas domiciliarias asignadas a venteros.

### Escenarios cubiertos

1. **Asignar una nueva visita a un ventero**
    - Given que el usuario está en la sección de "Asignación de visitas".
    - When hace clic en "Nueva visita".
    - And busca al ventero por su documento.
    - And completa los datos de la visita y da clic en guardar.
    - Then se crea y asigna una nueva visita domiciliaria.

2. **Actualizar los datos de una visita asignada**
    - Given que el usuario está en la sección de "Asignación de visitas".
    - When selecciona una visita y hace clic en "Detalles".
    - And modifica la información de la visita y da clic en el botón de actualizar.
    - Then se guardan los cambios de la visita.

3. **Eliminar una visita asignada**
    - Given que el usuario se encuentra en la sección de "Asignación de visitas".
    - When hace clic en el botón eliminar de la visita que desea eliminar.
    - And confirma la eliminación.
    - Then la visita es eliminada.

---

## 🧩 Feature: Gestión de Módulos

Esta feature automatiza la gestión de módulos en el sistema SISDEP.

### Escenarios cubiertos

1. **Registrar un nuevo módulo**
    - Given que el usuario está en la sección de "Módulos".
    - When hace clic en el botón "Agregar".
    - And completa el formulario con los datos del nuevo módulo y hace clic en "Guardar".
    - Then el nuevo módulo se registra en el sistema.

2. **Actualizar la información de un módulo existente**
    - Given que el usuario está en la sección de "Módulos".
    - When selecciona un módulo y hace clic en "Detalles".
    - And modifica los datos del módulo y hace clic en "Guardar".
    - Then la información del módulo es actualizada.

3. **Eliminar un módulo**
    - Given que el usuario está en la lista de "Módulos".
    - When hace clic en "Eliminar" en un módulo específico.
    - And confirma la eliminación.
    - Then el módulo es eliminado del sistema.

---

## 📝 Datos de ejemplo

- Documento de ventero: `12345678`
- ID de autorización: `AUT-001`

## 🚀 Ejecución de las suites

Desde la raíz del proyecto, ejecuta:

```sh
robot -d reports test_suites/features/regulaciones/gestion_autorizaciones.robot
```

O puedes ejecutar tests específicos:

```sh
# Solo crear autorización
robot -d reports -t "Creacion Nueva Solicitud Autorizacion" test_suites/features/regulaciones/gestion_autorizaciones.robot

# Solo agregar visita
robot -d reports -t "Agregar Visita Administrativa A Autorizacion" test_suites/features/regulaciones/gestion_autorizaciones.robot

# Solo agregar resolución
robot -d reports -t "Agregar Resolucion A Solicitud Autorizacion" test_suites/features/regulaciones/gestion_autorizaciones.robot

# Solo eliminar autorización
robot -d reports -t "Eliminar Autorizacion" test_suites/features/regulaciones/gestion_autorizaciones.robot

# Solo generar reporte Excel
robot -d reports -t "Generar Reporte Autorizaciones Excel" test_suites/features/regulaciones/gestion_autorizaciones.robot
```

Esto generará los reportes en la carpeta `reports/`.

## 📂 Estructura de archivos

- `gestion_autorizaciones.robot`: Casos de prueba para gestión de autorizaciones.
- `README.md`: Esta documentación.

## 🔗 Dependencias

- Page Objects: `page_objects/sisdep_autorizaciones_page.robot`
- Keywords comunes: `resources/common_keywords.robot`
- Datos de prueba: `data/sisdep_test_data.robot`

## 🎯 Escenarios implementados

1. **Creación de autorización**: Buscar ventero → Completar formulario → Guardar
2. **Agregar visita**: Acceder a detalles → Agregar visita → Completar formulario → Guardar
3. **Agregar resolución**: Acceder a detalles → Agregar resolución → Completar formulario → Guardar
4. **Eliminar autorización**: Seleccionar autorización → Eliminar → Confirmar
5. **Generar reporte Excel**: Aplicar filtros → Click Excel → Verificar descarga

---

**Recuerda:** Ajusta los selectores y datos según la implementación real de la aplicación. 