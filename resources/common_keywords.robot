*** Settings ***
Documentation     Keywords comunes reutilizables para el proyecto SISDEP
Resource          ../config/config.robot

*** Keywords ***
Abrir Navegador
    [Documentation]    Abre el navegador y maximiza la ventana
    [Arguments]    ${url}=${BASE_URL}
    ${chrome_options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --ignore-ssl-errors
    Call Method    ${chrome_options}    add_argument    --ignore-certificate-errors
    Call Method    ${chrome_options}    add_argument    --allow-running-insecure-content
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    Call Method    ${chrome_options}    add_argument    --disable-plugins

    Open Browser    ${url}    ${BROWSER}    options=${chrome_options}
    Maximize Browser Window
    Setup Test Environment

Cerrar Navegador
    [Documentation]    Cierra el navegador actual
    Close Browser

Esperar Elemento Visible
    [Documentation]    Espera a que un elemento sea visible
    [Arguments]    ${locator}    ${timeout}=${EXPLICIT_WAIT}
    Wait Until Element Is Visible    ${locator}    ${timeout}

Esperar Elemento Clickable
    [Documentation]    Espera a que un elemento sea clickeable
    [Arguments]    ${locator}    ${timeout}=${EXPLICIT_WAIT}
    Wait Until Element Is Enabled    ${locator}    ${timeout}



Hacer Click En Elemento
    [Documentation]    Hace click en un elemento después de esperar que sea clickeable
    [Arguments]    ${locator}    ${timeout}=${EXPLICIT_WAIT}
    Esperar Elemento Clickable    ${locator}    ${timeout}
    Click Element    ${locator}

Ingresar Texto
    [Documentation]    Ingresa texto en un campo después de esperar que sea visible
    [Arguments]    ${locator}    ${texto}    ${timeout}=${EXPLICIT_WAIT}
    Esperar Elemento Visible    ${locator}    ${timeout}
    Input Text    ${locator}    ${texto}

Verificar Texto En Página
    [Documentation]    Verifica que un texto esté presente en la página
    [Arguments]    ${texto}    ${timeout}=${EXPLICIT_WAIT}
    Wait Until Page Contains    ${texto}    ${timeout}

Verificar URL Contiene
    [Documentation]    Verifica que la URL actual contenga un texto específico
    [Arguments]    ${texto}    ${timeout}=${EXPLICIT_WAIT}
    Wait Until Location Contains    ${texto}    ${timeout}

Tomar Screenshot
    [Documentation]    Toma una captura de pantalla con nombre personalizado
    [Arguments]    ${nombre}=screenshot
    ${timestamp}=    Get Time    epoch
    ${screenshot_name}=    Set Variable    ${nombre}_${timestamp}.png
    Capture Page Screenshot    ${screenshot_name}
    Log    Screenshot guardado como: ${screenshot_name}

Verificar Elemento Presente
    [Documentation]    Verifica que un elemento esté presente en la página
    [Arguments]    ${locator}    ${timeout}=${EXPLICIT_WAIT}
    Wait Until Element Is Visible    ${locator}    ${timeout}

Limpiar Campo
    [Documentation]    Limpia el contenido de un campo de texto
    [Arguments]    ${locator}
    Clear Element Text    ${locator} 
Eliminar Atributo Readonly Y Escribir Fecha
    [Arguments]    ${locator}    ${fecha}
    ${id}=    Evaluate    '${locator}'.replace('id=','')
    Execute JavaScript    document.getElementById('${id}').removeAttribute('readonly')
    Input Text    ${locator}    ${fecha}
    Execute JavaScript    var input=document.getElementById('${id}'); input.dispatchEvent(new Event('input', { bubbles: true })); input.dispatchEvent(new Event('change', { bubbles: true })); 
Seleccionar Fecha Hoy En Datepicker
    [Arguments]    ${locator}
    # Si el locator es por id, quitar readonly con JS
    Run Keyword If    '${locator}'[:3] == 'id='    Execute JavaScript    document.getElementById('${locator.replace('id=','')}').removeAttribute('readonly')
    # Si el locator es xpath, quitar readonly con JS usando evaluate
    Run Keyword If    '${locator}'[:6] == 'xpath='    Execute JavaScript    var el=document.evaluate("${locator.replace('xpath=','')}",document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue;if(el){el.removeAttribute('readonly');}
    Hacer Click En Elemento    ${locator}
    Sleep    1s
    Hacer Click En Elemento    xpath://a[contains(@class,'ant-picker-today-btn') and text()='Today']
    Sleep    1s 