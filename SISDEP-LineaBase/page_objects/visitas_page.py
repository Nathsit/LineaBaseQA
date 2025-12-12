"""
Page Object para la asignación de visitas domiciliarias en SISDEP
Equivalente a page_objects/sisdep_visitas_page.robot
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


class VisitasPage:
    """Page Object para la asignación de visitas domiciliarias en SISDEP"""
    
    # Navegación
    MENU_REGULACIONES = "xpath=//span[@class='ant-menu-title-content' and text()='Regulaciones']"
    SUBMENU_ASIGNACION_VISITAS = "xpath=//a[@href='/sisdep/regulaciones/asignacion-visitas' and text()='Asignación de visitas domiciliarias']"
    SECCION_VISITAS_TITLE = "xpath=//h1[text()='Regulaciones - Asignación de visitas domiciliarias']"
    
    # Botones y campos principales
    NUEVA_VISITA_BUTTON = "xpath=//button[@aria-label='Nueva visita' and .//span[text()='Nueva visita']]"
    BUSCAR_VENTERO_INPUT = "id=documento"
    BUSCAR_VENTERO_BUTTON = "xpath=//button[.//span[text()='Buscar']]"
    GUARDAR_VISITA_BUTTON = "xpath=//button[.//span[text()='Guardar']]"
    DETALLES_VISITA_BUTTON_PRIMERO = "xpath=(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]"
    ACTUALIZAR_VISITA_BUTTON_PRIMERO = "xpath=(//button[.//span[text()='Actualizar']])[1]"
    ELIMINAR_VISITA_BUTTON_PRIMERO = "xpath=(//button[@aria-label='Remover' and .//span[text()='Remover']])[1]"
    CONFIRMAR_ELIMINAR_VISITA_BUTTON = "xpath=//button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]"
    
    # Campos del formulario
    VISITADOR_DROPDOWN = "id=idVisitador"
    TIPO_VISITA_DROPDOWN = "id=idTipo"
    VEHICULO_DROPDOWN = "id=idVehiculo"
    FRANJA_HORARIA_DROPDOWN = "id=idFranja"
    FECHA_VISITA_INPUT = "id=fechaVisita"
    FECHA_VISITA_TODAY_BUTTON = "xpath=//a[contains(@class,'ant-picker-today-btn') and text()='Today']"
    FECHA_EJECUCION_INPUT = "id=fechaEjecucion"
    FECHA_EJECUCION_HASTA_INPUT = "xpath=//input[@placeholder='Hasta']"
    VISITADOR_ACTUALIZAR_DROPDOWN = "id=visitador"
    
    def __init__(self, page: Page):
        self.page = page
    
    def el_usuario_esta_en_seccion_asignacion_visitas(self):
        """Navega a la sección de Asignación de Visitas"""
        menu_regulaciones = self.page.locator(self.MENU_REGULACIONES)
        menu_regulaciones.wait_for(state="visible", timeout=10000)
        menu_regulaciones.click(no_wait_after=True)
        time.sleep(1)
        
        submenu_visitas = self.page.locator(self.SUBMENU_ASIGNACION_VISITAS)
        submenu_visitas.wait_for(state="visible", timeout=10000)
        submenu_visitas.click()
        time.sleep(2)
        self.page.reload()
        verificar_elemento_presente(self.page, self.SECCION_VISITAS_TITLE)
    
    def hacer_click_en_nueva_visita(self):
        """Hace clic en el botón Nueva visita"""
        hacer_click_en_elemento(self.page, self.NUEVA_VISITA_BUTTON)
        time.sleep(2)
    
    def buscar_ventero_por_documento_en_visitas(self, documento: str):
        """Busca un ventero por su número de documento en la sección de visitas"""
        ingresar_texto(self.page, self.BUSCAR_VENTERO_INPUT, documento)
        time.sleep(1)
        hacer_click_en_elemento(self.page, self.BUSCAR_VENTERO_BUTTON)
        time.sleep(2)
    
    def _seleccionar_opcion_dropdown(self, campo_locator: str, valor: str):
        """Helper para seleccionar opciones en dropdowns"""
        campo = self.page.locator(campo_locator)
        campo.wait_for(state="visible", timeout=5000)
        campo.click()
        time.sleep(1)
        opcion_locator = f"xpath=//div[@class='ant-select-item-option-content' and text()='{valor}']"
        opcion = self.page.locator(opcion_locator).first
        opcion.wait_for(state="visible", timeout=5000)
        opcion.click()
        time.sleep(1)
    
    def _seleccionar_fecha_hoy(self, campo_id: str):
        """Helper para seleccionar la fecha de hoy en un date picker"""
        campo = self.page.locator(f"#{campo_id}")
        campo.wait_for(state="visible", timeout=5000)
        # Remover atributo readonly si existe
        self.page.evaluate(f"document.getElementById('{campo_id}').removeAttribute('readonly')")
        campo.click()
        time.sleep(1)
        # Hacer click en el botón "Today" del date picker
        today_button = self.page.locator(self.FECHA_VISITA_TODAY_BUTTON)
        if today_button.is_visible():
            today_button.click()
        time.sleep(1)
    
    def completar_formulario_visita(self, visitador: str, tipo_visita: str, vehiculo: str, fecha: str, franja: str):
        """Completa el formulario de visita con los datos proporcionados"""
        # Visitador
        self._seleccionar_opcion_dropdown(self.VISITADOR_DROPDOWN, visitador)
        # Tipo de visita
        self._seleccionar_opcion_dropdown(self.TIPO_VISITA_DROPDOWN, tipo_visita)
        # Vehículo
        self._seleccionar_opcion_dropdown(self.VEHICULO_DROPDOWN, vehiculo)
        # Fecha de la visita (si es "HOY", seleccionar hoy)
        if fecha.upper() == "HOY":
            self._seleccionar_fecha_hoy(self.FECHA_VISITA_INPUT.split("=")[-1])
        else:
            ingresar_texto(self.page, self.FECHA_VISITA_INPUT, fecha)
        # Franja horaria
        self._seleccionar_opcion_dropdown(self.FRANJA_HORARIA_DROPDOWN, franja)
    
    def hacer_click_en_guardar_visita(self):
        """Hace clic en el botón Guardar visita"""
        hacer_click_en_elemento(self.page, self.GUARDAR_VISITA_BUTTON)
        time.sleep(2)
    
    def verificar_creacion_visita_exitosa(self):
        """Verifica que la visita fue creada exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro creado exitosamente!")
    
    def actualizar_datos_visita(self, fecha_desde: str, fecha_hasta: str, visitador: str):
        """Actualiza los datos de la visita asignada"""
        # Fecha de ejecución (Desde)
        self.page.evaluate("document.getElementById('fechaEjecucion').removeAttribute('readonly')")
        ingresar_texto(self.page, self.FECHA_EJECUCION_INPUT, fecha_desde)
        time.sleep(1)
        # Fecha de ejecución (Hasta)
        hasta_input = self.page.locator(self.FECHA_EJECUCION_HASTA_INPUT)
        self.page.evaluate("document.evaluate(\"//input[@placeholder='Hasta']\",document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.removeAttribute('readonly')")
        ingresar_texto(self.page, self.FECHA_EJECUCION_HASTA_INPUT, fecha_hasta)
        time.sleep(1)
        # Visitador
        self._seleccionar_opcion_dropdown(self.VISITADOR_ACTUALIZAR_DROPDOWN, visitador)
    
    def hacer_click_en_detalles_visita(self):
        """Hace clic en el primer botón Detalles de la lista de visitas"""
        hacer_click_en_elemento(self.page, self.DETALLES_VISITA_BUTTON_PRIMERO)
        time.sleep(2)
    
    def hacer_click_en_actualizar_visita(self):
        """Hace clic en el primer botón Actualizar visita"""
        hacer_click_en_elemento(self.page, self.ACTUALIZAR_VISITA_BUTTON_PRIMERO)
        time.sleep(2)
    
    def verificar_actualizacion_visita_exitosa(self):
        """Verifica que la visita fue actualizada exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
    
    def hacer_click_en_eliminar_visita(self):
        """Hace clic en el primer botón Remover de la lista de visitas"""
        hacer_click_en_elemento(self.page, self.ELIMINAR_VISITA_BUTTON_PRIMERO)
        time.sleep(1)
    
    def confirmar_eliminacion_visita(self):
        """Confirma la eliminación de la visita"""
        hacer_click_en_elemento(self.page, self.CONFIRMAR_ELIMINAR_VISITA_BUTTON)
        time.sleep(2)
    
    def verificar_eliminacion_visita_exitosa(self):
        """Verifica que la visita fue eliminada exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro eliminado exitosamente!")

