"""
Page Object para la página de login de SISDEP
Equivalente a page_objects/sisdep_login_page.robot
"""
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page, expect
from typing import Optional
from config.config import SISDEP_URL, EXPLICIT_WAIT
from utils.common_helpers import (
    esperar_elemento_visible,
    hacer_click_en_elemento,
    ingresar_texto,
    verificar_elemento_presente,
    verificar_texto_en_pagina,
    limpiar_campo
)


class LoginPage:
    """Page Object para la página de login de SISDEP"""
    
    # Locators de la página de login SISDEP
    LOGIN_PAGE_TITLE = "xpath=//h5[@class='L_2VJc3_']"
    USERNAME_FIELD = "id=usuario"
    PASSWORD_FIELD = "id=password"
    LOGIN_BUTTON = "xpath=//button[.//span[text()='Iniciar sesión']]"
    ERROR_MESSAGE = "xpath=//div[contains(@class, 'ant-message-error')]"
    SUCCESS_MESSAGE = "xpath=//span[text()='Administrador']"
    LOGOUT_BUTTON = "xpath=//li[contains(@class, 'ant-dropdown-menu-item')]//span[text()='Cerrar sesión']"
    MENSAJE_USUARIO_INACTIVO = "xpath=//div[contains(@class,'ant-alert-message') and contains(text(),'Usuario no activado por el administrador')]"
    
    # Mensajes esperados
    LOGIN_ERROR_MSG = "Error accediendo"
    
    def __init__(self, page: Page):
        self.page = page
    
    def navegar_a_sisdep(self):
        """
        Navega a la página principal de SISDEP
        Equivalente a: Navegar A SISDEP
        """
        self.page.goto(SISDEP_URL)
        verificar_elemento_presente(self.page, self.LOGIN_PAGE_TITLE)
    
    def ingresar_usuario_sisdep(self, usuario: str):
        """
        Ingresa el nombre de usuario en SISDEP
        Equivalente a: Ingresar Usuario SISDEP
        """
        ingresar_texto(self.page, self.USERNAME_FIELD, usuario)
    
    def ingresar_contraseña_sisdep(self, contraseña: str):
        """
        Ingresa la contraseña en SISDEP
        Equivalente a: Ingresar Contraseña SISDEP
        """
        ingresar_texto(self.page, self.PASSWORD_FIELD, contraseña)
    
    def hacer_click_en_login_sisdep(self):
        """
        Hace click en el botón de login de SISDEP
        Equivalente a: Hacer Click En Login SISDEP
        """
        hacer_click_en_elemento(self.page, self.LOGIN_BUTTON)
    
    def realizar_login_sisdep(self, usuario: str, contraseña: str):
        """
        Realiza el proceso completo de login en SISDEP
        Equivalente a: Realizar Login SISDEP
        """
        self.ingresar_usuario_sisdep(usuario)
        self.ingresar_contraseña_sisdep(contraseña)
        self.hacer_click_en_login_sisdep()
    
    def verificar_login_exitoso_sisdep(self):
        """
        Verifica que el login en SISDEP fue exitoso
        Equivalente a: Verificar Login Exitoso SISDEP
        """
        verificar_elemento_presente(self.page, self.SUCCESS_MESSAGE)
    
    def verificar_login_fallido_sisdep(self, mensaje_error: str):
        """
        Verifica que el login en SISDEP falló
        Equivalente a: Verificar Login Fallido SISDEP
        """
        verificar_texto_en_pagina(self.page, mensaje_error)
    
    def verificar_mensaje_de_error_sisdep(self, mensaje: str):
        """
        Verifica que se muestre un mensaje de error específico en SISDEP
        Equivalente a: Verificar Mensaje De Error SISDEP
        """
        verificar_texto_en_pagina(self.page, mensaje)
    
    def limpiar_campos_de_login_sisdep(self):
        """
        Limpia los campos de usuario y contraseña en SISDEP
        Equivalente a: Limpiar Campos De Login SISDEP
        """
        limpiar_campo(self.page, self.USERNAME_FIELD)
        limpiar_campo(self.page, self.PASSWORD_FIELD)
    
    def verificar_elementos_de_login_sisdep_presentes(self):
        """
        Verifica que todos los elementos de la página de login de SISDEP estén presentes
        Equivalente a: Verificar Elementos De Login SISDEP Presentes
        """
        verificar_elemento_presente(self.page, self.LOGIN_PAGE_TITLE)
        verificar_elemento_presente(self.page, self.USERNAME_FIELD)
        verificar_elemento_presente(self.page, self.PASSWORD_FIELD)
        verificar_elemento_presente(self.page, self.LOGIN_BUTTON)
    
    def verificar_elemento_presente(self, locator: str, timeout: Optional[int] = None):
        """
        Método helper para verificar elemento presente
        """
        verificar_elemento_presente(self.page, locator, timeout)
    
    def verificar_usuario_inactivo(self):
        """
        Verifica que el usuario no puede iniciar sesión y recibe un mensaje de error claro.
        Equivalente a: Verificar Usuario Inactivo
        """
        import time
        time.sleep(2)
        verificar_texto_en_pagina(self.page, "Usuario no activado por el administrador.")

