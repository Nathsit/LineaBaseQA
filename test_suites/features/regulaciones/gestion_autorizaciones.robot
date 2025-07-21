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
    
    # Given: El usuario está en la sección de "Autorizaciones"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    # When: Busca un ventero por su documento
    Buscar Ventero Por Documento    ${DOCUMENTO_VENTERO}
    # And: Completa los datos de la solicitud y hace clic en guardar
    Completar Datos Solicitud Autorizacion
    Hacer Click En Guardar Solicitud
    # Then: Se crea una nueva solicitud de autorización para el ventero
    El Sistema Crea Nueva Solicitud Autorizacion

Agregar Visita Administrativa A Autorizacion
    [Documentation]    Agregar una visita administrativa a una autorización existente
    [Tags]    autorizaciones    visita    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: Existe una solicitud de autorización
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    # When: El usuario accede a los detalles de la autorización
    Acceder A Detalles Autorizacion    ${RADICADO_MERCURIO}
    # And: Hace clic en "Agregar" en la sección de visitas administrativas
    Hacer Click En Agregar Visita Administrativa
    # And: Completa y guarda el formulario de la visita
    Agregar Visita Administrativa A Autorizacion
    # Then: La visita administrativa queda registrada y asociada a la autorización
    El Sistema Registra Visita Administrativa

Agregar Resolucion A Solicitud Autorizacion
    [Documentation]    Agregar una resolución a una solicitud de autorización
    [Tags]    autorizaciones    resolucion    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: El usuario está en los detalles de una solicitud de autorización
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Acceder A Detalles Autorizacion    ${RADICADO_MERCURIO}
    # When: Hace clic en "Agregar resolución"
    Hacer Click En Agregar Resolucion
    # And: Completa el formulario de la resolución y da clic en guardar
    #Completar Formulario Resolucion    RES-2024-001    01/07/2025    01/07/2025
    #Hacer Click En Guardar Resolucion
    # Then: La resolución se asocia a la solicitud de autorización
    #El Sistema Asocia Resolucion A Autorizacion

Eliminar Autorizacion
    [Documentation]    Eliminar una autorización del sistema
    [Tags]    autorizaciones    eliminar    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: El usuario está en el listado de "Autorizaciones"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones 
    Hacer Click En Eliminar Autorizacion    ${RADICADO_MERCURIO}
    # And: Confirma la acción
    Confirmar Eliminacion Autorizacion
    # Then: La autorización es eliminada del sistema
    El Sistema Elimina La Autorizacion

Generar Reporte Autorizaciones Excel
    [Documentation]    Generar reporte de autorizaciones en Excel
    [Tags]    autorizaciones    reporte    excel    positivo
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    
    # Given: El usuario se encuentra en la pantalla de "Autorizaciones"
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    El Usuario Esta En Seccion Autorizaciones
    Hacer Click En Boton Excel
