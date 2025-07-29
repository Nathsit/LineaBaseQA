*** Settings ***
Documentation     Page Object para la sección de Gestión de Ofertas Institucionales en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
${MENU_PERSONAS}                xpath://div[@role='menuitem' and .//span[text()='Social']]
${SUBMENU_OFERTAS_INSTITUCIONALES}    xpath://a[@href='/sisdep/social/ofertas-institucionales']
${SECCION_OFERTAS_TITLE}    xpath://h1[contains(@class,'ant-typography') and text()='Social - Ofertas Institucionales']
${AGREGAR_OFERTA_BUTTON}    xpath://button[@aria-label='Agregar' and .//span[text()='Agregar']]
${FECHA_EJECUCION_INPUT}    xpath://div[contains(@class,'ant-modal')]//input[@id='fechaEjecucion']
${TIPO_OFERTA_INPUT}    xpath://input[@id='idTipo']
${TIPO_OFERTA_OPCION_SENA}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='sena dadad']
${CONVENIO_INPUT}    xpath://input[@id='idConvenio']
${CONVENIO_OPCION_SALUD}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Secretaria de Salud']
${GUARDAR_OFERTA_BUTTON}    xpath://button[@type='button' and .//span[text()='Guardar']]
${MENSAJE_EXITO_CREACION}    Registro creado exitosamente
${FILTRO_TIPO_OFERTA_INPUT}    xpath://input[@id='tipoOferta']
${FILTRO_TIPO_OFERTA_OPCION_SENA}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='sena dadad']
${DETALLES_OFERTA_BUTTON}    xpath://button[@aria-label='Detalles' and .//span[text()='Detalles']]
${AGREGAR_PARTICIPANTE_BUTTON}    xpath://button[@aria-label='Agregar' and .//span[text()='Agregar']]
${ELIMINAR_OFERTA_BUTTON}    xpath://button[@aria-label='Remover' and .//span[text()='Remover']]
${DOCUMENTO_PARTICIPANTE_INPUT}    xpath://input[@id='documento']
${BUSCAR_PARTICIPANTE_BUTTON}    xpath://button[.//span[@role='img' and @aria-label='search'] and .//span[text()='Buscar']]
${TIPO_CONOCIMIENTO_INPUT}    xpath://input[@id='idTipoConocimiento']
${TIPO_CONOCIMIENTO_OPCION_ATENCION}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Atención en la oficina']
${GUARDAR_PARTICIPANTE_BUTTON}    xpath://button[@type='button' and .//span[@role='img' and @aria-label='save'] and .//span[text()='Guardar']]
${MENSAJE_EXITO_PARTICIPANTE_AGREGADO}    ¡Registro creado exitosamente!
${REMOVER_PARTICIPANTE_BUTTON}    xpath://button[@aria-label='Remover' and .//span[text()='Remover']]
${CONFIRMAR_ELIMINAR_PARTICIPANTE_BUTTON}    xpath://button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]
${MENSAJE_EXITO_PARTICIPANTE_ELIMINADO}    ¡Registro eliminado exitosamente!

*** Keywords ***
Ir A Seccion Ofertas Institucionales
    [Documentation]    Navega a la sección de Ofertas Institucionales
    Hacer Click En Elemento    ${MENU_PERSONAS}
    Sleep    1s
    Hacer Click En Elemento    ${SUBMENU_OFERTAS_INSTITUCIONALES}
    Sleep    2s
    Verificar Elemento Presente    ${SECCION_OFERTAS_TITLE}

Hacer Click En Agregar Oferta
    [Documentation]    Hace clic en el botón Agregar oferta
    Hacer Click En Elemento    ${AGREGAR_OFERTA_BUTTON}
    Sleep    2s

Completar Formulario Oferta
    [Arguments]    ${FECHA_EJECUCION}    ${TIPO_OFERTA}    ${CONVENIO}
    [Documentation]    Completa el formulario de oferta institucional
    Hacer Click En Elemento    ${TIPO_OFERTA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_OFERTA}']
    Hacer Click En Elemento    ${CONVENIO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${CONVENIO}']
    Sleep    1s

Hacer Click En Guardar Oferta
    [Documentation]    Hace clic en el botón Guardar oferta
    Hacer Click En Elemento    ${GUARDAR_OFERTA_BUTTON}
    Sleep    2s

Verificar Creacion Oferta Exitosa
    [Documentation]    Verifica que la oferta institucional fue creada exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_CREACION}

Agregar Participante A Oferta
    [Arguments]    ${TIPO_OFERTA}    ${DOCUMENTO}    ${TIPO_CONOCIMIENTO}
    [Documentation]    Agrega un participante a una oferta institucional
    Hacer Click En Elemento    ${FILTRO_TIPO_OFERTA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_OFERTA}']
    Hacer Click En Elemento    ${DETALLES_OFERTA_BUTTON}
    Sleep    1s
    Hacer Click En Elemento    ${AGREGAR_PARTICIPANTE_BUTTON}
    Sleep    1s
    Ingresar Texto    ${DOCUMENTO_PARTICIPANTE_INPUT}    ${DOCUMENTO}
    Hacer Click En Elemento    ${BUSCAR_PARTICIPANTE_BUTTON}
    Sleep    1s
    Hacer Click En Elemento    ${TIPO_CONOCIMIENTO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_CONOCIMIENTO}']
    Hacer Click En Elemento    ${GUARDAR_PARTICIPANTE_BUTTON}
    Sleep    2s

Verificar Participante Agregado
    [Documentation]    Verifica que el participante fue agregado a la oferta
    Verificar Texto En Página    ${MENSAJE_EXITO_PARTICIPANTE_AGREGADO}

Eliminar Participante De Oferta
    [Arguments]    ${TIPO_OFERTA}
    [Documentation]    Elimina un participante de una oferta institucional
    Hacer Click En Elemento    ${FILTRO_TIPO_OFERTA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_OFERTA}']
    Hacer Click En Elemento    ${DETALLES_OFERTA_BUTTON}
    Sleep    1s
    Hacer Click En Elemento    ${REMOVER_PARTICIPANTE_BUTTON}
    Sleep    1s
    Hacer Click En Elemento    ${CONFIRMAR_ELIMINAR_PARTICIPANTE_BUTTON}
    Sleep    2s

Eliminar Oferta con Participantes
    [Arguments]    ${TIPO_OFERTA}
    [Documentation]    Elimina una oferta institucional con participantes
    Hacer Click En Elemento    ${FILTRO_TIPO_OFERTA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_OFERTA}']
    Hacer Click En Elemento    ${ELIMINAR_OFERTA_BUTTON}
    Sleep    1s
    Hacer Click En Elemento    ${CONFIRMAR_ELIMINAR_PARTICIPANTE_BUTTON}
    Sleep    2s
    Verificar Texto En Página  Elemento usado en Evidencias de la oferta

    Sleep    2s
Verificar Participante Eliminado
    [Documentation]    Verifica que el participante fue eliminado de la oferta
    Verificar Texto En Página    ${MENSAJE_EXITO_PARTICIPANTE_ELIMINADO} 