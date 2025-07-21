*** Settings ***
Documentation     Page Object para la gestión de autorizaciones en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
# Navegación a Autorizaciones
${REGULACIONES_MENU}           xpath://span[@class='ant-menu-title-content'][text()='Regulaciones']
${AUTORIZACIONES_SUBMENU}      xpath://a[@href='/sisdep/regulaciones/autorizaciones']
${AUTORIZACIONES_SECTION_TITLE}    xpath://h1[@class='ant-typography ant-typography-ellipsis ant-typography-single-line ant-typography-ellipsis-single-line _aZcl1wH'][text()='Regulaciones - Autorizaciones']

# Búsqueda de ventero
${BUSCAR_VENTERO_INPUT}        xpath://input[@role='textbox' and @aria-label='Documento' and @id='documento']
${BUSCAR_VENTERO_BUTTON}       xpath://button[@type='button' and @class='ant-btn ant-btn-primary'][.//span[text()='Buscar']]

# Botón agregar nueva autorización
${AGREGAR_AUTORIZACION_BUTTON}    xpath://button[@aria-label='Agregar' and @class='ant-btn ant-btn-primary HdMXdtFX']

# Formulario de solicitud de autorización
${FORM_SOLICITUD_AUTORIZACION}    xpath://form[contains(@class,'form-solicitud')]

# Campos del formulario
${RADICADO_MERCURIO_INPUT}     xpath://input[@role='textbox' and @aria-label='Radicado mercurio' and @id='radicadoMercurio']
${TIPO_AUTORIZACION_DROPDOWN}    xpath://input[@id='idMotivoAutorizacion' and @aria-label='Motivo de autorización']
${FECHA_INICIAL_INPUT}         xpath://input[@role='textbox' and @aria-label='Fecha inicial' and @id='fechaInicial']
${ESTADO_DROPDOWN}             id=idEstadoAutorizacion
${DIAS_DROPDOWN}               xpath://div[@class='ant-select ant-select-lg IlERIOp8 ant-select-multiple ant-select-allow-clear ant-select-show-search'][@aria-label='Dias']
${HORA_INICIO_INPUT}           xpath://input[@id='horaInicio' and @class='ant-input-number-input']
${HORA_FIN_INPUT}              xpath://input[@id='horaFin' and @class='ant-input-number-input']

${GUARDAR_SOLICITUD_BUTTON}    xpath://button[@type='button' and @class='ant-btn ant-btn-primary'][.//span[text()='Guardar']]

# Detalles de autorización
${DETALLES_AUTORIZACION}       xpath://div[contains(@class,'detalles-autorizacion')]
${AGREGAR_VISITA_BUTTON}       xpath://button[.//span[text()='Asignar visita domiciliaria']]
${AGREGAR_RESOLUCION_BUTTON}   xpath://button[.//span[text()='Agrega resolución']]

# Formulario de visita administrativa
${FORM_VISITA_ADMINISTRATIVA}  xpath://form[contains(@class,'form-visita')]
${GUARDAR_VISITA_BUTTON}       xpath://button[contains(text(),'Guardar visita')]

# Formulario de resolución
${FORM_RESOLUCION}             xpath://div[@class='ant-modal-header']/div[@class='ant-modal-title' and text()='Agregar resolución']
${NUMERO_RESOLUCION_INPUT}     id=numero
${FECHA_EFECTOS_FISCALES_INPUT}    id=fechaEfectosFiscales
${FECHA_EXPEDICION_INPUT}      id=fechaExpedicion
${GUARDAR_RESOLUCION_BUTTON}   xpath://button[.//span[text()='Guardar']]

# Eliminación de autorización
${ELIMINAR_AUTORIZACION_BUTTON}    xpath://button[@aria-label='Eliminar' and .//span[text()='Eliminar']]
${CONFIRMAR_ELIMINAR_BUTTON}   xpath://button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]

# Reporte Excel
${FILTROS_REPORTE}             xpath://div[contains(@class,'filtros-reporte')]
${BOTON_EXCEL}                 xpath://button[.//span[text()='Excel']]

# Mensajes
${MENSAJE_EXITO}               xpath://div[contains(@class,'mensaje-exito')]
${MENSAJE_ERROR}               xpath://div[contains(@class,'mensaje-error')]

