*** Settings ***
Documentation     Feature: Autenticación de Usuario - Scenario: Inicio de sesión con credenciales inválidas
Resource          ../../../../resources/common_keywords.robot
Resource          ../../../../page_objects/sisdep_login_page.robot
Resource          ../../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Inicio De Sesion Con Credenciales Incorrectas
    [Documentation]    Given que el usuario se encuentra en la página de inicio de sesión.
    ...                When ingresa un nombre de usuario o contraseña incorrectos.
    ...                And hace clic en el botón Iniciar sesión".
    ...                Then el sistema muestra un mensaje de error indicando que las credenciales son inválidas.
    [Tags]             autenticacion    login    negativo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Verificar Elementos De Login SISDEP Presentes    
    Realizar Login SISDEP    ${INVALID_USERNAME}    ${INVALID_PASSWORD}    
    Verificar Login Fallido SISDEP    ${SISDEP_LOGIN_ERROR_MSG}
    Verificar Elemento Presente    ${SISDEP_ERROR_MESSAGE}    
    Tomar Screenshot    login_credenciales_invalidas

Inicio De Sesion Con Usuario Invalido
    [Documentation]    Test específico para usuario inválido con contraseña válida
    [Tags]             autenticacion    login    negativo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${INVALID_USERNAME}    ${VALID_PASSWORD}
    Verificar Login Fallido SISDEP    ${SISDEP_LOGIN_ERROR_MSG}
    Tomar Screenshot    login_usuario_invalido

Inicio De Sesion Con Password Invalido
    [Documentation]    Test específico para contraseña inválida con usuario válido
    [Tags]             autenticacion    login    negativo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${INVALID_PASSWORD}
    Verificar Login Fallido SISDEP    ${SISDEP_LOGIN_ERROR_MSG}
    Tomar Screenshot    login_password_invalido 