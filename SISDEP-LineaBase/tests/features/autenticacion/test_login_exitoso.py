"""
Feature: Autenticación de Usuario - Scenario: Inicio de sesión exitoso
Equivalente a test_suites/features/autenticacion/login_exitoso/login_exitoso.robot
"""
import pytest
import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from config.config import VALID_USERNAME, VALID_PASSWORD, SISDEP_URL
from utils.common_helpers import tomar_screenshot


@pytest.mark.autenticacion
@pytest.mark.login
@pytest.mark.positivo
@pytest.mark.smoke
@pytest.mark.funcional
def test_inicio_de_sesion_exitoso_con_credenciales_validas(page: Page):
    """
    Given que el usuario tiene un usuario y contraseña válidos y activos.
    When ingresa sus credenciales en la página de inicio de sesión.
    And hace clic en el botón "Iniciar sesión".
    Then el sistema le da la bienvenida y muestra la pantalla principal.
    Equivalente a: Inicio De Sesion Exitoso Con Credenciales Validas
    """
    login_page = LoginPage(page)
    
    # Navegar a SISDEP
    login_page.navegar_a_sisdep()
    
    # Verificar elementos de login presentes
    login_page.verificar_elementos_de_login_sisdep_presentes()
    
    # Realizar login
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Verificar login exitoso
    login_page.verificar_login_exitoso_sisdep()
    
    # Verificar elemento presente (mensaje de éxito)
    login_page.verificar_elemento_presente(login_page.SUCCESS_MESSAGE)
    
    # Tomar screenshot
    tomar_screenshot(page, "login_exitoso_completado")

