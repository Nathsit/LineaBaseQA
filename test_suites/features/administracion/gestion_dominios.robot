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
    
    # Given: El administrador está en la sección "Administración - Dominios"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    # When: Selecciona un dominio específico
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    # And: Ingresa un nuevo valor en el campo correspondiente
    Ingresa Nuevo Valor En Dominio    ${NUEVO_VALOR_DOMINIO}
    # And: Hace clic en "Agregar"
    Hace Click En Agregar Valor
    # Then: El sistema añade el nuevo valor a la lista de valores del dominio
    El Sistema Anade El Nuevo Valor Al Dominio

Actualizar Valor De Dominio
    [Documentation]    Actualizar la descripción de un valor existente en un dominio
    [Tags]    dominios    actualizar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: El administrador está en la sección "Administración - Dominios"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    # When: Selecciona un dominio específico
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    # And: Modifica la descripción de un valor existente
    Hace Click En Actualizar Valor
    # Then: El sistema guarda los cambios del valor
    El Sistema Guarda Los Cambios Del Valor

Eliminar Valor De Dominio No En Uso
    [Documentation]    Eliminar un valor de dominio que no está asociado a ningún registro
    [Tags]    dominios    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: El administrador está en la sección "Administración - Dominios"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Administrador Esta En Seccion Dominios
    # When: Selecciona un dominio específico
    Selecciona Dominio Especifico    ${DOMINIO_TIPO_DOCUMENTO}
    # And: Hace clic en el botón "Eliminar"
    Hace Click En Eliminar Valor

