*** Settings ***
Documentation     Suite de pruebas para la Feature: Gestión de Módulos (Regulaciones)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_modulos_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Registrar Nuevo Modulo
    [Documentation]    Given que el usuario está en la sección de "Módulos".
    ...                When hace clic en el botón "Agregar".
    ...                And completa el formulario con los datos del nuevo módulo y hace clic en "Guardar".
    ...                Then el nuevo módulo se registra en el sistema.
    [Tags]    modulos    crear    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador

    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Modulos
    Hacer Click En Agregar Modulo
    Completar Formulario Modulo    Propia    Bueno    10.5    5.2    3.0    Oriental    Tipo 1    Estadio
    

Actualizar Informacion Modulo Existente
    [Documentation]    Given que el usuario está en la sección de "Módulos".
    ...                When selecciona un módulo y hace clic en "Detalles".
    ...                And modifica los datos del módulo y hace clic en "Guardar".
    ...                Then la información del módulo es actualizada.
    [Tags]    modulos    actualizar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador

    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Modulos
    Filtrar Modulo Por Serial    10-AVPL-002
    Hacer Click En Detalles Modulo
    Reload Page
    Hacer Click En Guardar Modulo
    Verificar Actualizacion Modulo Exitosa

Eliminar Modulo
    [Documentation]    Given que el usuario está en la lista de "Módulos".
    ...                When hace clic en "Eliminar" en un módulo específico.
    ...                And confirma la eliminación.
    ...                Then el módulo es eliminado del sistema.
    [Tags]    modulos    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador

    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Modulos
    Filtrar Modulo Por Serial    10-AVPL-002
    Hacer Click En Eliminar Modulo
