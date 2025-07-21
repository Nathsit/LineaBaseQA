*** Settings ***
Documentation     Page Object para la sección de Asignación de Visitas Domiciliarias en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Navegación
${MENU_REGULACIONES}           xpath://span[@class='ant-menu-title-content' and text()='Regulaciones']
${SUBMENU_ASIGNACION_VISITAS}  xpath://a[@href='/sisdep/regulaciones/asignacion-visitas' and text()='Asignación de visitas domiciliarias']
${SECCION_VISITAS_TITLE}       xpath://h1[text()='Regulaciones - Asignación de visitas domiciliarias']

# Botones y campos principales
${NUEVA_VISITA_BUTTON}         xpath://button[@aria-label='Nueva visita' and .//span[text()='Nueva visita']]
${BUSCAR_VENTERO_INPUT}        id=documento
${BUSCAR_VENTERO_BUTTON}       xpath://button[.//span[text()='Buscar']]
${FORM_VISITA}                 # TODO: Selector del formulario de visita
${GUARDAR_VISITA_BUTTON}       xpath://button[.//span[text()='Guardar']]
${DETALLES_VISITA_BUTTON}      # TODO: Selector del botón Detalles de visita
${ACTUALIZAR_VISITA_BUTTON}    # TODO: Selector del botón Actualizar visita
${ELIMINAR_VISITA_BUTTON}      # TODO: Selector del botón Eliminar visita
${CONFIRMAR_ELIMINAR_BUTTON}   # TODO: Selector del botón Confirmar eliminación
${VISITADOR_DROPDOWN}          id=idVisitador
${VISITADOR_OPCION}            xpath://div[@class='ant-select-item-option-content' and text()='Administrador DEL SISTEMA']
${TIPO_VISITA_DROPDOWN}        id=idTipo
${TIPO_VISITA_OPCION}          xpath://div[@class='ant-select-item-option-content' and text()='Actualización']
${VEHICULO_DROPDOWN}           id=idVehiculo
${VEHICULO_OPCION}             xpath://div[@class='ant-select-item-option-content' and text()='RJZ672']
${FRANJA_HORARIA_DROPDOWN}     id=idFranja
${FRANJA_HORARIA_OPCION}       xpath://div[@class='ant-select-item-option-content' and text()='AM']
${FECHA_VISITA_INPUT}          id=fechaVisita
${FECHA_VISITA_TODAY_BUTTON}   xpath://a[contains(@class,'ant-picker-today-btn') and text()='Today']
${MENSAJE_EXITO_CREACION}      ¡Registro creado exitosamente!
${FECHA_EJECUCION_INPUT}        id=fechaEjecucion
${FECHA_EJECUCION_HASTA_INPUT}  xpath://input[@placeholder='Hasta']
${VISITADOR_ACTUALIZAR_DROPDOWN}    id=visitador
${VISITADOR_ACTUALIZAR_OPCION}      xpath://div[@class='ant-select-item-option-content' and text()='Administrador DEL SISTEMA']
${DETALLES_VISITA_BUTTON}       xpath://button[@aria-label='Detalles' and .//span[text()='Detalles']]
${DETALLES_VISITA_BUTTON_PRIMERO}    xpath:(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]
${ACTUALIZAR_VISITA_BUTTON}     xpath://button[.//span[text()='Actualizar']]
${ACTUALIZAR_VISITA_BUTTON_PRIMERO}     xpath:(//button[.//span[text()='Actualizar']])[1]
${MENSAJE_EXITO_ACTUALIZACION}  ¡Registro actualizado exitosamente!
${ELIMINAR_VISITA_BUTTON_PRIMERO}    xpath:(//button[@aria-label='Remover' and .//span[text()='Remover']])[1]
${CONFIRMAR_ELIMINAR_VISITA_BUTTON}  xpath://button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]
${MENSAJE_EXITO_ELIMINACION}         ¡Registro eliminado exitosamente!

*** Keywords ***
El Usuario Esta En Seccion Asignacion Visitas
    [Documentation]    Navega a la sección de Asignación de Visitas
    Hacer Click En Elemento    ${MENU_REGULACIONES}
    Sleep    1s
    Hacer Click En Elemento    ${SUBMENU_ASIGNACION_VISITAS}
    Sleep    2s
    Reload Page
    Verificar Elemento Presente    ${SECCION_VISITAS_TITLE}

Hacer Click En Nueva Visita
    [Documentation]    Hace clic en el botón Nueva visita
    Hacer Click En Elemento    ${NUEVA_VISITA_BUTTON}
    Sleep    2s

Buscar Ventero Por Documento En Visitas
    [Arguments]    ${documento}
    [Documentation]    Busca un ventero por su número de documento en la sección de visitas
    Ingresar Texto    ${BUSCAR_VENTERO_INPUT}    ${documento}
    Sleep    1s
    Hacer Click En Elemento    ${BUSCAR_VENTERO_BUTTON}
    Sleep    2s

Completar Formulario Visita
    [Arguments]    ${VISITADOR}    ${TIPO_VISITA}    ${VEHICULO}    ${FECHA}    ${FRANJA}
    [Documentation]    Completa el formulario de visita con los datos proporcionados
    # Visitador
    Hacer Click En Elemento    ${VISITADOR_DROPDOWN}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content' and text()='${VISITADOR}']
    Sleep    1s
    # Tipo de visita
    Hacer Click En Elemento    ${TIPO_VISITA_DROPDOWN}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content' and text()='${TIPO_VISITA}']
    Sleep    1s
    # Vehículo
    Hacer Click En Elemento    ${VEHICULO_DROPDOWN}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content' and text()='${VEHICULO}']
    Sleep    1s
    # Fecha de la visita (habilitar campo y seleccionar 'Hoy')
    Execute JavaScript    document.getElementById('fechaVisita').removeAttribute('readonly')
    Hacer Click En Elemento    ${FECHA_VISITA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    ${FECHA_VISITA_TODAY_BUTTON}
    Sleep    1s
    # Franja horaria
    Hacer Click En Elemento    ${FRANJA_HORARIA_DROPDOWN}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content' and text()='${FRANJA}']
    Sleep    1s

Hacer Click En Guardar Visita
    [Documentation]    Hace clic en el botón Guardar visita
    Hacer Click En Elemento    ${GUARDAR_VISITA_BUTTON}
    Sleep    2s

Hacer Click En Detalles Visita
    [Documentation]    Hace clic en el primer botón Detalles de la lista de visitas
    Esperar Elemento Clickable    ${DETALLES_VISITA_BUTTON_PRIMERO}
    Hacer Click En Elemento       ${DETALLES_VISITA_BUTTON_PRIMERO}
    Sleep    2s

Actualizar Datos Visita
    [Arguments]    ${FECHA_DESDE}    ${FECHA_HASTA}    ${VISITADOR}
    [Documentation]    Actualiza los datos de la visita asignada
    # Fecha de ejecución (Desde)
    Execute JavaScript    document.getElementById('fechaEjecucion').removeAttribute('readonly')
    Ingresar Texto    ${FECHA_EJECUCION_INPUT}    ${FECHA_DESDE}
    Sleep    1s
    # Fecha de ejecución (Hasta)
    Execute JavaScript    document.evaluate("//input[@placeholder='Hasta']",document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.removeAttribute('readonly')
    Ingresar Texto    ${FECHA_EJECUCION_HASTA_INPUT}    ${FECHA_HASTA}
    Sleep    1s
    # Visitador
    Hacer Click En Elemento    ${VISITADOR_ACTUALIZAR_DROPDOWN}
    Sleep    1s
    Hacer Click En Elemento    ${VISITADOR_ACTUALIZAR_OPCION}
    Sleep    1s

Hacer Click En Actualizar Visita
    [Documentation]    Hace clic en el primer botón Actualizar visita
    Esperar Elemento Clickable    ${ACTUALIZAR_VISITA_BUTTON_PRIMERO}
    Hacer Click En Elemento       ${ACTUALIZAR_VISITA_BUTTON_PRIMERO}
    Sleep    2s

Verificar Actualizacion Visita Exitosa
    [Documentation]    Verifica que la visita fue actualizada exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ACTUALIZACION}

Hacer Click En Eliminar Visita
    [Documentation]    Hace clic en el primer botón Remover de la lista de visitas
    Esperar Elemento Clickable    ${ELIMINAR_VISITA_BUTTON_PRIMERO}
    Hacer Click En Elemento       ${ELIMINAR_VISITA_BUTTON_PRIMERO}
    Sleep    1s

Confirmar Eliminacion Visita
    [Documentation]    Confirma la eliminación de la visita
    Esperar Elemento Clickable    ${CONFIRMAR_ELIMINAR_VISITA_BUTTON}
    Hacer Click En Elemento       ${CONFIRMAR_ELIMINAR_VISITA_BUTTON}
    Sleep    2s

Verificar Eliminacion Visita Exitosa
    [Documentation]    Verifica que la visita fue eliminada exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ELIMINACION}

Verificar Creacion Visita Exitosa
    [Documentation]    Verifica que la visita fue creada exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_CREACION} 