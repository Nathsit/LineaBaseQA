*** Settings ***
Documentation     Suite completa de pruebas para la Feature: Autenticación de Usuario
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_dashboard_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Smoke Test - Login Exitoso
    [Documentation]    Test crítico de login exitoso
    [Tags]             smoke    autenticacion    login
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verificar Login Exitoso SISDEP

Smoke Test - Login Con Credenciales Invalidas
    [Documentation]    Test crítico de validación de credenciales
    [Tags]             smoke    autenticacion    login    negativo
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${INVALID_USERNAME}    ${INVALID_PASSWORD}
    Verificar Login Fallido SISDEP    ${SISDEP_LOGIN_ERROR_MSG}

# Functional Tests - Pruebas funcionales completas
Functional Test - Flujo Completo Login Logout
    [Documentation]    Test del flujo completo de login y logout
    [Tags]             funcional    autenticacion    flujo_completo
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    # Login
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verificar Login Exitoso SISDEP
    Verificar Dashboard Cargado
    
    # Logout
    Realizar Logout
    Verificar Logout Exitoso
    Verificar Elementos De Login SISDEP Presentes

# Regression Tests - Pruebas de regresión
Regression Test - Validacion De Campos
    [Documentation]    Test de validación de campos de login
    [Tags]             regression    autenticacion    validacion
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Verificar Elementos De Login SISDEP Presentes
    Limpiar Campos De Login SISDEP
    Tomar Screenshot    validacion_campos_vacios 

