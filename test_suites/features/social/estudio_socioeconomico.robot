*** Settings ***
Documentation     Suite de pruebas para la Feature: Estudio Socioeconómico (Social)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_estudio_socioeconomico_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Crear Nuevo Estudio Socioeconomico
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Estudio Socioeconomico
    Filtrar Estudio Por Fecha    2025    jul.
    Seleccionar Estudio Socioeconomico En Calendario
    Guardar Formularios Estudio Varias Veces


Firmar Estudio Socioeconomico Completo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Estudio Socioeconomico
    Filtrar Estudio Por Fecha    2025    jul.
    Seleccionar Estudio Socioeconomico En Calendario
    Guardar Formularios Estudio Varias Veces

Generar PDF Estudio Socioeconomico
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Estudio Socioeconomico
    Filtrar Estudio Por Fecha    2025    abr.
    
