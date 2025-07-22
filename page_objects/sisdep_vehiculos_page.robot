*** Settings ***
Documentation     Page Object para la sección de Gestión de Vehículos en SISDEP
Resource          ../resources/common_keywords.robot

*** Variables ***
${MENU_VEHICULOS}    xpath://a[@href='/sisdep/vehiculos']
${SECCION_VEHICULOS_TITLE}    xpath://h1[contains(@class,'ant-typography') and text()='Vehiculos']
${AGREGAR_VEHICULO_BUTTON}    xpath://button[@aria-label='Agregar' and .//span[text()='Agregar']]
${NOMBRE_CONDUCTOR_INPUT}    xpath://input[@id='nombreConductor']
${PLACA_INPUT}    xpath://input[@id='placa']
${TIPO_VEHICULO_INPUT}    xpath://input[@id='idTipoVehiculo']
${TIPO_VEHICULO_OPCION_CAMION}    xpath://div[contains(@class,'ant-select-item-option-content') and text()='Camion']
${GUARDAR_VEHICULO_BUTTON}    xpath://button[@type='button' and .//span[text()='Guardar']]
${MENSAJE_EXITO_CREACION}    ¡Registro creado exitosamente!
${REMOVER_VEHICULO_BUTTON}    xpath://button[@aria-label='Remover' and .//span[text()='Remover']]
${CONFIRMAR_ELIMINAR_VEHICULO_BUTTON}    xpath://button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]
${MENSAJE_EXITO_ELIMINACION}    ¡Registro eliminado exitosamente!

*** Keywords ***
Ir A Seccion Vehiculos
    [Documentation]    Navega a la sección de Vehículos
    Hacer Click En Elemento    ${MENU_VEHICULOS}
    Sleep    2s
    Verificar Elemento Presente    ${SECCION_VEHICULOS_TITLE}

Hacer Click En Agregar Vehiculo
    [Documentation]    Hace clic en el botón Agregar vehículo
    Hacer Click En Elemento    ${AGREGAR_VEHICULO_BUTTON}
    Sleep    2s

Completar Formulario Vehiculo
    [Arguments]    ${NOMBRE_CONDUCTOR}    ${PLACA}    ${TIPO_VEHICULO}
    [Documentation]    Completa el formulario de vehículo
    Ingresar Texto    ${NOMBRE_CONDUCTOR_INPUT}    ${NOMBRE_CONDUCTOR}
    Ingresar Texto    ${PLACA_INPUT}    ${PLACA}
    Hacer Click En Elemento    ${TIPO_VEHICULO_INPUT}
    Sleep    1s
    Hacer Click En Elemento    xpath://div[contains(@class,'ant-select-item-option-content') and text()='${TIPO_VEHICULO}']
    Sleep    1s

Hacer Click En Guardar Vehiculo
    [Documentation]    Hace clic en el botón Guardar vehículo
    Hacer Click En Elemento    ${GUARDAR_VEHICULO_BUTTON}
    Sleep    2s

Verificar Creacion Vehiculo Exitosa
    [Documentation]    Verifica que el vehículo fue creado exitosamente
    Verificar Texto En Página    ${MENSAJE_EXITO_CREACION}

Seleccionar Vehiculo Por Placa
    [Arguments]    ${PLACA}
    [Documentation]    Selecciona un vehículo por placa
    Ingresar Texto    ${PLACA_INPUT}    ${PLACA}
    Sleep    1s

Hacer Click En Remover Vehiculo
    [Documentation]    Hace clic en el botón Remover vehículo
    Hacer Click En Elemento    ${REMOVER_VEHICULO_BUTTON}
    Sleep    1s

Confirmar Eliminacion Vehiculo
    [Documentation]    Confirma la eliminación del vehículo
    Hacer Click En Elemento    ${CONFIRMAR_ELIMINAR_VEHICULO_BUTTON}
    Sleep    2s

Verificar Vehiculo Eliminado
    [Documentation]    Verifica que el vehículo fue eliminado
    Verificar Texto En Página    ${MENSAJE_EXITO_ELIMINACION} 

Eliminar Vehiculo Por Placa
    [Arguments]    ${PLACA}
    [Documentation]    Elimina un vehículo por placa llenando el input y haciendo clic en Remover
    Ingresar Texto    ${PLACA_INPUT}    ${PLACA}
    Sleep    1s
    Hacer Click En Elemento    ${REMOVER_VEHICULO_BUTTON}
    Sleep    2s 