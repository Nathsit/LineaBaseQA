*** Settings ***
Documentation     Feature: Autenticación de Usuario - Scenario: Inicio de sesión exitoso
Resource          ../../../../resources/common_keywords.robot
Resource          ../../../../page_objects/sisdep_login_page.robot
Resource          ../../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Inicio De Sesion Exitoso Con Credenciales Validas
    [Documentation]    Given que el usuario tiene un usuario y contraseña válidos y activos.
    ...                When ingresa sus credenciales en la página de inicio de sesión.
    ...                And hace clic en el botón Iniciar sesión".
    ...                Then el sistema le da la bienvenida y muestra la pantalla principal.
    [Tags]             autenticacion    login    positivo    smoke    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Verificar Elementos De Login SISDEP Presentes    
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}    
    Verificar Login Exitoso SISDEP
    Verificar Elemento Presente    ${SISDEP_SUCCESS_MESSAGE}    
    Tomar Screenshot    login_exitoso_completado 