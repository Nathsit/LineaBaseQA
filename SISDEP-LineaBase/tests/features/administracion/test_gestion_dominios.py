"""
Suite de pruebas para la gestión de dominios en SISDEP
Equivalente a test_suites/features/administracion/gestion_dominios.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.dominios_page import DominiosPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import DOMINIO_TIPO_DOCUMENTO, NUEVO_VALOR_DOMINIO


@pytest.mark.dominios
@pytest.mark.agregar
@pytest.mark.positivo
def test_agregar_nuevo_valor_a_dominio(page: Page):
    """
    Agregar un nuevo valor a un dominio existente
    Equivalente a: Agregar Nuevo Valor A Dominio
    """
    login_page = LoginPage(page)
    dominios_page = DominiosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección dominios
    dominios_page.el_administrador_esta_en_seccion_dominios()
    dominios_page.selecciona_dominio_especifico(DOMINIO_TIPO_DOCUMENTO)
    dominios_page.ingresa_nuevo_valor_en_dominio(NUEVO_VALOR_DOMINIO)
    # Nota: Los siguientes pasos están comentados en el original
    # dominios_page.hace_click_en_agregar_valor()
    # dominios_page.el_sistema_anade_el_nuevo_valor_al_dominio()


@pytest.mark.dominios
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_valor_de_dominio(page: Page):
    """
    Actualizar la descripción de un valor existente en un dominio
    Equivalente a: Actualizar Valor De Dominio
    """
    login_page = LoginPage(page)
    dominios_page = DominiosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección dominios y actualizar
    dominios_page.el_administrador_esta_en_seccion_dominios()
    dominios_page.selecciona_dominio_especifico(DOMINIO_TIPO_DOCUMENTO)
    dominios_page.hace_click_en_actualizar_valor()
    dominios_page.el_sistema_guarda_los_cambios_del_valor()


@pytest.mark.dominios
@pytest.mark.eliminar
@pytest.mark.positivo
def test_eliminar_valor_de_dominio_no_en_uso(page: Page):
    """
    Eliminar un valor de dominio que no está asociado a ningún registro
    Equivalente a: Eliminar Valor De Dominio No En Uso
    """
    login_page = LoginPage(page)
    dominios_page = DominiosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección dominios y eliminar
    dominios_page.el_administrador_esta_en_seccion_dominios()
    dominios_page.selecciona_dominio_especifico(DOMINIO_TIPO_DOCUMENTO)
    dominios_page.hace_click_en_eliminar_valor()


@pytest.mark.dominios
@pytest.mark.agregar
@pytest.mark.negativo
def test_agregar_nuevo_valor_vacio_a_dominio(page: Page):
    """
    Agregar un nuevo valor vacío a un dominio
    Equivalente a: Agregar Nuevo Valor vacio a Dominio
    """
    login_page = LoginPage(page)
    dominios_page = DominiosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección dominios
    dominios_page.el_administrador_esta_en_seccion_dominios()
    dominios_page.selecciona_dominio_especifico(DOMINIO_TIPO_DOCUMENTO)
    dominios_page.ingresa_nuevo_valor_en_dominio(NUEVO_VALOR_DOMINIO)
    dominios_page.hace_click_en_agregar_valor()
    dominios_page.el_sistema_no_debe_anadir_el_nuevo_valor_al_dominio()

