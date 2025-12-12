"""
Feature: Estudio Socioeconómico (Social)
Equivalente a test_suites/features/social/estudio_socioeconomico.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.estudio_socioeconomico_page import EstudioSocioeconomicoPage
from config.config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.social
@pytest.mark.estudio
@pytest.mark.crear
@pytest.mark.positivo
def test_crear_nuevo_estudio_socioeconomico(page: Page):
    """
    Crear un nuevo estudio socioeconómico
    Equivalente a: Crear Nuevo Estudio Socioeconomico
    """
    login_page = LoginPage(page)
    estudio_page = EstudioSocioeconomicoPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    estudio_page.ir_a_seccion_estudio_socioeconomico()
    estudio_page.filtrar_estudio_por_fecha("2025", "dic.")
    estudio_page.seleccionar_estudio_socioeconomico_en_calendario()
    estudio_page.guardar_formularios_estudio_varias_veces(7)


@pytest.mark.social
@pytest.mark.estudio
@pytest.mark.firmar
@pytest.mark.positivo
def test_firmar_estudio_socioeconomico_completo(page: Page):
    """
    Firmar un estudio socioeconómico completo
    Equivalente a: Firmar Estudio Socioeconomico Completo
    """
    login_page = LoginPage(page)
    estudio_page = EstudioSocioeconomicoPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    estudio_page.ir_a_seccion_estudio_socioeconomico()
    estudio_page.filtrar_estudio_por_fecha("2025", "dic.")
    estudio_page.seleccionar_estudio_socioeconomico_en_calendario()
    estudio_page.guardar_formularios_estudio_varias_veces(7)
    # Nota: Agregar lógica de firma según implementación


@pytest.mark.social
@pytest.mark.estudio
@pytest.mark.reporte
@pytest.mark.pdf
@pytest.mark.positivo
def test_generar_pdf_estudio_socioeconomico(page: Page):
    """
    Generar PDF del estudio socioeconómico
    Equivalente a: Generar PDF Estudio Socioeconomico
    """
    login_page = LoginPage(page)
    estudio_page = EstudioSocioeconomicoPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    estudio_page.ir_a_seccion_estudio_socioeconomico()
    estudio_page.filtrar_estudio_por_fecha("2025", "abr.")
    estudio_page.generar_pdf_estudio_socioeconomico()


@pytest.mark.social
@pytest.mark.estudio
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_estudio_socioeconomico(page: Page):
    """
    Actualizar un estudio socioeconómico existente
    Equivalente a: Actualizar Estudio Socioeconomico
    Flujo: Filtrar por fecha -> Seleccionar en calendario -> Detalles -> Guardar
    """
    login_page = LoginPage(page)
    estudio_page = EstudioSocioeconomicoPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    estudio_page.ir_a_seccion_estudio_socioeconomico()
    # Actualizar el estudio usando la misma fecha del primer test
    estudio_page.actualizar_estudio_socioeconomico("2025", "dic.")
    estudio_page.verificar_actualizacion_estudio_exitosa()

