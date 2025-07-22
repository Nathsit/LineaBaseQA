*** Settings ***
Documentation     Suite de pruebas para la gestión de autorizaciones en SISDEP
...               Incluye: crear, agregar visita, agregar resolución, eliminar y generar reporte
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_autorizaciones_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Creacion Nueva Solicitud Autorizacion
    [Documentation]    Crear una nueva solicitud de autorización para un ventero
    [Tags]    autorizaciones    crear    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Buscar Ventero Por Documento    ${DOCUMENTO_VENTERO}
    Completar Datos Solicitud Autorizacion
    Hacer Click En Guardar Solicitud
    El Sistema Crea Nueva Solicitud Autorizacion

Agregar Visita Administrativa A Autorizacion
    [Documentation]    Agregar una visita administrativa a una autorización existente
    [Tags]    autorizaciones    visita    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Acceder A Detalles Autorizacion    ${RADICADO_MERCURIO}
    Hacer Click En Agregar Visita Administrativa
    Agregar Visita Administrativa A Autorizacion
    El Sistema Registra Visita Administrativa

Agregar Resolucion A Solicitud Autorizacion
    [Documentation]    Agregar una resolución a una solicitud de autorización
    [Tags]    autorizaciones    resolucion    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Acceder A Detalles Autorizacion    ${RADICADO_MERCURIO}
    Hacer Click En Agregar Resolucion
   

Eliminar Autorizacion
    [Documentation]    Eliminar una autorización del sistema
    [Tags]    autorizaciones    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones 
    Hacer Click En Eliminar Autorizacion    ${RADICADO_MERCURIO}
    Confirmar Eliminacion Autorizacion
    El Sistema Elimina La Autorizacion

Generar Reporte Autorizaciones Excel
    [Documentation]    Generar reporte de autorizaciones en Excel
    [Tags]    autorizaciones    reporte    excel    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Hacer Click En Boton Excel