*** Keywords ***
El Usuario Esta En Seccion Autorizaciones
    [Documentation]    Navega a la sección de Autorizaciones
    Hacer Click En Elemento    ${REGULACIONES_MENU}
    Sleep    1s
    Hacer Click En Elemento    ${AUTORIZACIONES_SUBMENU}
    Sleep    2s
    Verificar Elemento Presente    ${AUTORIZACIONES_SECTION_TITLE}

Buscar Ventero Por Documento
    [Arguments]    ${documento}
    [Documentation]    Busca un ventero por su número de documento
    Hacer Click En Elemento    ${AGREGAR_AUTORIZACION_BUTTON}
    Sleep    2s
    Ingresar Texto    ${BUSCAR_VENTERO_INPUT}    ${documento}
    Sleep    1s
    Hacer Click En Elemento    ${BUSCAR_VENTERO_BUTTON}
    Sleep    2s

Completar Datos Solicitud Autorizacion
    [Documentation]    Completa los datos del formulario de solicitud de autorización
    Sleep    2s
    # Completar campo Radicado Mercurio
    Ingresar Texto    ${RADICADO_MERCURIO_INPUT}    ${RADICADO_MERCURIO}
    Sleep    1s
    
    # Seleccionar Tipo de Autorización
    Hacer Click En Elemento    ${TIPO_AUTORIZACION_DROPDOWN}
    Sleep    1s
    # Seleccionar "Nueva autorizacion" de la lista
    ${NUEVA_AUTORIZACION_OPTION}=    Set Variable    xpath://div[@class='ant-select-item-option-content'][text()='Nueva autorizacion']
    Hacer Click En Elemento    ${NUEVA_AUTORIZACION_OPTION}
    Sleep    1s
    
    # Completar Fecha Inicial
    Ingresar Texto    ${FECHA_INICIAL_INPUT}    ${FECHA_INICIAL}
    Sleep    1s
    
    # Seleccionar Estado
    Hacer Click En Elemento    ${ESTADO_DROPDOWN}
    Sleep    1s
    # Seleccionar "En proceso" de la lista
    ${EN_PROCESO_OPTION}=    Set Variable    xpath://div[@class='ant-select-item-option-content'][text()='En proceso']
    Hacer Click En Elemento    ${EN_PROCESO_OPTION}
    Sleep    1s
    
    # Seleccionar Días
    Hacer Click En Elemento    ${DIAS_DROPDOWN}
    Sleep    1s
    # Seleccionar "Lunes" de la lista
    ${LUNES_OPTION}=    Set Variable    xpath://div[@class='ant-select-item-option-content'][text()='Lunes']
    Hacer Click En Elemento    ${LUNES_OPTION}
    Sleep    1s
    
    # Completar Hora Inicio
    Ingresar Texto    ${HORA_INICIO_INPUT}    ${HORA_INICIO}
    Sleep    1s
    
    # Completar Hora Fin
    Ingresar Texto    ${HORA_FIN_INPUT}    ${HORA_FIN}
    Sleep    1s

Hacer Click En Guardar Solicitud
    [Documentation]    Hace clic en el botón guardar de la solicitud
    Hacer Click En Elemento    ${GUARDAR_SOLICITUD_BUTTON}
    Sleep    2s

El Sistema Crea Nueva Solicitud Autorizacion
    [Documentation]    Verifica que se creó la nueva solicitud de autorización
    Verificar Texto En Página    ¡Registro creado exitosamente!

Acceder A Detalles Autorizacion
    [Arguments]    ${RADICADO_MERCURIO}
    [Documentation]    Accede a los detalles de una autorización filtrando por radicado y haciendo click en el botón Detalle
    Ingresar Texto    id=filtroRadicadoMercurio    ${RADICADO_MERCURIO}
    Sleep    1s
    Hacer Click En Elemento    xpath://button[@aria-label='Detalle' and .//span[text()='Detalle']]
    Sleep    2s
    Reload Page
    Sleep    2s

Hacer Click En Agregar Visita Administrativa
    [Documentation]    Hace clic en el botón agregar visita administrativa
    Hacer Click En Elemento    ${AGREGAR_VISITA_BUTTON}
    Sleep    2s
    
