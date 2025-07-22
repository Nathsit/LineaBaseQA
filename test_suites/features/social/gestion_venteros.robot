*** Settings ***
Documentation     Suite de pruebas para la Feature: Gestión de Venteros (Social)
Library           String
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_venteros_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Registrar Nuevo Ventero
    [Documentation]    Given que el usuario está en la opción de "Registro ventero".
    ...                When llena todos los campos requeridos en el formulario.
    ...                And hace clic en "Guardar".
    ...                Then se crea un nuevo registro de ventero en el sistema.
    [Tags]    venteros    crear    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Registro Ventero
    ${DOCUMENTO_RANDOM}=    Generate Random String    10    [NUMBERS]
    Set Suite Variable    ${DOCUMENTO_PRUEBA}    ${DOCUMENTO_RANDOM}
    Completar Formulario Ventero    TEST    TEST    Cédula de ciudadanía    ${DOCUMENTO_PRUEBA}    01/01/2020    MEDELLÍN    Colombiano/a    Hombre    Natural    3001234567    01/01/1990    Soltero (a)    Preescolar
    Hacer Click En Guardar Ventero
    Verificar Creacion Ventero Exitosa

Actualizar Informacion Ventero
    [Documentation]    Given que el usuario ha seleccionado los detalles de un ventero.
    ...                When da clic en "Guardar".
    ...                Then la información del ventero se actualiza.
    [Tags]    venteros    actualizar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Personas Y Buscar Ventero Por Documento    ${DOCUMENTO_PRUEBA}
    Hacer Click En Guardar Ventero
    Verificar Actualizacion Ventero Exitosa

Generar Reporte Venteros Excel
    [Documentation]    Given que el usuario se encuentra en el menú "Persona".
    ...                When aplica los filtros de búsqueda deseados.
    ...                And hace clic en el botón "Excel".
    ...                Then el sistema descarga un reporte en formato Excel con los venteros filtrados.
    [Tags]    venteros    reporte    excel
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
     Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Hacer Click En Boton Excel Venteros    ${DOCUMENTO_PRUEBA}