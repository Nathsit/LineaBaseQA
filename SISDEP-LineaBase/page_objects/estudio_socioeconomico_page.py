"""
Page Object para la sección de Estudio Socioeconómico en SISDEP
Equivalente a page_objects/sisdep_estudio_socioeconomico_page.robot
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


class EstudioSocioeconomicoPage:
    """Page Object para la sección de Estudio Socioeconómico en SISDEP"""
    
    # Navegación
    MENU_PERSONAS = "xpath=//div[@role='menuitem' and .//span[text()='Social']]"
    SUBMENU_VISITAS_ASIGNADAS = "xpath=//a[@href='/sisdep/social/visitas-asignadas']"
    
    # Filtros - Buscar los selects por el span que muestra el valor seleccionado
    FILTRO_ANIO_SELECT = "xpath=//span[@class='ant-select-selection-item']"  # Primer span (año)
    FILTRO_MES_SELECT = "xpath=(//span[@class='ant-select-selection-item'])[2]"  # Segundo span (mes)
    
    # Calendario y botones
    DIA_ESTUDIO_CALENDARIO = "xpath=(//div[contains(@class,'ant-picker-calendar-date-content') and .//span[@class='ant-badge BleNtNoI']])[1]"
    DETALLES_ESTUDIO_BUTTON = "xpath=(//button[.//span[text()='Actualización -'] and .//span[text()='Detalles']])[1]"
    GUARDAR_ESTUDIO_BUTTON = "xpath=//button[@type='button' and .//span[text()='Guardar']]"
    DIA_ESTUDIO_CALENDARIO_PDF = "xpath=(//div[contains(@class,'ant-picker-calendar-date-content') and .//span[@role='img' and @aria-label='file-exclamation']])[1]"
    BOTON_PDF = "xpath=//button[.//span[@role='img' and @aria-label='file-pdf'] and .//span[contains(text(),'Concepto socioeconómico FO-GGOL-016')]]"
    BOTON_CERRAR_MODAL = "xpath=//span[contains(@class,'ant-modal-close-x')]"
    
    def __init__(self, page: Page):
        self.page = page
    
    def ir_a_seccion_estudio_socioeconomico(self):
        """Navega al menú Social > Visitas domiciliarias asignadas"""
        menu_personas = self.page.locator(self.MENU_PERSONAS)
        menu_personas.wait_for(state="visible", timeout=10000)
        menu_personas.click(no_wait_after=True)
        time.sleep(1)
        
        submenu_visitas = self.page.locator(self.SUBMENU_VISITAS_ASIGNADAS)
        submenu_visitas.wait_for(state="visible", timeout=10000)
        submenu_visitas.click()
        time.sleep(2)
        self.page.reload()
    
    def filtrar_estudio_por_fecha(self, anio: str, mes: str):
        """Aplica el filtro de año y mes en la sección de estudio socioeconómico"""
        time.sleep(2)  # Esperar a que la página cargue completamente
        
        # Filtro año - hacer click en el primer span que muestra el valor seleccionado
        filtro_anio = self.page.locator(self.FILTRO_ANIO_SELECT).first
        filtro_anio.wait_for(state="visible", timeout=10000)
        filtro_anio.click()
        time.sleep(1)
        
        # Seleccionar la opción del año
        opcion_anio = self.page.locator(f"xpath=//div[@class='ant-select-item-option-content' and text()='{anio}']").first
        opcion_anio.wait_for(state="visible", timeout=5000)
        opcion_anio.click()
        time.sleep(1)
        
        # Filtro mes - hacer click en el segundo span que muestra el valor seleccionado
        filtro_mes = self.page.locator(self.FILTRO_MES_SELECT)
        filtro_mes.wait_for(state="visible", timeout=10000)
        filtro_mes.click()
        time.sleep(1)
        
        # Seleccionar la opción del mes (ej: "jul." o "abr.")
        opcion_mes = self.page.locator(f"xpath=//div[@class='ant-select-item-option-content' and text()='{mes}']").first
        opcion_mes.wait_for(state="visible", timeout=5000)
        opcion_mes.click()
        time.sleep(1)
    
    def seleccionar_estudio_socioeconomico_en_calendario(self):
        """Selecciona el día en el calendario y abre el estudio socioeconómico"""
        # Usar .first para evitar strict mode violation
        dia_calendario = self.page.locator(self.DIA_ESTUDIO_CALENDARIO).first
        dia_calendario.wait_for(state="visible", timeout=10000)
        dia_calendario.click()
        time.sleep(1)
        
        # Usar .first para el botón de detalles
        boton_detalles = self.page.locator(self.DETALLES_ESTUDIO_BUTTON).first
        boton_detalles.wait_for(state="visible", timeout=10000)
        boton_detalles.click()
        time.sleep(2)
    
    def guardar_formularios_estudio_varias_veces(self, veces: int = 7):
        """Hace clic varias veces en el botón Guardar y espera el mensaje de éxito"""
        for i in range(veces):
            hacer_click_en_elemento(self.page, self.GUARDAR_ESTUDIO_BUTTON)
            time.sleep(1)
    
    def generar_pdf_estudio_socioeconomico(self):
        """Hace clic en el botón PDF del estudio socioeconómico"""
        # Verificar si hay un modal abierto y cerrarlo primero
        try:
            modal_close = self.page.locator(self.BOTON_CERRAR_MODAL)
            if modal_close.is_visible():
                modal_close.click()
                time.sleep(1)
        except:
            pass
        
        # Usar .first para evitar strict mode violation
        dia_calendario_pdf = self.page.locator(self.DIA_ESTUDIO_CALENDARIO_PDF).first
        dia_calendario_pdf.wait_for(state="visible", timeout=10000)
        
        # Si hay un modal interceptando, usar force=True
        try:
            dia_calendario_pdf.click()
        except:
            # Si falla, intentar con force=True
            dia_calendario_pdf.click(force=True)
        
        time.sleep(1)
        
        # Usar .first para el botón de detalles
        boton_detalles = self.page.locator(self.DETALLES_ESTUDIO_BUTTON).first
        boton_detalles.wait_for(state="visible", timeout=10000)
        boton_detalles.click()
        time.sleep(2)
    
    def actualizar_estudio_socioeconomico(self, anio: str, mes: str):
        """Actualiza un estudio socioeconómico.
        Flujo: Filtrar por fecha -> Seleccionar en calendario -> Detalles -> Guardar"""
        # Filtrar por fecha
        self.filtrar_estudio_por_fecha(anio, mes)
        time.sleep(2)  # Esperar a que se filtre
        
        # Seleccionar el estudio en el calendario (esto abre los detalles)
        self.seleccionar_estudio_socioeconomico_en_calendario()
        time.sleep(2)  # Esperar a que se abra el modal o la página
        
        # Esperar a que la página o modal cargue
        self.page.wait_for_load_state("networkidle", timeout=10000)
        time.sleep(1)
        
        # Clic en el botón Guardar (type="submit" con ant-btn-lg)
        boton_guardar = self.page.locator("xpath=//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[text()='Guardar']]").first
        boton_guardar.wait_for(state="visible", timeout=15000)
        boton_guardar.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_guardar.click()
        time.sleep(2)
    
    def verificar_actualizacion_estudio_exitosa(self):
        """Verifica que el estudio socioeconómico fue actualizado exitosamente"""
        time.sleep(1)
        # Buscar el mensaje de éxito específico
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
        


