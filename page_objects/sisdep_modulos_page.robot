*** Settings ***
Documentation     Page Object para la sección de Gestión de Módulos en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Navegación
${MENU_REGULACIONES}           xpath://span[@class='ant-menu-title-content' and text()='Regulaciones']
${SUBMENU_MODULOS}             xpath://a[@href='/sisdep/regulaciones/modulos']
${SECCION_MODULOS_TITLE}       xpath://h1[contains(@class, 'ant-typography') and contains(text(), 'Regulaciones - Módulos')]

# Botones y campos principales
${AGREGAR_MODULO_BUTTON}       xpath://button[@aria-label='Agregar' and contains(@class, 'ant-btn-primary')]
${NOMBRE_MODULO_INPUT}         # TODO: Selector del campo Nombre
${DESCRIPCION_MODULO_INPUT}    # TODO: Selector del campo Descripción
${TENENCIA_PROPIEDAD_INPUT}           xpath://input[@id='idTenenciaPropiedad']
${TENENCIA_PROPIEDAD_OPCION_PROPIA}   xpath://div[contains(@class,'ant-select-item-option-content') and text()='Propia']
${ESTADO_INPUT}                       xpath://input[@id='idEstado']
${ESTADO_OPCION_BUENO}                xpath://div[contains(@class,'ant-select-item-option-content') and text()='Bueno']
${SWITCH_SERVICIOS_PUBLICOS}          xpath://button[@id='tieneServiciosPublicos']
${SWITCH_USA_PIPETA}                  xpath://button[@id='usaPipeta']
${FONDO_INPUT}                        xpath://input[@id='fondo']
${FRENTE_INPUT}                       xpath://input[@id='frente']
${ALTO_INPUT}                         xpath://input[@id='alto']
${TIPO_MODULO_INPUT}                  xpath://input[@id='idTipoModulo']
${TIPO_MODULO_OPCION_ORIENTAL}        xpath://div[contains(@class,'ant-select-item-option-content') and text()='Oriental']
${TIPO_OTRO_MODULO_INPUT}             xpath://input[@id='idTipoOtroModulo']
${TIPO_OTRO_MODULO_OPCION_TIPO1}      xpath://div[contains(@class,'ant-select-item-option-content') and text()='Tipo 1']
${SECTOR_MODULO_INPUT}                xpath://input[@id='idSectorModulo']
${SECTOR_MODULO_OPCION_ESTADIO}       xpath://div[contains(@class,'ant-select-item-option-content') and text()='Estadio']
${GUARDAR_MODULO_BUTTON}              xpath://button[contains(@class,'ant-btn-primary') and .//span[text()='Guardar']]
${DETALLES_MODULO_BUTTON}      # TODO: Selector del botón Detalles
${DETALLES_MODULO_BUTTON_PRIMERO}    xpath:(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]
${ELIMINAR_MODULO_BUTTON}      # TODO: Selector del botón Eliminar
${CONFIRMAR_ELIMINAR_BUTTON}   # TODO: Selector del botón Confirmar eliminación
${MENSAJE_EXITO_CREACION}      ¡Registro creado exitosamente!
${FILTRO_SERIAL_INPUT}                xpath://input[@id='serial']
${DETALLES_MODULO_BUTTON}             xpath://button[@aria-label='Detalles' and .//span[text()='Detalles']]
${MENSAJE_EXITO_ACTUALIZACION}        ¡Registro actualizado exitosamente!
${ELIMINAR_MODULO_BUTTON_PRIMERO}    xpath:(//button[@aria-label='Eliminar' and .//span[text()='Eliminar']])[1]
${MENSAJE_EXITO_ELIMINACION}         ¡Registro eliminado exitosamente!

*** Keywords ***
El Usuario Esta En Seccion Modulos
    [Documentation]    Navega a la sección de Módulos
    Hacer Click En Elemento    ${MENU_REGULACIONES}
    Sleep    1s
    Hacer Click En Elemento    ${SUBMENU_MODULOS}
    Sleep    2s
    Reload Page
    Verificar Elemento Presente    ${SECCION_MODULOS_TITLE}

Hacer Click En Agregar Modulo
    [Documentation]    Hace clic en el botón Agregar módulo
    Hacer Click En Elemento    ${AGREGAR_MODULO_BUTTON}
    Sleep    2s

Completar Formulario Modulo
    [Arguments]    ${TENENCIA}    ${ESTADO}    ${FONDO}    ${FRENTE}    ${ALTO}    ${TIPO_MODULO}    ${TIPO_OTRO_MODULO}    ${SECTOR_MODULO}
    [Documentation]    Completa el formulario de módulo con los datos proporcionados
    # Tenencia de la propiedad
    Hacer Click En Elemento    ${TENENCIA_PROPIEDAD_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TENENCIA}']
    Sleep    1s
    # Estado
    Hacer Click En Elemento    ${ESTADO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${ESTADO}']
    Sleep    1s
    # Fondo
    Ingresar Texto    ${FONDO_INPUT}    ${FONDO}
    Sleep    1s
    # Frente
    Ingresar Texto    ${FRENTE_INPUT}    ${FRENTE}
    Sleep    1s
    # Alto
    Ingresar Texto    ${ALTO_INPUT}    ${ALTO}
    Sleep    1s
   
Hacer Click En Guardar Modulo
    [Documentation]    Hace clic en el botón Guardar módulo
    Hacer Click En Elemento    ${GUARDAR_MODULO_BUTTON}
    Sleep    2s

Verificar Creacion Modulo Exitosa
    [Documentation]    Verifica que el módulo fue creado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_CREACION} 

Filtrar Modulo Por Serial
    [Arguments]    ${SERIAL}
    [Documentation]    Ingresa el serial en el filtro para buscar el módulo
    Ingresar Texto    ${FILTRO_SERIAL_INPUT}    ${SERIAL}
    Sleep    1s

Hacer Click En Detalles Modulo
    [Documentation]    Hace clic en el primer botón Detalles del módulo filtrado
    Hacer Click En Elemento    ${DETALLES_MODULO_BUTTON_PRIMERO}
    Sleep    2s


Verificar Actualizacion Modulo Exitosa
    [Documentation]    Verifica que el módulo fue actualizado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ACTUALIZACION} 

Hacer Click En Eliminar Modulo
    [Documentation]    Hace clic en el primer botón Eliminar del módulo filtrado
    Hacer Click En Elemento    ${ELIMINAR_MODULO_BUTTON_PRIMERO}
    Sleep    1s

Verificar Eliminacion Modulo Exitosa
    [Documentation]    Verifica que el módulo fue eliminado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ELIMINACION} 