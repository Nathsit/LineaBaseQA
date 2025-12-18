"""
Page Object para la gestión de Personas en SISDEP
"""
import sys
from pathlib import Path
import time

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from utils.common_helpers import (
    verificar_elemento_presente,
    hacer_click_en_elemento
)


class PersonasPage:
    """Page Object para la gestión de Personas en SISDEP"""
    
    # Navegación
    MENU_PERSONAS_LINK = "xpath=//a[@href='/sisdep/personas']"
    
    def __init__(self, page: Page):
        self.page = page
    
    def ir_a_modulo_personas(self):
        """Navega al módulo de Personas"""
        menu_personas = self.page.locator(self.MENU_PERSONAS_LINK)
        menu_personas.wait_for(state="visible", timeout=10000)
        menu_personas.click()
        time.sleep(2)  # Esperar a que cargue la página

