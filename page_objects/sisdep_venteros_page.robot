*** Settings ***
Documentation     Page Object para la sección de Gestión de Venteros en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
${MENU_PERSONAS}                xpath://div[@role='menuitem' and .//span[text()='Social']]
${SUBMENU_REGISTRO_VENTERO}    xpath://a[@href='/sisdep/social/registro-ventero']
${SECCION_VENTEROS_TITLE}      xpath://span[@class='ant-page-header-heading-title' and @title='Registro nuevo ventero']
${AGREGAR_VENTERO_BUTTON}      # TODO: Selector del botón Agregar
${GUARDAR_VENTERO_BUTTON}      xpath://button[@type='submit' and .//span[text()='Guardar']]
${DETALLES_VENTERO_BUTTON}     # TODO: Selector del botón Detalles
${EXCEL_VENTEROS_BUTTON}    xpath://button[.//span[text()='Excel'] and @type='button']
${MENSAJE_EXITO_CREACION}    ¡Registro creado exitosamente!
${MENSAJE_EXITO_ACTUALIZACION}    ¡Registro actualizado exitosamente!
${PRIMER_NOMBRE_INPUT}         xpath://input[@id='nombre1']
${PRIMER_APELLIDO_INPUT}       xpath://input[@id='apellido1']
${TIPO_DOCUMENTO_INPUT}        xpath://input[@id='idTipoDocumento']
${TIPO_DOCUMENTO_OPCION_CC}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Cédula de ciudadanía']
${DOCUMENTO_INPUT}             xpath://input[@id='documento']
${FECHA_EXPEDICION_INPUT}      xpath://input[@id='fechaExpedicion']
${LUGAR_EXPEDICION_INPUT}      xpath://input[@id='lugarExpedicion']
${LUGAR_EXPEDICION_OPCION_MEDELLIN}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='MEDELLÍN']
${NACIONALIDAD_INPUT}          xpath://input[@id='idNacionalidad']
${NACIONALIDAD_OPCION_COLOMBIANO}      xpath://div[contains(@class,'ant-select-item-option-content') and text()='Colombiano/a']
${SEXO_INPUT}                  xpath://input[@id='idSexo']
${SEXO_OPCION_HOMBRE}          xpath://div[contains(@class,'ant-select-item-option-content') and text()='Hombre']
${TIPO_PERSONA_INPUT}          xpath://input[@id='idTipoPersona']
${TIPO_PERSONA_OPCION_NATURAL}         xpath://div[contains(@class,'ant-select-item-option-content') and text()='Natural']
${TELEFONO_CELULAR_INPUT}      xpath://input[@id='telefonoCelular']
${FECHA_NACIMIENTO_INPUT}      xpath://input[@id='fechaNacimiento']
${ESTADO_CIVIL_INPUT}          xpath://input[@id='ventero_idEstadoCivil']
${ESTADO_CIVIL_OPCION_SOLTERO}         xpath://div[contains(@class,'ant-select-item-option-content') and text()='Soltero (a)']
${NIVEL_ESCOLARIDAD_INPUT}      xpath://input[@id='ventero_idEscolaridad']
${NIVEL_ESCOLARIDAD_OPCION_BASICA_SECUNDARIA}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Básica Secundaria']
${NIVEL_ESCOLARIDAD_OPCION_PREESCOLAR}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Preescolar']
${PERSONAS}    xpath://a[@href='/sisdep/personas']
${FILTRO_DOCUMENTO_INPUT}    xpath://input[@id='documento' and @placeholder='Documento']
${DETALLES_VENTERO_BUTTON_PRIMERO}    xpath:(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]

*** Keywords ***
El Usuario Esta En Seccion Registro Ventero
    [Documentation]    Navega a la sección de Registro de Venteros
    Hacer Click En Elemento    ${MENU_PERSONAS}
    Sleep    1s
    Hacer Click En Elemento    ${SUBMENU_REGISTRO_VENTERO}
    Sleep    2s
    Reload Page
    Verificar Elemento Presente    ${SECCION_VENTEROS_TITLE}

Hacer Click En Agregar Ventero
    [Documentation]    Hace clic en el botón Agregar ventero
    Hacer Click En Elemento    ${AGREGAR_VENTERO_BUTTON}
    Sleep    2s

