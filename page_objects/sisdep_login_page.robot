*** Settings ***
Documentation     Page Object para la página de login de SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Locators de la página de login SISDEP (TODO: Actualizar con locators reales)
#${SISDEP_LOGIN_PAGE_TITLE}     xpath://h5[@class='titulo--L_2V']
${SISDEP_LOGIN_PAGE_TITLE}     xpath://h5[@class='L_2VJc3_']
${SISDEP_USERNAME_FIELD}       id:usuario    
${SISDEP_PASSWORD_FIELD}       id:password    
${SISDEP_LOGIN_BUTTON}         xpath://button[.//span[text()='Iniciar sesión']]
${SISDEP_ERROR_MESSAGE}        xpath://div[contains(@class, 'ant-message-error')]
${SISDEP_SUCCESS_MESSAGE}      xpath://span[text()='Administrador']
${SISDEP_LOGOUT_BUTTON}        xpath://li[contains(@class, ant-dropdown-menu-item)]//span[text()='Cerrar sesión']

# Mensajes esperados en SISDEP
${SISDEP_LOGIN_ERROR_MSG}      Error accediendo
${MENSAJE_USUARIO_INACTIVO}    xpath://div[contains(@class,'ant-alert-message') and contains(text(),'Usuario no activado por el administrador')]
${USUARIO_INPUT}    id:usuario 

*** Keywords ***
Navegar A SISDEP
    [Documentation]    Navega a la página principal de SISDEP
    Go To    ${SISDEP_URL}
    Verificar Elemento Presente    ${SISDEP_LOGIN_PAGE_TITLE}

Ingresar Usuario SISDEP
    [Documentation]    Ingresa el nombre de usuario en SISDEP
    [Arguments]    ${usuario}
    Ingresar Texto    ${SISDEP_USERNAME_FIELD}    ${usuario}

Ingresar Contraseña SISDEP
    [Documentation]    Ingresa la contraseña en SISDEP
    [Arguments]    ${contraseña}
    Ingresar Texto    ${SISDEP_PASSWORD_FIELD}    ${contraseña}

Hacer Click En Login SISDEP
    [Documentation]    Hace click en el botón de login de SISDEP
    Hacer Click En Elemento    ${SISDEP_LOGIN_BUTTON}

Realizar Login SISDEP
    [Documentation]    Realiza el proceso completo de login en SISDEP
    [Arguments]    ${usuario}    ${contraseña}
    Ingresar Usuario SISDEP    ${usuario}
    Ingresar Contraseña SISDEP    ${contraseña}
    Hacer Click En Login SISDEP

Verificar Login Exitoso SISDEP
    [Documentation]    Verifica que el login en SISDEP fue exitoso
    Verificar Elemento Presente    ${SISDEP_SUCCESS_MESSAGE}

Verificar Login Fallido SISDEP
    [Documentation]    Verifica que el login en SISDEP falló
    [Arguments]    ${mensaje_error}
    Verificar Texto En Página    ${mensaje_error}

Verificar Mensaje De Error SISDEP
    [Documentation]    Verifica que se muestre un mensaje de error específico en SISDEP
    [Arguments]    ${mensaje}
    Verificar Texto En Página    ${mensaje}

Limpiar Campos De Login SISDEP
    [Documentation]    Limpia los campos de usuario y contraseña en SISDEP
    Limpiar Campo    ${SISDEP_USERNAME_FIELD}
    Limpiar Campo    ${SISDEP_PASSWORD_FIELD}

Verificar Elementos De Login SISDEP Presentes
    [Documentation]    Verifica que todos los elementos de la página de login de SISDEP estén presentes
    Verificar Elemento Presente    ${SISDEP_LOGIN_PAGE_TITLE}
    Verificar Elemento Presente    ${SISDEP_USERNAME_FIELD}
    Verificar Elemento Presente    ${SISDEP_PASSWORD_FIELD}
    Verificar Elemento Presente    ${SISDEP_LOGIN_BUTTON}

Explorar Elementos De La Página
    [Documentation]    Keyword temporal para explorar y identificar elementos de la página
    Log    Explorando elementos de la página SISDEP...
    # TODO: Agregar keywords para identificar elementos dinámicamente
    # Ejemplo: Get All Elements, Get Element Attributes, etc. 

Verificar Usuario Inactivo
    [Documentation]    Verifica que el usuario no puede iniciar sesión y recibe un mensaje de error claro.
    Sleep    2s
    Verificar Texto En Página    Usuario no activado por el administrador.
