*** Settings ***
Documentation     Page Object para la página del dashboard de SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Locators del dashboard SISDEP (TODO: Actualizar con locators reales)
${SISDEP_DASHBOARD_TITLE}      xpath://h1[text()='SISDEP']
${SISDEP_USER_PROFILE_ICON}    xpath://span[contains(@class, 'ant-avatar') and contains(@class, 'ant-dropdown-trigger')]
${SISDEP_LOGOUT_OPTION}        xpath://span[contains(@class, 'ant-dropdown-menu-title-content') and text()='Cerrar sesión']
${SISDEP_LOGOUT_CONFIRM}       # No existe confirmación - se elimina del flujo

# Mensajes esperados
${SISDEP_LOGOUT_SUCCESS_MSG}   xpath://h5[@class='L_2VJc3_']    # Valida que estamos en la página de login

*** Keywords ***
Verificar Dashboard Cargado
    [Documentation]    Verifica que el dashboard se haya cargado correctamente
    Verificar Elemento Presente    ${SISDEP_DASHBOARD_TITLE}

Hacer Click En Perfil Usuario
    [Documentation]    Hace click en el ícono del perfil del usuario
    Hacer Click En Elemento    ${SISDEP_USER_PROFILE_ICON}

Seleccionar Cerrar Sesion
    [Documentation]    Selecciona la opción de cerrar sesión del menú desplegable
    Hacer Click En Elemento    ${SISDEP_LOGOUT_OPTION}

Confirmar Cerrar Sesion
    [Documentation]    Confirma el cierre de sesión si hay un modal de confirmación
    Hacer Click En Elemento    ${SISDEP_LOGOUT_CONFIRM}

Realizar Logout
    [Documentation]    Realiza el proceso completo de logout
    Hacer Click En Perfil Usuario
    Seleccionar Cerrar Sesion

Verificar Logout Exitoso
    [Documentation]    Verifica que el logout fue exitoso
    Verificar Elemento Presente    ${SISDEP_LOGOUT_SUCCESS_MSG}
    # También verificar que estamos en la página de login
    Verificar URL Contiene    ${URL_VERIFICATION_PATH} 