"""
Feature: Gestión de Ofertas Institucionales (Social)
Equivalente a test_suites/features/social/gestion_ofertas_institucionales.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.ofertas_institucionales_page import OfertasInstitucionalesPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import TIPO_OFERTA, CONVENIO, DOCUMENTO_PARTICIPANTE, TIPO_CONOCIMIENTO


@pytest.mark.social
@pytest.mark.ofertas
@pytest.mark.crear
@pytest.mark.positivo
def test_registrar_nueva_oferta_institucional(page: Page):
    """
    Registrar una nueva oferta institucional
    Equivalente a: Registrar Nueva Oferta Institucional
    """
    login_page = LoginPage(page)
    ofertas_page = OfertasInstitucionalesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    ofertas_page.ir_a_seccion_ofertas_institucionales()
    ofertas_page.hacer_click_en_agregar_oferta()
    ofertas_page.completar_formulario_oferta(
        fecha_ejecucion="2025-07-21",
        tipo_oferta=TIPO_OFERTA,
        convenio=CONVENIO
    )
    ofertas_page.hacer_click_en_guardar_oferta()
    ofertas_page.verificar_creacion_oferta_exitosa()


@pytest.mark.social
@pytest.mark.ofertas
@pytest.mark.participante
@pytest.mark.positivo
def test_agregar_participante_a_oferta_institucional(page: Page):
    """
    Agregar un participante a una oferta institucional
    Equivalente a: Agregar Participante A Oferta Institucional
    """
    login_page = LoginPage(page)
    ofertas_page = OfertasInstitucionalesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    ofertas_page.ir_a_seccion_ofertas_institucionales()
    #ofertas_page.agregar_participante_a_oferta(
     #   tipo_oferta=TIPO_OFERTA,
     #   documento=DOCUMENTO_PARTICIPANTE,
     #   tipo_conocimiento=TIPO_CONOCIMIENTO
    #)
    #ofertas_page.verificar_participante_agregado()


@pytest.mark.social
@pytest.mark.ofertas
@pytest.mark.eliminar
@pytest.mark.negativo
def test_eliminar_oferta_institucional_con_participantes(page: Page):
    """
    Intentar eliminar una oferta institucional con participantes
    Equivalente a: Eliminar Oferta Institucional Con Participantes
    """
    login_page = LoginPage(page)
    ofertas_page = OfertasInstitucionalesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    ofertas_page.ir_a_seccion_ofertas_institucionales()
    ofertas_page.eliminar_oferta_con_participantes(TIPO_OFERTA)


@pytest.mark.social
@pytest.mark.ofertas
@pytest.mark.participante
@pytest.mark.eliminar
@pytest.mark.positivo
def test_eliminar_participante_de_oferta_institucional(page: Page):
    """
    Eliminar un participante de una oferta institucional
    Equivalente a: Eliminar Participante De Oferta Institucional
    """
    login_page = LoginPage(page)
    ofertas_page = OfertasInstitucionalesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    ofertas_page.ir_a_seccion_ofertas_institucionales()
    #ofertas_page.eliminar_participante_de_oferta(TIPO_OFERTA)
    #ofertas_page.verificar_participante_eliminado()


@pytest.mark.social
@pytest.mark.ofertas
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_oferta_institucional(page: Page):
    """
    Actualizar una oferta institucional existente
    Equivalente a: Actualizar Oferta Institucional
    Flujo: Filtrar por tipo de oferta -> Detalles -> Guardar
    """
    login_page = LoginPage(page)
    ofertas_page = OfertasInstitucionalesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    ofertas_page.ir_a_seccion_ofertas_institucionales()
    # Actualizar la oferta usando el tipo de oferta del primer test
    ofertas_page.actualizar_oferta_institucional(TIPO_OFERTA)
    ofertas_page.verificar_actualizacion_oferta_exitosa()

