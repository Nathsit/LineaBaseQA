"""
Feature: Autenticación de Usuario - Scenario: Cierre de sesión
Equivalente a test_suites/features/autenticacion/logout/logout.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from config.config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.autenticacion
@pytest.mark.logout
@pytest.mark.funcional
def test_logout_exitoso(page: Page):
    """
    Test del flujo completo de logout
    Equivalente a: Logout Exitoso
    """
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Navegar a SISDEP y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    login_page.verificar_login_exitoso_sisdep()
    
    # Verificar dashboard cargado
    dashboard_page.verificar_dashboard_cargado()
    
    # Realizar logout
    dashboard_page.realizar_logout()
    
    # Verificar logout exitoso (esto ya verifica el elemento de login)
    dashboard_page.verificar_logout_exitoso()
    
    # Verificar que los elementos de login están presentes (verificación adicional)
    login_page.verificar_elementos_de_login_sisdep_presentes()

