*** Variables ***
# Datos de prueba para SISDEP
&{USUARIO_SISDEP_VALIDO}    username=# TODO: Usuario real    password=# TODO: Contraseña real
&{USUARIO_SISDEP_INVALIDO}    username=usuario_invalido    password=password_invalido
&{USUARIO_SISDEP_VACIO}    username=${EMPTY}    password=${EMPTY}

# Mensajes esperados en SISDEP (TODO: Actualizar con mensajes reales)
${SISDEP_MENSAJE_LOGIN_EXITOSO}    Bienvenido al Sistema SISDEP
${SISDEP_MENSAJE_CREDENCIALES_INVALIDAS}    Credenciales inválidas
${SISDEP_MENSAJE_USUARIO_VACIO}    El campo usuario es requerido
${SISDEP_MENSAJE_PASSWORD_VACIO}    El campo contraseña es requerido

# URLs específicas de SISDEP
${SISDEP_URL_LOGIN}    https://www.medellin.gov.co/sisdep/
${SISDEP_URL_DASHBOARD}    https://www.medellin.gov.co/sisdep/dashboard
${SISDEP_URL_LOGOUT}    https://www.medellin.gov.co/sisdep/logout

# Configuraciones específicas para SISDEP
${SISDEP_TIMEOUT_CARGA}    30s
${SISDEP_TIMEOUT_LOGIN}    15s
${SISDEP_TIMEOUT_NAVEGACION}    10s

# Roles de usuario en SISDEP (TODO: Actualizar según roles reales)
@{ROLES_SISDEP}    administrador

# Datos de prueba para Gestión de Dominios
${DOMINIO_TIPO_DOCUMENTO}    Social
${NUEVO_VALOR_DOMINIO}       Nueva EPS Test

# Datos de prueba para Gestión de Autorizaciones
${DOCUMENTO_VENTERO}         1000100100
${ID_AUTORIZACION}           AUT-001

# Datos del formulario de autorización
${RADICADO_MERCURIO}         RAD-2024-001
${FECHA_INICIAL}             20/12/2024
${HORA_INICIO}               8
${HORA_FIN}                  8