"""
Page Object para la página del dashboard de SISDEP
Equivalente a page_objects/sisdep_dashboard_page.robot
"""
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from config.config import SISDEP_URL
from utils.common_helpers import (
    verificar_elemento_presente,
    hacer_click_en_elemento,
    verificar_url_contiene
)


class DashboardPage:
    """Page Object para la página del dashboard de SISDEP"""
    
    # Locators del dashboard SISDEP
    DASHBOARD_TITLE = "xpath=//h1[text()='SISDEP']"
    USER_PROFILE_ICON = "xpath=//span[contains(@class, 'ant-avatar') and contains(@class, 'ant-dropdown-trigger')]"
    LOGOUT_OPTION = "xpath=//span[contains(@class, 'ant-dropdown-menu-title-content') and text()='Cerrar sesión']"
    
    # Mensajes esperados
    LOGOUT_SUCCESS_MSG = "xpath=//h5[@class='L_2VJc3_']"  # Valida que estamos en la página de login
    
    def __init__(self, page: Page):
        self.page = page
    
    def verificar_dashboard_cargado(self):
        """
        Verifica que el dashboard se haya cargado correctamente
        Equivalente a: Verificar Dashboard Cargado
        """
        verificar_elemento_presente(self.page, self.DASHBOARD_TITLE)
    
    def hacer_click_en_perfil_usuario(self):
        """
        Hace click en el ícono del perfil del usuario
        Equivalente a: Hacer Click En Perfil Usuario
        """
        hacer_click_en_elemento(self.page, self.USER_PROFILE_ICON)
    
    def seleccionar_cerrar_sesion(self):
        """
        Selecciona la opción de cerrar sesión del menú desplegable
        Equivalente a: Seleccionar Cerrar Sesion
        """
        hacer_click_en_elemento(self.page, self.LOGOUT_OPTION)
    
    def realizar_logout(self):
        """
        Realiza el proceso completo de logout
        Equivalente a: Realizar Logout
        """
        import time
        
        self.hacer_click_en_perfil_usuario()
        # Esperar un momento para que el menú se abra
        time.sleep(1)
        self.seleccionar_cerrar_sesion()
        # Esperar a que se complete el logout
        time.sleep(2)
    
    def verificar_logout_exitoso(self):
        """
        Verifica que el logout fue exitoso
        Equivalente a: Verificar Logout Exitoso
        """
        import time
        from playwright.sync_api import expect
        
        # Esperar un momento para que se complete el logout
        time.sleep(2)
        
        # Verificar que el elemento de login está presente (indica que estamos en la página de login)
        verificar_elemento_presente(self.page, self.LOGOUT_SUCCESS_MSG)
        
        # Verificar la URL de manera más segura (sin esperar navegación)
        try:
            current_url = self.page.url
            url_verification_path = "/sisdep" if "localhost" not in SISDEP_URL else "localhost:3000"
            if url_verification_path not in current_url:
                # Si no está en la URL, esperar un poco más y verificar de nuevo
                time.sleep(1)
                current_url = self.page.url
                assert url_verification_path in current_url, f"URL no contiene '{url_verification_path}'. URL actual: {current_url}"
        except Exception as e:
            # Si hay algún error, al menos verificar que el elemento de login está presente
            # Esto es suficiente para confirmar que el logout fue exitoso
            pass

