*** Settings ***
Documentation     Suite de pruebas para la Feature: Gestión de Ofertas Institucionales (Social)
Resource          ../../../resources/common_keywords.robot
Resource          ../../../page_objects/sisdep_login_page.robot
Resource          ../../../page_objects/sisdep_ofertas_institucionales_page.robot
Resource          ../../../data/sisdep_test_data.robot
Suite Setup       Setup Test Environment
Suite Teardown    Teardown Test Environment

*** Test Cases ***
Registrar Nueva Oferta Institucional
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Ofertas Institucionales
    Hacer Click En Agregar Oferta
    Completar Formulario Oferta    01/01/2024    sena dadad    Secretaria de Salud
    Hacer Click En Guardar Oferta

Agregar Participante A Oferta Institucional
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Ofertas Institucionales
    Agregar Participante A Oferta    sena dadad    1000100100    Atención en la oficina
    Verificar Participante Agregado

Eliminar Oferta Institucional Con Participantes
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Ofertas Institucionales
    Eliminar Oferta con Participantes    sena dadad

Eliminar Participante De Oferta Institucional
    [Setup]    Abrir Navegador    ${SISDEP_URL}
    [Teardown]    Cerrar Navegador
    Navegar A SISDEP
    Realizar Login SISDEP    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Ir A Seccion Ofertas Institucionales
    Eliminar Participante De Oferta    sena dadad
    Verificar Participante Eliminado 