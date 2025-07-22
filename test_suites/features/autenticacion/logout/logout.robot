*** Settings ***
Documentation     Feature: Autenticación de Usuario - Scenario: Cierre de sesión
Resource          ../../../../resources/common_keywords.robot
Resource          ../../../../page_objects/sisdep_login_page.robot
Resource          ../../../../page_objects/sisdep_dashboard_page.robot
Resource          ../../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Cierre De Sesion Exitoso
    [Documentation]    Given que el usuario ha iniciado sesión en el sistema.
    ...                When hace clic en el ícono de su perfil en la esquina superior derecha.
    ...                And selecciona la opción Cerrar sesión".
    ...                Then el sistema cierra la sesión y lo redirige a la página de inicio de sesión.
    [Tags]             autenticacion    logout    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verificar Login Exitoso SISDEP
    Verificar Dashboard Cargado
    
    Realizar Logout
    
    Verificar Logout Exitoso
    Verificar Elementos De Login SISDEP Presentes
    
    Tomar Screenshot    logout_exitoso_completado

Cierre De Sesion Desde Dashboard
    [Documentation]    Test alternativo para verificar logout desde diferentes ubicaciones del dashboard
    [Tags]             autenticacion    logout    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verificar Dashboard Cargado
    
    Realizar Logout
    Verificar Logout Exitoso
    Tomar Screenshot    logout_desde_dashboard 