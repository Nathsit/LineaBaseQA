*** Settings ***
Documentation     Page Object para la gestión de usuarios en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Locators de la sección de usuarios
${MENU_ADMINISTRACION}         xpath://div[@role='menuitem' and .//span[text()='Administracion']]
${USUARIOS_LINK}               xpath://a[@href='/sisdep/administracion/usuarios' and text()='Usuarios']
${USUARIOS_SECTION_TITLE}      xpath://h1[@class='ant-typography ant-typography-ellipsis ant-typography-single-line ant-typography-ellipsis-single-line _aZcl1wH'][text()='Administración - Usuarios']
${AGREGAR_USUARIO_BUTTON}      xpath://button[@aria-label='Nuevo usuario' and .//span[text()='Nuevo usuario']]
${FORM_NOMBRE}                 css:#nombre
${FORM_APELLIDO}               css:#apellido
${FORM_TIPO_DOCUMENTO}         css:#idTipoDocumento
${FORM_DOCUMENTO}              css:#identificacion
${FORM_GRUPO}                  css:#idGrupo
${FORM_EMAIL}                  css:#email
${FILTRO_DOCUMENTO}            css:#identificacion
${FORM_GUARDAR_BUTTON}         xpath://button[.//span[@aria-label='save'] and .//span[text()='Guardar']]
${USUARIOS_GRID}               xpath://div[contains(@class, 'ant-row') or contains(@class, 'grid')]
${USUARIO_CARD}                xpath://div[contains(@class, 'card') or contains(@class, 'ant-card')]
${DETALLES_BUTTON}             xpath://button[@aria-label='Detalles' and .//span[text()='Detalles']]
${REMOVER_BUTTON}              xpath://button[@aria-label='Remover' and .//span[text()='Remover']]
${CONFIRMAR_REMOVER_BUTTON}    xpath://button[.//span[text()='Sí, eliminar']]

# Mensajes esperados
${USUARIO_CREADO_MSG}          Usuario creado exitosamente
${USUARIO_ACTUALIZADO_MSG}     Usuario actualizado exitosamente
${USUARIO_ELIMINADO_MSG}       Usuario eliminado exitosamente

*** Keywords ***
Deshabilitar Elementos Superpuestos
    [Documentation]    Deshabilita elementos que pueden estar interceptando los clicks
    Execute JavaScript    document.querySelectorAll('.ant-modal-wrap').forEach(el => el.style.display = 'none');
    Execute JavaScript    document.querySelectorAll('.ant-select-dropdown').forEach(el => el.style.display = 'none');
    Execute JavaScript    document.querySelectorAll('.ant-page-header-content').forEach(el => el.style.pointerEvents = 'none');
    Sleep    1s

Llenar Campo Con JavaScript
    [Documentation]    Llena un campo usando JavaScript para evitar problemas de interceptación
    [Arguments]    ${locator}    ${valor}
    ${id}=    Set Variable    ${locator.replace('id=', '')}
    Execute JavaScript    document.getElementById('${id}').value = '${valor}'
    Sleep    0.5s

Seleccionar Opcion Dropdown
    [Documentation]    Selecciona una opción específica en un campo dropdown
    [Arguments]    ${locator}    ${valor}
    # Usar Input Text directamente para seleccionar la opción específica
    Ingresar Texto    ${locator}    ${valor}
    Sleep    1s

Ir A Seccion Usuarios
    [Documentation]    Navega a la sección de administración de usuarios
    Hacer Click En Elemento    ${MENU_ADMINISTRACION}
    Hacer Click En Elemento    ${USUARIOS_LINK}
    Verificar Elemento Presente    ${USUARIOS_SECTION_TITLE}

Agregar Nuevo Usuario
    [Documentation]    Agrega un nuevo usuario llenando el formulario completo
    [Arguments]    ${nombre}    ${apellido}    ${tipo_documento}    ${documento}    ${grupo}    ${email}
    Hacer Click En Elemento    ${AGREGAR_USUARIO_BUTTON}
    # Esperar a que el modal se cargue completamente
    Sleep    2s
    Ingresar Texto    ${FORM_NOMBRE}         ${nombre}
    Ingresar Texto    ${FORM_APELLIDO}       ${apellido}
    Seleccionar Opcion Dropdown    ${FORM_TIPO_DOCUMENTO}    1
    Ingresar Texto    ${FORM_DOCUMENTO}      ${documento}
    Seleccionar Opcion Dropdown    ${FORM_GRUPO}    1
    Ingresar Texto    ${FORM_EMAIL}          ${email}
    Hacer Click En Elemento    ${FORM_GUARDAR_BUTTON}

Actualizar Usuario
    [Documentation]    Actualiza la información de un usuario existente
    [Arguments]    ${nombre_nuevo}    ${apellido_nuevo}    ${tipo_documento}    ${documento}    ${grupo}    ${email}
    Hacer Click En Elemento    ${DETALLES_BUTTON}
    # Esperar a que el modal se cargue completamente
    Sleep    2s
    Ingresar Texto    ${FORM_NOMBRE}         ${nombre_nuevo}
    Ingresar Texto    ${FORM_APELLIDO}       ${apellido_nuevo}
    Seleccionar Opcion Dropdown    ${FORM_TIPO_DOCUMENTO}    1
    Ingresar Texto    ${FORM_DOCUMENTO}      ${documento}
    Seleccionar Opcion Dropdown    ${FORM_GRUPO}    1
    Ingresar Texto    ${FORM_EMAIL}          ${email}
    Hacer Click En Elemento    ${FORM_GUARDAR_BUTTON}

