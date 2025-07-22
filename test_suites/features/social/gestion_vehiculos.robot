*** Settings ***
Documentation     Suite de pruebas para la Feature: Gestión de Vehículos
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_vehiculos_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Registrar Nuevo Vehiculo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Vehiculos
    Hacer Click En Agregar Vehiculo
    Completar Formulario Vehiculo    Juan Perez    RJZ672    Camion
    Hacer Click En Guardar Vehiculo

Eliminar Vehiculo No Utilizado
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Vehiculos
    Eliminar Vehiculo Por Placa    RJZ672
    