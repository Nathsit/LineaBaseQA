*** Settings ***
Documentation     Suite de pruebas para la gestión de dominios en SISDEP
...               Incluye: agregar, actualizar y eliminar valores de dominios
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_dominios_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Agregar Nuevo Valor A Dominio
    [Documentation]    Agregar un nuevo valor a un dominio existente
    [Tags]    dominios    agregar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    Ingresa Nuevo Valor En Dominio    ${NUEVO_VALOR_DOMINIO}
    Hace Click En Agregar Valor
    El Sistema Anade El Nuevo Valor Al Dominio

Actualizar Valor De Dominio
    [Documentation]    Actualizar la descripción de un valor existente en un dominio
    [Tags]    dominios    actualizar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    Hace Click En Actualizar Valor
    El Sistema Guarda Los Cambios Del Valor

Eliminar Valor De Dominio No En Uso
    [Documentation]    Eliminar un valor de dominio que no está asociado a ningún registro
    [Tags]    dominios    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    Hace Click En Eliminar Valor

