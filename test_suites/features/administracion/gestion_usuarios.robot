*** Settings ***
Documentation     Feature: Gestión de Usuarios (Administración)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_usuarios_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Registro De Nuevo Usuario Exitoso
    [Documentation]    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    [Tags]             administracion    usuarios    positivo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Usuarios
    Hacer Click En Elemento    ${AGREGAR_USUARIO_BUTTON}
    Sleep    2s
    Verificar Elemento Presente    ${FORM_NOMBRE}

Actualizacion De Informacion De Usuario
    [Documentation]    Given que el administrador está en la sección "Administración - Usuarios".
    [Tags]             administracion    usuarios    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Usuarios
    Ingresar Texto En Filtro Documento    1000870852
    Seleccionar Usuario Por Documento    1000870852
    Editar Solo Email Usuario    usuario.editado@prueba.com
    Verificar Email Actualizado

Eliminacion De Usuario Existente
    [Documentation]    Given que el administrador está en la sección "Administración - Usuarios".
    [Tags]             administracion    usuarios    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Usuarios
    Ingresar Texto En Filtro Documento    1000870852
    Seleccionar Usuario Por Documento    1000870852
    Eliminar Usuario

Registro De Nuevo Usuario Campos Vacios
    [Documentation]    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    [Tags]             administracion    usuarios    positivo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Usuarios
    Hacer Click En Elemento    ${AGREGAR_USUARIO_BUTTON}
    Sleep    2s
    Verificar Elemento Presente    ${FORM_NOMBRE}
    Ingresar Texto En Campos Vacios


Registro De Nuevo Usuario ya Existente
    [Documentation]    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    [Tags]             administracion    usuarios    positivo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Usuarios
    Hacer Click En Elemento    ${AGREGAR_USUARIO_BUTTON}
    Sleep    2s
    Verificar Elemento Presente    ${FORM_NOMBRE}
