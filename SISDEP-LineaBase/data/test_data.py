"""
Datos de prueba para SISDEP
Equivalente a data/sisdep_test_data.robot
"""

# Datos de prueba para SISDEP
USUARIO_SISDEP_VALIDO = {
    "username": "admin",
    "password": "prueba123"
}

USUARIO_SISDEP_INVALIDO = {
    "username": "usuario_invalido",
    "password": "password_invalido"
}

USUARIO_SISDEP_VACIO = {
    "username": "",
    "password": ""
}

# Mensajes esperados en SISDEP
SISDEP_MENSAJE_LOGIN_EXITOSO = "Bienvenido al Sistema SISDEP"
SISDEP_MENSAJE_CREDENCIALES_INVALIDAS = "Credenciales inválidas"
SISDEP_MENSAJE_USUARIO_VACIO = "El campo usuario es requerido"
SISDEP_MENSAJE_PASSWORD_VACIO = "El campo contraseña es requerido"
SISDEP_LOGIN_ERROR_MSG = "Error accediendo"

# URLs específicas de SISDEP
SISDEP_URL_LOGIN = "https://base.innovacion.it.com/"
SISDEP_URL_DASHBOARD = "https://base.innovacion.it.com/dashboard"
SISDEP_URL_LOGOUT = "https://base.innovacion.it.com/logout"

# Configuraciones específicas para SISDEP
SISDEP_TIMEOUT_CARGA = 30000  # en milisegundos
SISDEP_TIMEOUT_LOGIN = 15000  # en milisegundos
SISDEP_TIMEOUT_NAVEGACION = 10000  # en milisegundos

# Roles de usuario en SISDEP
ROLES_SISDEP = ["administrador"]

# Datos de prueba para Gestión de Dominios
DOMINIO_TIPO_DOCUMENTO = "Social"
NUEVO_VALOR_DOMINIO = "Nueva EPS Test"

# Datos de prueba para Gestión de Usuarios
NUEVO_USUARIO = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "tipo_documento": "Cédula de ciudadanía",  # Valor exacto según el selector
    "documento": "1234567890",
    "grupo": "Administración",  # Ajustar según opciones disponibles
    "email": "juan.perez@prueba.com"
}

# Email actualizado para el test de actualización
EMAIL_USUARIO_ACTUALIZADO = "juan.perez.actualizado@prueba.com"

# Datos de prueba para Gestión de Autorizaciones
DOCUMENTO_VENTERO = "1000100100"
RADICADO_MERCURIO = "RAD-2024-001"
FECHA_INICIAL = "2024-12-20"  # Formato YYYY-MM-DD para campos type="date"
HORA_INICIO = "8"
HORA_FIN = "8"

# Datos de prueba para Gestión de Venteros
# Se generará un documento aleatorio en el test

# Datos de prueba para Gestión de Vehículos
NOMBRE_CONDUCTOR = "Juan Perez"
PLACA_VEHICULO = "RJZ673"
TIPO_VEHICULO = "Camion"
PLACA_VEHICULO_EN_USO = "RJZ672"

# Datos de prueba para Ofertas Institucionales
TIPO_OFERTA = "sena dadad"
CONVENIO = "Secretaria de Salud"
DOCUMENTO_PARTICIPANTE = "1000100100"
TIPO_CONOCIMIENTO = "Atención en la oficina"

