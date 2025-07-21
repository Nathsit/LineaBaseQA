*** Settings ***
Documentation     Suite de pruebas para la Feature: Asignación de Visitas Domiciliarias (Regulaciones)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_visitas_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Asignar Nueva Visita A Ventero
    [Documentation]    Given que el usuario está en la sección de "Asignación de visitas".
    ...                When hace clic en "Nueva visita".
    ...                And busca al ventero por su documento.
    ...                And completa los datos de la visita y da clic en guardar.
    ...                Then se crea y asigna una nueva visita domiciliaria.
    [Tags]    visitas    asignar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Asignacion Visitas
    Hacer Click En Nueva Visita
    Buscar Ventero Por Documento En Visitas    ${DOCUMENTO_VENTERO}
    Completar Formulario Visita    Administrador DEL SISTEMA    Actualización    RJZ672    HOY    AM
    Hacer Click En Guardar Visita
    Verificar Creacion Visita Exitosa

Actualizar Datos De Visita Asignada
    [Documentation]    Given que el usuario está en la sección de "Asignación de visitas".
    ...                When selecciona una visita y hace clic en "Detalles".
    ...                And modifica la información de la visita y da clic en el botón de actualizar.
    ...                Then se guardan los cambios de la visita.
    [Tags]    visitas    actualizar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Asignacion Visitas
    Actualizar Datos Visita    2025-07-21    2025-07-21    Administrador DEL SISTEMA
    Hacer Click En Detalles Visita    
    Hacer Click En Actualizar Visita
    Verificar Actualizacion Visita Exitosa

Eliminar Visita Asignada
    [Documentation]    Given que el usuario se encuentra en la sección de "Asignación de visitas".
    ...                When hace clic en el botón eliminar de la visita que desea eliminar.
    ...                And confirma la eliminación.
    ...                Then la visita es eliminada.
    [Tags]    visitas    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Asignacion Visitas
    Actualizar Datos Visita    2025-07-21    2025-07-21    Administrador DEL SISTEMA
    Hacer Click En Eliminar Visita
    Confirmar Eliminacion Visita
    # TODO: Verificar que la visita fue eliminada 