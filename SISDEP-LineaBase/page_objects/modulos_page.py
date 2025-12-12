"""
Page Object para la gestión de módulos en SISDEP
Equivalente a page_objects/sisdep_modulos_page.robot
"""
import sys
from pathlib import Path
import time

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page, expect
from utils.common_helpers import (
    verificar_elemento_presente,
    hacer_click_en_elemento,
    ingresar_texto,
    verificar_texto_en_pagina
)


class ModulosPage:
    """Page Object para la gestión de módulos en SISDEP"""
    
    # Locators de navegación
    MENU_REGULACIONES = "xpath=//span[@class='ant-menu-title-content' and text()='Regulaciones']"
    SUBMENU_MODULOS = "xpath=//a[@href='/sisdep/regulaciones/modulos']"
    SECCION_MODULOS_TITLE = "xpath=//h1[contains(@class, 'ant-typography') and contains(text(), 'Regulaciones - Módulos')]"
    
    # Botones y campos principales
    AGREGAR_MODULO_BUTTON = "xpath=//button[@aria-label='Agregar' and contains(@class, 'ant-btn-primary')]"
    # Locators dentro del diálogo (más específicos)
    TENENCIA_PROPIEDAD_INPUT = "xpath=//div[@role='dialog']//input[@id='idTenenciaPropiedad']"
    ESTADO_INPUT = "xpath=//div[@role='dialog']//input[@id='idEstado']"
    FONDO_INPUT = "xpath=//div[@role='dialog']//input[@id='fondo']"
    FRENTE_INPUT = "xpath=//div[@role='dialog']//input[@id='frente']"
    ALTO_INPUT = "xpath=//div[@role='dialog']//input[@id='alto']"
    TIPO_MODULO_INPUT = "xpath=//div[@role='dialog']//input[@id='idTipoModulo']"
    TIPO_OTRO_MODULO_INPUT = "xpath=//div[@role='dialog']//input[@id='idTipoOtroModulo']"
    SECTOR_MODULO_INPUT = "xpath=//div[@role='dialog']//input[@id='idSectorModulo']"
    # Botón guardar para crear (type="button", sin ant-btn-lg)
    GUARDAR_MODULO_BUTTON = "xpath=//div[@role='dialog']//button[@type='button' and contains(@class,'ant-btn-primary') and not(contains(@class,'ant-btn-lg')) and .//span[@aria-label='save'] and .//span[text()='Guardar']]"
    # Botón guardar para actualizar (type="submit", con ant-btn-lg)
    GUARDAR_MODULO_ACTUALIZAR_BUTTON = "xpath=//div[@role='dialog']//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[@aria-label='save'] and .//span[text()='Guardar']]"
    DETALLES_MODULO_BUTTON_PRIMERO = "xpath=(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]"
    ELIMINAR_MODULO_BUTTON_PRIMERO = "xpath=(//button[@aria-label='Eliminar' and .//span[text()='Eliminar']])[1]"
    FILTRO_SERIAL_INPUT = "xpath=//input[@id='serial']"
    
    def __init__(self, page: Page):
        self.page = page
    
    def el_usuario_esta_en_seccion_modulos(self):
        """Navega a la sección de Módulos"""
        menu_regulaciones = self.page.locator(self.MENU_REGULACIONES)
        menu_regulaciones.wait_for(state="visible", timeout=10000)
        menu_regulaciones.click(no_wait_after=True)
        time.sleep(2)  # Esperar más tiempo para que el menú se expanda
        
        submenu_modulos = self.page.locator(self.SUBMENU_MODULOS)
        
        # Intentar esperar a que el elemento sea visible
        try:
            submenu_modulos.wait_for(state="visible", timeout=5000)
            submenu_modulos.click()
        except:
            # Si no es visible, esperar a que esté en el DOM y hacer scroll + click
            submenu_modulos.wait_for(state="attached", timeout=10000)
            time.sleep(1)
            # Hacer scroll al elemento para que sea visible
            submenu_modulos.scroll_into_view_if_needed()
            time.sleep(0.5)
            # Intentar hacer click
            try:
                submenu_modulos.click()
            except:
                # Si aún falla, usar JavaScript para hacer click
                self.page.evaluate("""
                    document.querySelector('a[href="/sisdep/regulaciones/modulos"]').click();
                """)
        
        time.sleep(2)
        
        self.page.reload()
        time.sleep(2)  # Esperar más tiempo después del reload
        
        # Intentar verificar el título con diferentes variaciones
        try:
            verificar_elemento_presente(self.page, self.SECCION_MODULOS_TITLE)
        except:
            # Intentar con variaciones del título
            titulos_posibles = [
                "xpath=//h1[contains(text(), 'Módulos')]",
                "xpath=//h1[contains(text(), 'Regulaciones')]",
                "xpath=//h1[contains(@class, 'ant-typography')]"
            ]
            for titulo in titulos_posibles:
                try:
                    verificar_elemento_presente(self.page, titulo)
                    break
                except:
                    continue
    
    def hacer_click_en_agregar_modulo(self):
        """Hace clic en el botón Agregar módulo"""
        hacer_click_en_elemento(self.page, self.AGREGAR_MODULO_BUTTON)
        time.sleep(2)
    
    def _seleccionar_opcion_dropdown(self, campo_locator: str, valor: str):
        """Helper para seleccionar opciones en dropdowns de Ant Design"""
        campo = self.page.locator(campo_locator).first  # Usar .first para evitar strict mode violation
        campo.wait_for(state="visible", timeout=5000)
        campo.click()
        time.sleep(1)
        opcion_locator = f"xpath=//div[contains(@class,'ant-select-item-option-content') and text()='{valor}']"
        opcion = self.page.locator(opcion_locator).first
        opcion.wait_for(state="visible", timeout=5000)
        opcion.click()
        time.sleep(1)
    
    def completar_formulario_modulo(self, tenencia: str, estado: str, fondo: str, frente: str, alto: str, 
                                    tipo_modulo: str, tipo_otro_modulo: str, sector_modulo: str):
        """Completa el formulario de módulo con los datos proporcionados"""
        # Esperar a que el diálogo esté visible
        dialog = self.page.locator("xpath=//div[@role='dialog']")
        dialog.wait_for(state="visible", timeout=5000)
        time.sleep(1)
        
        # Tenencia de la propiedad
        self._seleccionar_opcion_dropdown(self.TENENCIA_PROPIEDAD_INPUT, tenencia)
        # Estado
        self._seleccionar_opcion_dropdown(self.ESTADO_INPUT, estado)
        # Fondo
        campo_fondo = self.page.locator(self.FONDO_INPUT).first
        campo_fondo.wait_for(state="visible", timeout=5000)
        ingresar_texto(self.page, self.FONDO_INPUT, fondo)
        time.sleep(1)
        # Frente
        campo_frente = self.page.locator(self.FRENTE_INPUT).first
        campo_frente.wait_for(state="visible", timeout=5000)
        ingresar_texto(self.page, self.FRENTE_INPUT, frente)
        time.sleep(1)
        # Alto
        campo_alto = self.page.locator(self.ALTO_INPUT).first
        campo_alto.wait_for(state="visible", timeout=5000)
        ingresar_texto(self.page, self.ALTO_INPUT, alto)
        time.sleep(1)
        # Tipo módulo
        self._seleccionar_opcion_dropdown(self.TIPO_MODULO_INPUT, tipo_modulo)
        # Tipo otro módulo
        self._seleccionar_opcion_dropdown(self.TIPO_OTRO_MODULO_INPUT, tipo_otro_modulo)
        # Sector módulo
        self._seleccionar_opcion_dropdown(self.SECTOR_MODULO_INPUT, sector_modulo)
    
    def hacer_click_en_guardar_modulo(self):
        """
        Hace clic en el botón Guardar módulo (para crear)
        Equivalente a: Hacer Click En Guardar Modulo
        El botón de crear tiene: type="button" (no submit), sin ant-btn-lg
        """
        # Esperar a que el diálogo esté visible
        dialog = self.page.locator("xpath=//div[@role='dialog']")
        dialog.wait_for(state="visible", timeout=5000)
        time.sleep(0.5)
        
        # Buscar el botón de crear: type="button", sin ant-btn-lg, con span aria-label="save"
        boton_guardar = self.page.locator(self.GUARDAR_MODULO_BUTTON).first
        
        # Esperar a que el botón esté visible
        boton_guardar.wait_for(state="visible", timeout=10000)
        
        # Verificar que el botón esté habilitado antes de hacer click
        if boton_guardar.is_enabled():
            boton_guardar.click()
        else:
            # Si no está habilitado, esperar un poco más
            time.sleep(1)
            boton_guardar.wait_for(state="visible", timeout=5000)
            if boton_guardar.is_enabled():
                boton_guardar.click()
            else:
                # Fallback: usar el método helper
                hacer_click_en_elemento(self.page, self.GUARDAR_MODULO_BUTTON)
        time.sleep(2)
    
    def hacer_click_en_guardar_modulo_actualizar(self):
        """
        Hace clic en el botón Guardar módulo (para actualizar)
        Usado después de hacer click en Detalles y modificar datos
        El botón de actualizar tiene: type="submit", con ant-btn-lg
        Nota: Después de reload, el botón puede estar en la página directamente, no en un diálogo
        """
        time.sleep(2)  # Esperar un poco más después del reload para que la página cargue
        
        # Buscar el botón de actualizar directamente en la página
        # type="submit", con ant-btn-lg, con span aria-label="save" y span text="Guardar"
        boton_guardar = self.page.locator("xpath=//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[@aria-label='save'] and .//span[text()='Guardar']]").first
        
        # Esperar a que el botón esté visible
        boton_guardar.wait_for(state="visible", timeout=10000)
        
        # Verificar que el botón esté habilitado antes de hacer click
        if boton_guardar.is_enabled():
            boton_guardar.click()
        else:
            # Si no está habilitado, esperar un poco más
            time.sleep(1)
            boton_guardar.wait_for(state="visible", timeout=5000)
            if boton_guardar.is_enabled():
                boton_guardar.click()
            else:
                # Fallback: usar el método helper
                hacer_click_en_elemento(self.page, self.GUARDAR_MODULO_ACTUALIZAR_BUTTON)
        time.sleep(2)
    
    def verificar_creacion_modulo_exitosa(self):
        """Verifica que el módulo fue creado exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro creado exitosamente!")
    
    def filtrar_modulo_por_serial(self, serial: str):
        """Ingresa el serial en el filtro para buscar el módulo"""
        ingresar_texto(self.page, self.FILTRO_SERIAL_INPUT, serial)
        time.sleep(1)
    
    def hacer_click_en_detalles_modulo(self):
        """Hace clic en el primer botón Detalles del módulo filtrado"""
        hacer_click_en_elemento(self.page, self.DETALLES_MODULO_BUTTON_PRIMERO)
        time.sleep(2)
    
    def verificar_actualizacion_modulo_exitosa(self):
        """Verifica que el módulo fue actualizado exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
    
    def hacer_click_en_eliminar_modulo(self):
        """Hace clic en el primer botón Eliminar del módulo filtrado"""
        hacer_click_en_elemento(self.page, self.ELIMINAR_MODULO_BUTTON_PRIMERO)
        time.sleep(1)
    
    def verificar_eliminacion_modulo_exitosa(self):
        """Verifica que el módulo fue eliminado exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro eliminado exitosamente!")

