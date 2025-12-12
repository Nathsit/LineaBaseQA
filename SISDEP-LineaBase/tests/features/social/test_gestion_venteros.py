"""
Feature: Gestión de Venteros (Social)
Equivalente a test_suites/features/social/gestion_venteros.robot
"""
import pytest
import sys
import random
import string
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.venteros_page import VenterosPage
from config.config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.social
@pytest.mark.venteros
@pytest.mark.crear
@pytest.mark.positivo
def test_registrar_nuevo_ventero(page: Page):
    """
    Given que el usuario está en la opción de "Registro ventero".
    When llena todos los campos requeridos en el formulario.
    And hace clic en "Guardar".
    Then se crea un nuevo registro de ventero en el sistema.
    Equivalente a: Registrar Nuevo Ventero
    """
    login_page = LoginPage(page)
    venteros_page = VenterosPage(page)
    
    # Generar documento aleatorio
    documento_random = ''.join(random.choices(string.digits, k=10))
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    venteros_page.el_usuario_esta_en_seccion_registro_ventero()
    venteros_page.completar_formulario_ventero(
        primer_nombre="TEST",
        primer_apellido="TEST",
        tipo_documento="Cédula de ciudadanía",
        documento=documento_random,
        fecha_expedicion="01/01/2020",
        lugar_expedicion="MEDELLÍN",
        nacionalidad="Colombiano/a",
        sexo="Hombre",
        tipo_persona="Natural",
        telefono_celular="3001234567",
        fecha_nacimiento="01/01/1990",
        estado_civil="Soltero (a)",
        nivel_escolaridad="Preescolar"
    )
    venteros_page.hacer_click_en_guardar_ventero()
    venteros_page.verificar_creacion_ventero_exitosa()
    
    # Guardar documento para uso en otros tests
    pytest.documento_prueba = documento_random


@pytest.mark.social
@pytest.mark.venteros
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_informacion_ventero(page: Page):
    """
    Given que el usuario ha seleccionado los detalles de un ventero.
    When da clic en "Guardar".
    Then la información del ventero se actualiza.
    Equivalente a: Actualizar Informacion Ventero
    """
    login_page = LoginPage(page)
    venteros_page = VenterosPage(page)
    
    # Usar documento del test anterior o uno existente
    documento = getattr(pytest, 'documento_prueba', '1000100100')
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    venteros_page.ir_a_personas_y_buscar_ventero_por_documento(documento)
    venteros_page.hacer_click_en_guardar_ventero()
    venteros_page.verificar_actualizacion_ventero_exitosa()


@pytest.mark.social
@pytest.mark.venteros
@pytest.mark.reporte
@pytest.mark.excel
def test_generar_reporte_venteros_excel(page: Page):
    """
    Given que el usuario se encuentra en el menú "Persona".
    When aplica los filtros de búsqueda deseados.
    And hace clic en el botón "Excel".
    Then el sistema descarga un reporte en formato Excel con los venteros filtrados.
    Equivalente a: Generar Reporte Venteros Excel
    """
    login_page = LoginPage(page)
    venteros_page = VenterosPage(page)
    
    documento = getattr(pytest, 'documento_prueba', '1000100100')
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    venteros_page.hacer_click_en_boton_excel_venteros(documento)