Eliminar Usuario
    [Documentation]    Elimina un usuario existente
    Hacer Click En Elemento    ${REMOVER_BUTTON}
    Sleep    2s
    Hacer Click En Elemento    ${CONFIRMAR_REMOVER_BUTTON}

Verificar Usuario Eliminado
    [Documentation]    Verifica que el usuario fue eliminado exitosamente
    Sleep    2s
    Verificar Texto En Página    Usuario eliminado exitosamente

Seleccionar Usuario En Lista
    [Documentation]    Selecciona un usuario específico en la lista de tarjetas
    [Arguments]    ${email}
    ${usuario_card}=    Set Variable    xpath://div[contains(@class, 'card') or contains(@class, 'ant-card')][.//text()[contains(., '${email}')]]
    Hacer Click En Elemento    ${usuario_card}

Verificar Usuario En Lista
    [Documentation]    Verifica que un usuario esté presente en la lista de tarjetas
    [Arguments]    ${email}    ${nombre}=${EMPTY}
    ${usuario_card}=    Set Variable    xpath://div[contains(@class, 'card') or contains(@class, 'ant-card')][.//text()[contains(., '${email}')]]
    Verificar Elemento Presente    ${usuario_card}
    IF    '${nombre}' != '${EMPTY}'
        Verificar Texto En Página    ${nombre}
    END

Verificar Usuario No En Lista
    [Documentation]    Verifica que un usuario NO esté presente en la lista de tarjetas
    [Arguments]    ${email}
    ${usuario_card}=    Set Variable    xpath://div[contains(@class, 'card') or contains(@class, 'ant-card')][.//text()[contains(., '${email}')]]
    Element Should Not Be Visible    ${usuario_card}

Verificar Mensaje Exitoso
    [Documentation]    Verifica que se muestre un mensaje de éxito
    [Arguments]    ${mensaje}
    Verificar Texto En Página    ${mensaje}

Limpiar Formulario Usuario
    [Documentation]    Limpia los campos del formulario de usuario
    Limpiar Campo    ${FORM_NOMBRE}
    Limpiar Campo    ${FORM_EMAIL}

Verificar Elementos De Usuarios Presentes
    [Documentation]    Verifica que todos los elementos de la página de usuarios estén presentes
    Verificar Elemento Presente    ${USUARIOS_SECTION_TITLE}
    Verificar Elemento Presente    ${AGREGAR_USUARIO_BUTTON}
    Verificar Elemento Presente    ${USUARIOS_GRID} 

Llenar Formulario Con Tab
    [Documentation]    Llena el formulario usando Tab para navegar entre campos
    [Arguments]    ${nombre}    ${apellido}    ${documento}    ${email}
    # Hacer click en el primer campo y usar Tab para navegar
    Hacer Click En Elemento    ${FORM_NOMBRE}
    Press Keys    ${FORM_NOMBRE}    ${nombre}
    Press Keys    None    TAB
    Press Keys    None    ${apellido}
    Press Keys    None    TAB
    Press Keys    None    TAB  # Saltar tipo documento
    Press Keys    None    ${documento}
    Press Keys    None    TAB
    Press Keys    None    TAB  # Saltar grupo
    Press Keys    None    ${email} 

Llenar Campo Con Coordenadas
    [Documentation]    Llena un campo haciendo click en coordenadas específicas usando XPath
    [Arguments]    ${locator}    ${valor}
    # Obtener la posición del elemento usando XPath y hacer click en el centro
    ${element}=    Get WebElement    ${locator}
    ${location}=    Call Method    ${element}    location
    ${size}=    Call Method    ${element}    size
    ${x}=    Evaluate    ${location['x']} + ${size['width']} / 2
    ${y}=    Evaluate    ${location['y']} + ${size['height']} / 2
    Click Element At Coordinates    ${locator}    ${x}    ${y}
    Input Text    ${locator}    ${valor} 

Ingresar Texto En Filtro Documento
    [Documentation]    Ingresa texto en el filtro de documento
    [Arguments]    ${documento}
    Sleep    3s
    Verificar Elemento Presente    ${FILTRO_DOCUMENTO}
    Ingresar Texto    ${FILTRO_DOCUMENTO}    ${documento}
    Sleep    2s

Seleccionar Usuario Por Documento
    [Documentation]    Selecciona un usuario específico por su número de documento
    [Arguments]    ${documento}
    Sleep    2s
    ${usuario_card}=    Set Variable    xpath://div[contains(@class, 'card') or contains(@class, 'ant-card')][.//text()[contains(., '${documento}')]]
    Verificar Elemento Presente    ${usuario_card}
    Hacer Click En Elemento    ${usuario_card}

Editar Solo Email Usuario
    [Documentation]    Edita solo el campo de email del usuario
    [Arguments]    ${nuevo_email}
    Sleep    2s
    Hacer Click En Elemento    ${DETALLES_BUTTON}
    Sleep    3s
    Verificar Elemento Presente    ${FORM_EMAIL}
    Limpiar Campo    ${FORM_EMAIL}
    Sleep    1s
    Ingresar Texto    ${FORM_EMAIL}    ${nuevo_email}
    Sleep    1s
    Hacer Click En Elemento    ${FORM_GUARDAR_BUTTON}

Verificar Email Actualizado
    [Documentation]    Verifica que el email del usuario se actualizó correctamente
    Sleep    2s
    Verificar Texto En Página    ¡Registro actualizado exitosamente! 

Ingresar Texto En Campos Vacios
    [Documentation]    Verifica que se muestre un mensaje de error cuando se intenta guardar un usuario con campos vacíos
    Hacer Click En Elemento    ${FORM_GUARDAR_BUTTON}
    Verificar Texto En Página    El campo es obligatorio


    