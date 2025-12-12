"""
Feature: Autenticación de Usuario - Scenario: Inicio de sesión con credenciales inválidas
Equivalente a test_suites/features/autenticacion/login_credenciales_invalidas/login_credenciales_invalidas.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from config.config import INVALID_USERNAME, INVALID_PASSWORD, SISDEP_URL
from data.test_data import SISDEP_LOGIN_ERROR_MSG


@pytest.mark.autenticacion
@pytest.mark.login
@pytest.mark.negativo
@pytest.mark.funcional
def test_login_con_credenciales_completamente_invalidas(page: Page):
    """
    Test de login con credenciales completamente inválidas
    """
    login_page = LoginPage(page)
    
    # Navegar a SISDEP
    login_page.navegar_a_sisdep()
    
    # Realizar login con credenciales inválidas
    login_page.realizar_login_sisdep(INVALID_USERNAME, INVALID_PASSWORD)
    
    # Verificar que el login falló
    login_page.verificar_login_fallido_sisdep(SISDEP_LOGIN_ERROR_MSG)


@pytest.mark.autenticacion
@pytest.mark.login
@pytest.mark.negativo
@pytest.mark.funcional
def test_login_con_usuario_invalido_contraseña_valida(page: Page):
    """
    Test de login con usuario inválido pero contraseña válida
    """
    from config.config import VALID_PASSWORD
    
    login_page = LoginPage(page)
    
    # Navegar a SISDEP
    login_page.navegar_a_sisdep()
    
    # Realizar login con usuario inválido
    login_page.realizar_login_sisdep(INVALID_USERNAME, VALID_PASSWORD)
    
    # Verificar que el login falló
    login_page.verificar_login_fallido_sisdep(SISDEP_LOGIN_ERROR_MSG)


@pytest.mark.autenticacion
@pytest.mark.login
@pytest.mark.negativo
@pytest.mark.funcional
def test_login_con_contraseña_invalida_usuario_valido(page: Page):
    """
    Test de login con contraseña inválida pero usuario válido
    """
    from config.config import VALID_USERNAME
    
    login_page = LoginPage(page)
    
    # Navegar a SISDEP
    login_page.navegar_a_sisdep()
    
    # Realizar login con contraseña inválida
    login_page.realizar_login_sisdep(VALID_USERNAME, INVALID_PASSWORD)
    
    # Verificar que el login falló
    login_page.verificar_login_fallido_sisdep(SISDEP_LOGIN_ERROR_MSG)

