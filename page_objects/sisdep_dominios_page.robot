*** Settings ***
Documentation     Page Object para la gestión de dominios en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Navegación a Dominios
${ADMINISTRACION_MENU}         xpath://div[@role='menuitem' and .//span[text()='Administracion']]
${DOMINIOS_SUBMENU}           xpath://a[@href='/sisdep/administracion/dominios']

# Formulario de búsqueda de dominio
${NOMBRE_DOMINIO_INPUT}       xpath://input[@role='textbox' and @aria-label='Nombre']
${VER_DOMINIOS_BUTTON}        xpath://button[@aria-label='Ver dominios']

# Paginación
${PAGINA_5_BUTTON}            xpath://a[@rel='nofollow'][text()='5']

# Formulario de valores de dominio
${NUEVO_VALOR_INPUT}          xpath://input[@role='textbox' and @id='descripcion']
${AGREGAR_VALOR_BUTTON}       xpath://button[@aria-label='Agregar dominio']

# Edición de valores
${EDITAR_VALOR_BUTTON}        xpath://button[contains(@class,'editar-valor')]
${ACTUALIZAR_VALOR_BUTTON}    xpath://button[@aria-label='Actualizar dominio']

# Eliminación de valores
${ELIMINAR_VALOR_BUTTON}      xpath://button[@aria-label='Eliminar dominio']

*** Keywords ***
Hacer Login Como Administrador
    [Documentation]    Realiza login como administrador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}

El Administrador Esta En Seccion Dominios
    [Documentation]    Navega a la sección de Administración - Dominios
    Hacer Click En Elemento    ${ADMINISTRACION_MENU}
    Sleep    1s
    Hacer Click En Elemento    ${DOMINIOS_SUBMENU}
    Sleep    2s
    Verificar Elemento Presente    ${NOMBRE_DOMINIO_INPUT}

Selecciona Dominio Especifico
    [Arguments]    ${nombre_dominio}
    [Documentation]    Selecciona un dominio específico de la lista
    Ingresar Texto    ${NOMBRE_DOMINIO_INPUT}    ${nombre_dominio}
    Sleep    1s
    Hacer Click En Elemento    ${VER_DOMINIOS_BUTTON}
    Sleep    2s
    Hacer Click En Elemento    ${PAGINA_5_BUTTON}
    Sleep    2s
    ${DOMINIO_ITEM_LOCATOR}=    Set Variable    xpath://li[@class='ant-list-item'][contains(text(),'Etapa ciclo vital')]
    Hacer Click En Elemento    ${DOMINIO_ITEM_LOCATOR}
    Sleep    2s
    Verificar Elemento Presente    ${NUEVO_VALOR_INPUT}

Ingresa Nuevo Valor En Dominio
    [Arguments]    ${nuevo_valor}
    [Documentation]    Ingresa un nuevo valor en el campo correspondiente
    Ingresar Texto    ${NUEVO_VALOR_INPUT}    ${nuevo_valor}

Hace Click En Agregar Valor
    [Documentation]    Hace clic en el botón "Agregar"
    Hacer Click En Elemento    ${AGREGAR_VALOR_BUTTON}
    Sleep    2s

El Sistema Anade El Nuevo Valor Al Dominio
    [Documentation]    Verifica que el nuevo valor se agregó correctamente
    Verificar Texto En Página    ¡Registro creado exitosamente!

Modifica Descripcion De Valor Existente
    [Arguments]    ${valor_existente}
    [Documentation]    Modifica la descripción de un valor existente
    ${VALOR_ITEM_LOCATOR}=    Set Variable    xpath://div[contains(@class,'valor-item')][contains(text(),'${valor_existente}')]
    Hacer Click En Elemento    ${VALOR_ITEM_LOCATOR}
    Sleep    1s
    Hacer Click En Elemento    ${EDITAR_VALOR_BUTTON}
    Sleep    1s

Hace Click En Actualizar Valor
    [Documentation]    Hace clic en el botón "Actualizar"
    Hacer Click En Elemento    ${ACTUALIZAR_VALOR_BUTTON}
    Sleep    2s

El Sistema Guarda Los Cambios Del Valor
    [Documentation]    Verifica que los cambios se guardaron correctamente
    Verificar Texto En Página    ¡Registro actualizado exitosamente!

Hace Click En Eliminar Valor
    [Documentation]    Hace clic en el botón "Eliminar"
    Hacer Click En Elemento    ${ELIMINAR_VALOR_BUTTON}
    Sleep    2s

El Sistema Elimina El Valor Del Dominio
    [Documentation]    Verifica que el valor se eliminó correctamente
    Verificar Texto En Página    ¡Registro eliminado exitosamente! 