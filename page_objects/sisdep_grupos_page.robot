*** Settings ***
Documentation     Page Object para la gestión de grupos y permisos en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Locators genéricos (ajustar según HTML real)
${GRUPOS_SECTION_TITLE}         xpath://h1[contains(., 'Grupos y Permisos')]
${NUEVO_GRUPO_BUTTON}           xpath://button[@aria-label='Nuevo grupo' and .//span[text()='Nuevo grupo']]
${NOMBRE_GRUPO_FIELD}           css:#nombre
${DESCRIPCION_GRUPO_FIELD}      css:#descripcion
${CHECK_ES_SOCIAL}              css:#esSocial
${CHECK_OTRO}                   xpath:(//button[@role='switch'])[2]
${GUARDAR_GRUPO_BUTTON}         xpath://button[@aria-label='Guardar permisos' and .//span[text()='Guardar']]
${EDITAR_GRUPO_BUTTON}          xpath://button[@aria-label='Detalles' and .//span[text()='Detalles']]
${REMOVER_GRUPO_BUTTON}         xpath://button[@aria-label='Remover' and .//span[text()='Remover']]
${CONFIRMAR_REMOVER_BUTTON}     xpath://button[.//span[contains(., 'Sí, eliminar')]]
${MENU_ADMINISTRACION}         xpath://div[@role='menuitem' and .//span[text()='Administracion']]
${GRUPOS_PERMISOS_LINK}        xpath://a[@href='/sisdep/administracion/grupos' and text()='Grupos y permisos']

*** Keywords ***
Ir A Seccion Grupos Y Permisos
    [Documentation]    Navega a la sección de administración de grupos y permisos
    Hacer Click En Elemento    ${MENU_ADMINISTRACION}
    Hacer Click En Elemento    ${GRUPOS_PERMISOS_LINK}
    Verificar Elemento Presente    ${GRUPOS_SECTION_TITLE}

Crear Nuevo Grupo Con Permisos
    [Documentation]    Crea un nuevo grupo y asigna permisos
    [Arguments]    ${nombre_grupo}    ${permisos}
    Hacer Click En Elemento    ${NUEVO_GRUPO_BUTTON}
    Sleep    3s
    Ingresar Texto    ${NOMBRE_GRUPO_FIELD}    ${nombre_grupo}
    Ingresar Texto    ${DESCRIPCION_GRUPO_FIELD}    Grupo de prueba automatizado
    Hacer Click En Elemento    ${CHECK_ES_SOCIAL}
    Hacer Click En Elemento    ${CHECK_OTRO}
    Hacer Click En Elemento    ${GUARDAR_GRUPO_BUTTON}

Verificar Grupo Creado
    [Documentation]    Verifica que el grupo fue creado correctamente
    [Arguments]    ${nombre_grupo}
    Sleep    2s
    Verificar Texto En Página    Registro creado exitosamente

Seleccionar Grupo Para Editar
    [Documentation]    Selecciona un grupo para editar
    [Arguments]    ${nombre_grupo}
    Filtrar Grupo Por Nombre    ${nombre_grupo}
    Hacer Click En Elemento    ${EDITAR_GRUPO_BUTTON}

Actualizar Permisos De Grupo
    [Documentation]    Actualiza la descripción del grupo
    [Arguments]    ${nueva_descripcion}
    Ingresar Texto    ${DESCRIPCION_GRUPO_FIELD}    ${nueva_descripcion}
    Hacer Click En Elemento    ${GUARDAR_GRUPO_BUTTON}

Verificar Permisos Actualizados
    [Documentation]    Verifica que el grupo fue actualizado exitosamente
    Sleep    2s
    Verificar Texto En Página    ¡Registro actualizado exitosamente!

Seleccionar Grupo Para Eliminar
    [Documentation]    Selecciona un grupo para eliminar
    [Arguments]    ${nombre_grupo}
    Filtrar Grupo Por Nombre    ${nombre_grupo}
    Hacer Click En Elemento    ${REMOVER_GRUPO_BUTTON}

Eliminar Grupo
    [Documentation]    Elimina el grupo seleccionado
    Run Keyword And Ignore Error    Hacer Click En Elemento    ${REMOVER_GRUPO_BUTTON}

Verificar Grupo Eliminado
    [Documentation]    Verifica que el grupo fue eliminado exitosamente
    Sleep    2s
    Verificar Texto En Página    ¡Registro eliminado exitosamente!

Filtrar Grupo Por Nombre
    [Documentation]    Filtra la lista de grupos por nombre
    [Arguments]    ${nombre_grupo}
    Ingresar Texto    ${NOMBRE_GRUPO_FIELD}    ${nombre_grupo}
    Sleep    1s 