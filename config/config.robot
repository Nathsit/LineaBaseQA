*** Settings ***
Documentation     
Library           SeleniumLibrary
Library           Collections
Library           String
Library           OperatingSystem

*** Variables ***
# URLs de la aplicación SISDEP
#${BASE_URL}                    http://localhost:3000
${BASE_URL}                    https://www.medellin.gov.co/sisdep
${SISDEP_URL}                  ${BASE_URL}
${LOGIN_URL}                   ${SISDEP_URL}
${SECURE_AREA_URL}             ${SISDEP_URL}

# Detección automática del ambiente para verificación de URL
${URL_VERIFICATION_PATH}       ${BASE_URL.find('localhost') != -1 and 'localhost:3000' or '/sisdep'}

# Configuración del navegador
${BROWSER}                     Chrome
${BROWSER_HEADLESS}            False
${IMPLICIT_WAIT}              10s
${EXPLICIT_WAIT}               30s
${SELENIUM_SPEED}              0.3s
${PAGE_LOAD_TIMEOUT}           60s
# Credenciales de prueba SISDEP
${VALID_USERNAME}              admin
${VALID_PASSWORD}              EspacioPublico2024?sisdep
${INVALID_USERNAME}            invalid_user
${INVALID_PASSWORD}            invalid_password

# Rutas de archivos
${DRIVERS_PATH}                ${EXECDIR}/drivers
${REPORTS_PATH}                ${EXECDIR}/reports
${LOGS_PATH}                   ${EXECDIR}/logs
${DATA_PATH}                   ${EXECDIR}/data

# Configuración de reportes
${OUTPUT_DIR}                  ${REPORTS_PATH}
${LOG_LEVEL}                   INFO
${SCREENSHOT_DIR}              ${REPORTS_PATH}/screenshots

*** Keywords ***
Setup Test Environment
    [Documentation]    Configuración inicial del entorno de pruebas
    Set Selenium Speed    ${SELENIUM_SPEED}
    Set Selenium Implicit Wait    ${IMPLICIT_WAIT}
    Set Screenshot Directory    ${SCREENSHOT_DIR}
    Set Selenium Timeout    ${EXPLICIT_WAIT}
    Set Selenium Page Load Timeout    ${PAGE_LOAD_TIMEOUT}
    # Ya no es necesario modificar el PATH para Chrome si chromedriver.exe está en drivers/

Teardown Test Environment
    [Documentation]    Limpieza del entorno de pruebas
    Close All Browsers 