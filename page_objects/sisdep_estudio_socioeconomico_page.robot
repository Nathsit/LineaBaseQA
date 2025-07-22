*** Settings ***
Documentation     Page Object para la sección de Estudio Socioeconómico en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# TODO: Agregar selectores reales cuando el usuario los proporcione
${MENU_PERSONAS}                xpath://div[@role='menuitem' and .//span[text()='Social']]
${SUBMENU_VISITAS_ASIGNADAS}    xpath://a[@href='/sisdep/social/visitas-asignadas']
${FILTRO_ANIO_INPUT}    xpath://span[@class='ant-select-selection-item' and @title='2025']
${FILTRO_ANIO_OPCION_2025}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='2025']
${FILTRO_MES_INPUT}    xpath://span[@class='ant-select-selection-item' and @title='jul.']
${FILTRO_MES_OPCION_JUL}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='jul.']
${DIA_ESTUDIO_CALENDARIO}    xpath://div[contains(@class,'ant-picker-calendar-date-content') and .//span[@class='ant-badge BleNtNoI']]
${DETALLES_ESTUDIO_BUTTON}    xpath://button[.//span[text()='Actualización -'] and .//span[text()='Detalles']]
${GUARDAR_ESTUDIO_BUTTON}    xpath://button[@type='button' and .//span[text()='Guardar']]
${MENSAJE_EXITO_ACTUALIZACION}    ¡Registro actualizado exitosamente!
${DIA_ESTUDIO_CALENDARIO_PDF}    xpath://div[contains(@class,'ant-picker-calendar-date-content') and .//span[@role='img' and @aria-label='file-exclamation']]
${BOTON_PDF}    xpath://button[.//span[@role='img' and @aria-label='file-pdf'] and .//span[contains(text(),'Concepto socioeconómico FO-GGOL-016')]]
${BOTON_CERRAR_MODAL}    xpath://span[contains(@class,'ant-modal-close-x')]
*** Keywords ***
Ir A Seccion Estudio Socioeconomico
    [Documentation]    Navega al menú Social > Visitas domiciliarias asignadas y verifica el título
    Hacer Click En Elemento    ${MENU_PERSONAS}
    Sleep    1s
    Hacer Click En Elemento    ${SUBMENU_VISITAS_ASIGNADAS}
    Sleep    2s
    Reload Page    

Seleccionar Visita Asignada
    [Arguments]    ${VISITA}
    [Documentation]    Selecciona la visita asignada por algún identificador (ajustar selector)
    # TODO: Implementar selección de la visita

Elegir Causal Estudio
    [Arguments]    ${CAUSAL}
    [Documentation]    Selecciona el causal del estudio socioeconómico
    # TODO: Implementar selección del causal

Completar Formularios Estudio
    [Arguments]    ${DATOS}
    [Documentation]    Completa todos los formularios requeridos del estudio
    # TODO: Implementar llenado de formularios

Hacer Click En Guardar Estudio
    [Documentation]    Hace clic en el botón Guardar del estudio socioeconómico
    # TODO: Implementar click en guardar

Verificar Creacion Estudio Exitosa
    [Documentation]    Verifica que el estudio socioeconómico fue creado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ACTUALIZACION} 

Firmar Estudio Socioeconomico
    [Documentation]    Hace clic en el botón Firmar del estudio socioeconómico
    # TODO: Implementar click en firmar

Verificar Estudio Firmado
    [Documentation]    Verifica que el estado del estudio socioeconómico es 'Firmado'
    # TODO: Implementar verificación de estado

Generar PDF Estudio Socioeconomico
    [Documentation]    Hace clic en el botón PDF del estudio socioeconómico
    Hacer Click En Elemento    ${DIA_ESTUDIO_CALENDARIO_PDF}
    Sleep    1s
    Hacer Click En Elemento    ${DETALLES_ESTUDIO_BUTTON}
    Sleep    2s
    Hacer Click En Elemento    ${BOTON_PDF}
    Sleep    2s
     

Verificar PDF Estudio Generado
    [Documentation]    Verifica que el PDF del estudio socioeconómico fue generado y mostrado
    # TODO: Implementar verificación de PDF 

Filtrar Estudio Por Fecha
    [Arguments]    ${ANIO}    ${MES}
    [Documentation]    Aplica el filtro de año y mes en la sección de estudio socioeconómico
    Hacer Click En Elemento    ${FILTRO_ANIO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${ANIO}']
    Sleep    1s
    Hacer Click En Elemento    ${FILTRO_MES_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${MES}']
    Sleep    1s

Seleccionar Estudio Socioeconomico En Calendario
    [Documentation]    Selecciona el día en el calendario y abre el estudio socioeconómico
    Hacer Click En Elemento    ${DIA_ESTUDIO_CALENDARIO}
    Sleep    1s
    Hacer Click En Elemento    ${DETALLES_ESTUDIO_BUTTON}
    Sleep    2s 

Guardar Formularios Estudio Varias Veces
    [Documentation]    Hace clic 7 veces en el botón Guardar y espera el mensaje de éxito
    FOR    ${i}    IN RANGE    7
        Hacer Click En Elemento    ${GUARDAR_ESTUDIO_BUTTON}
        Sleep    1s
    END