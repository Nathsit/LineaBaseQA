*** Settings ***
Documentation     Feature: Gestión de Grupos y Permisos (Administración)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_grupos_page.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Creacion De Nuevo Grupo Con Permisos Especificos
    [Documentation]    Given que el administrador está en la sección "Administración - Grupos y Permisos".
    [Tags]             administracion    grupos    permisos    positivo    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Grupos Y Permisos
    Crear Nuevo Grupo Con Permisos    Grupo Prueba    Permiso1,Permiso2
    Verificar Grupo Creado    Grupo Prueba

Actualizacion De Permisos De Grupo
    [Documentation]    Given que el administrador está en la sección "Administración - Grupos y Permisos".
    [Tags]             administracion    grupos    permisos    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Grupos Y Permisos
    Seleccionar Grupo Para Editar    Grupo Prueba
    Actualizar Permisos De Grupo    Permiso3,Permiso4
    Verificar Permisos Actualizados

Eliminacion De Grupo
    [Documentation]    Given que el administrador se encuentra en la sección de "Grupos y Permisos".
    [Tags]             administracion    grupos    permisos    funcional
    [Setup]            Abrir Navegador    ${SISDEP_URL}
    [Teardown]         Cerrar Navegador
    
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Grupos Y Permisos
    Seleccionar Grupo Para Eliminar    Grupo Prueba
    Eliminar Grupo