Completar Formulario Ventero
    [Arguments]    ${PRIMER_NOMBRE}    ${PRIMER_APELLIDO}    ${TIPO_DOCUMENTO}    ${DOCUMENTO}    ${FECHA_EXPEDICION}    ${LUGAR_EXPEDICION}    ${NACIONALIDAD}    ${SEXO}    ${TIPO_PERSONA}    ${TELEFONO_CELULAR}    ${FECHA_NACIMIENTO}    ${ESTADO_CIVIL}    ${NIVEL_ESCOLARIDAD}
    [Documentation]    Completa el formulario de ventero con los datos proporcionados
    Ingresar Texto    ${PRIMER_NOMBRE_INPUT}    ${PRIMER_NOMBRE}
    Ingresar Texto    ${PRIMER_APELLIDO_INPUT}    ${PRIMER_APELLIDO}
    Hacer Click En Elemento    ${TIPO_DOCUMENTO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_DOCUMENTO}']
    Ingresar Texto    ${DOCUMENTO_INPUT}    ${DOCUMENTO}
    Ingresar Texto    ${FECHA_EXPEDICION_INPUT}    ${FECHA_EXPEDICION}
    Hacer Click En Elemento    ${LUGAR_EXPEDICION_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${LUGAR_EXPEDICION}']
    Hacer Click En Elemento    ${NACIONALIDAD_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${NACIONALIDAD}']
    Hacer Click En Elemento    ${SEXO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${SEXO}']
    Hacer Click En Elemento    ${TIPO_PERSONA_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_PERSONA}']
    Ingresar Texto    ${TELEFONO_CELULAR_INPUT}    ${TELEFONO_CELULAR}
    Ingresar Texto    ${FECHA_NACIMIENTO_INPUT}    ${FECHA_NACIMIENTO}
    Hacer Click En Elemento    ${ESTADO_CIVIL_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${ESTADO_CIVIL}']
    Hacer Click En Elemento    ${NIVEL_ESCOLARIDAD_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${NIVEL_ESCOLARIDAD}']
    Sleep    1s

Hacer Click En Guardar Ventero
    [Documentation]    Hace clic en el botón Guardar ventero
    Hacer Click En Elemento    ${GUARDAR_VENTERO_BUTTON}
    Sleep    2s

Verificar Creacion Ventero Exitosa
    [Documentation]    Verifica que el ventero fue creado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_CREACION}

Filtrar Ventero Por Documento
    [Arguments]    ${NUM_DOC}
    [Documentation]    Filtra la lista de venteros por número de documento
    # TODO: Implementar filtro

Hacer Click En Detalles Ventero
    [Documentation]    Hace clic en el botón Detalles del ventero filtrado
    Hacer Click En Elemento    ${DETALLES_VENTERO_BUTTON}
    Sleep    2s

Actualizar Datos Ventero
    [Arguments]    ${NOMBRE}    ${APELLIDO}    ${DIRECCION}    ${TELEFONO}    ${OTROS}
    [Documentation]    Actualiza los datos del ventero con los valores proporcionados
    # TODO: Implementar actualización de campos

Verificar Actualizacion Ventero Exitosa
    [Documentation]    Verifica que el ventero fue actualizado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_ACTUALIZACION}

Hacer Click En Boton Excel Venteros
    [Arguments]    ${DOCUMENTO}
    [Documentation]    Hace clic en el botón Excel para exportar los venteros filtrados
    Hacer Click En Elemento    ${PERSONAS}
    Sleep    2s
    Ingresar Texto    ${FILTRO_DOCUMENTO_INPUT}    ${DOCUMENTO}
    Sleep    1s
    Hacer Click En Elemento    ${EXCEL_VENTEROS_BUTTON}
    Sleep    2s

Verificar Descarga Reporte Excel Venteros
    [Documentation]    Verifica que el archivo Excel de venteros fue descargado correctamente
    # TODO: Implementar verificación de descarga 

Ir A Personas Y Buscar Ventero Por Documento
    [Arguments]    ${DOCUMENTO}
    [Documentation]    Navega al menú Personas, filtra por documento y abre detalles del ventero
    Hacer Click En Elemento    ${PERSONAS}
    Sleep    2s
    Ingresar Texto    ${FILTRO_DOCUMENTO_INPUT}    ${DOCUMENTO}
    Sleep    1s
    Hacer Click En Elemento    ${DETALLES_VENTERO_BUTTON_PRIMERO}
    Sleep    2s 