Hacer Click En Guardar Visita
    [Documentation]    Hace clic en el botón guardar visita
    Hacer Click En Elemento    ${GUARDAR_VISITA_BUTTON}
    Sleep    2s

El Sistema Registra Visita Administrativa
    [Documentation]    Verifica que se registró la visita administrativa
    Verificar Texto En Página    ¡Registro creado exitosamente!

Hacer Click En Agregar Resolucion
    [Documentation]    Hace clic en el botón agregar resolución
    Hacer Click En Elemento    ${AGREGAR_RESOLUCION_BUTTON}
    Sleep    2s

Completar Formulario Resolucion
    [Arguments]    ${NUMERO}    ${FECHA_EFECTOS}    ${FECHA_EXPEDICION}
    [Documentation]    Completa el formulario de resolución
    # Esperar que el modal esté presente
    Verificar Elemento Presente    ${FORM_RESOLUCION}
    Ingresar Texto    ${NUMERO_RESOLUCION_INPUT}    ${NUMERO}
    Ingresar Texto    ${FECHA_EFECTOS_FISCALES_INPUT}    ${FECHA_EFECTOS}
    Ingresar Texto    ${FECHA_EXPEDICION_INPUT}    ${FECHA_EXPEDICION}

Hacer Click En Guardar Resolucion
    [Documentation]    Hace clic en el botón guardar resolución
    Hacer Click En Elemento    ${GUARDAR_RESOLUCION_BUTTON}
    Sleep    2s

El Sistema Asocia Resolucion A Autorizacion
    [Documentation]    Verifica que se asoció la resolución a la autorización
    Verificar Texto En Página    Resolución asociada exitosamente

Hacer Click En Eliminar Autorizacion
    [Arguments]    ${RADICADO_MERCURIO}
    [Documentation]    Hace clic en el botón eliminar de una autorización
    Ingresar Texto    id=filtroRadicadoMercurio    ${RADICADO_MERCURIO}
    Sleep    1s
    Hacer Click En Elemento    ${ELIMINAR_AUTORIZACION_BUTTON}
    Sleep    1s

Confirmar Eliminacion Autorizacion
    [Documentation]    Confirma la eliminación de la autorización
    Verificar Elemento Presente    ${CONFIRMAR_ELIMINAR_BUTTON}
    Hacer Click En Elemento    ${CONFIRMAR_ELIMINAR_BUTTON}
    Sleep    2s

El Sistema Elimina La Autorizacion
    [Documentation]    Verifica que se eliminó la autorización
    Verificar Texto En Página    ¡Registro eliminado exitosamente!

Aplicar Filtros Para Reporte
    [Documentation]    Aplica los filtros necesarios para el reporte
    Verificar Elemento Presente    ${FILTROS_REPORTE}
    # TODO: Agregar filtros específicos según la interfaz real

Hacer Click En Boton Excel
    [Documentation]    Hace clic en el botón Excel para generar el reporte
    Hacer Click En Elemento    ${BOTON_EXCEL}
    Sleep    5s

Agregar Visita Administrativa A Autorizacion    
    [Documentation]    Agrega una visita administrativa a una autorización filtrando por radicado y completando el formulario real
    Sleep    2s
    # Completar formulario de visita
    # Visitador
    Hacer Click En Elemento    id=idVisitador
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content'][text()='Administrador DEL SISTEMA']
    Sleep    1s
    # Tipo de visita
    Hacer Click En Elemento    id=idTipo
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content'][text()='Actualización']
    Sleep    1s
    # Vehículo
    Hacer Click En Elemento    id=idVehiculo
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content'][text()='RJZ672']
    Sleep    1s
    # Fecha de la visita
    Seleccionar Fecha Hoy En Datepicker    id=fechaVisita
    Sleep    1s
    # Franja horaria
    Hacer Click En Elemento    id=idFranja
    Sleep    1s
    Hacer Click En Elemento    xpath://div[@class='ant-select-item-option-content'][text()='AM']
    Sleep    1s
    # Guardar visita (OK)
    Hacer Click En Elemento    xpath://button[@type='button' and contains(@class,'ant-btn-primary') and .//span[text()='OK']]
    Sleep    2s 