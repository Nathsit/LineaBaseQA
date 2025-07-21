# 🧑‍💼 Features de Administración SISDEP

Este directorio contiene las suites automatizadas para las funcionalidades de administración en SISDEP.

## 📋 Features cubiertas

### 1. Gestión de Usuarios
- Registro de un nuevo usuario de forma exitosa
- Actualización de la información de un usuario
- Eliminación de un usuario existente

### 2. Gestión de Grupos y Permisos
- Creación de un nuevo grupo con permisos específicos
- Actualización de los permisos de un grupo
- Eliminación de un grupo

### 3. Gestión de Dominios
- Agregar un nuevo valor a un dominio existente
- Actualizar la descripción de un valor de dominio
- Eliminar un valor de dominio que no está en uso
- Validar que no se puede eliminar un valor de dominio que está en uso

## 📝 Datos de ejemplo

- Usuario de prueba: `Usuario Prueba` / `usuario.prueba@correo.com`
- Grupo de prueba: `Grupo Prueba`
- Permisos de ejemplo: `Permiso1`, `Permiso2`, `Permiso3`, `Permiso4`
- Dominio de prueba: `Tipo de Documento`
- Valores de dominio: `Cédula de Ciudadanía`, `Pasaporte Extranjero`, `Valor Temporal`

## 🚀 Ejecución de las suites

Desde la raíz del proyecto, ejecuta:

```sh
robot -d reports test_suites/features/administracion/gestion_usuarios.robot test_suites/features/administracion/gestion_grupos_permisos.robot test_suites/features/administracion/gestion_dominios.robot
```

O puedes ejecutar solo una feature:

```sh
robot -d reports test_suites/features/administracion/gestion_usuarios.robot
```

```sh
robot -d reports test_suites/features/administracion/gestion_grupos_permisos.robot
```

```sh
robot -d reports test_suites/features/administracion/gestion_dominios.robot
```

Esto generará los reportes en la carpeta `reports/`.

## 📂 Estructura de archivos

- `gestion_usuarios.robot`: Casos de prueba para gestión de usuarios.
- `gestion_grupos_permisos.robot`: Casos de prueba para gestión de grupos y permisos.
- `gestion_dominios.robot`: Casos de prueba para gestión de dominios.
- `README.md`: Esta documentación.

## 🔗 Dependencias

- Page Objects: `page_objects/sisdep_usuarios_page.robot`, `page_objects/sisdep_grupos_page.robot`, `page_objects/sisdep_dominios_page.robot`
- Keywords comunes: `resources/common_keywords.robot`
- Datos de prueba: `data/sisdep_test_data.robot`

