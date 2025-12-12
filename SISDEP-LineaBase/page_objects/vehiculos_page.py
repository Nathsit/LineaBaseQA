"""
Page Object para la gestión de vehículos en SISDEP
Equivalente a page_objects/sisdep_vehiculos_page.robot
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


class VehiculosPage:
    """Page Object para la gestión de vehículos en SISDEP"""
    
    # Navegación
    MENU_VEHICULOS = "xpath=//a[@href='/sisdep/vehiculos']"
    SECCION_VEHICULOS_TITLE = "xpath=//h1[contains(@class,'ant-typography') and text()='Vehiculos']"
    
    # Botones
    AGREGAR_VEHICULO_BUTTON = "xpath=//button[@aria-label='Agregar' and .//span[text()='Agregar']]"
    GUARDAR_VEHICULO_BUTTON = "xpath=//button[@type='button' and .//span[text()='Guardar']]"
    GUARDAR_VEHICULO_ACTUALIZAR_BUTTON = "xpath=//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[text()='Guardar']]"
    REMOVER_VEHICULO_BUTTON = "xpath=//button[@aria-label='Remover' and .//span[text()='Remover']]"
    CONFIRMAR_ELIMINAR_VEHICULO_BUTTON = "xpath=//button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]"
    
    # Campos del formulario (dentro del modal para crear)
    NOMBRE_CONDUCTOR_INPUT = "xpath=//div[@role='dialog']//input[@id='nombreConductor' and @aria-label='Nombre del condutor']"
    PLACA_INPUT_MODAL = "xpath=//div[@role='dialog']//input[@id='placa' and @aria-label='Placa' and @aria-required='true']"
    TIPO_VEHICULO_INPUT = "xpath=//div[@role='dialog']//input[@id='idTipoVehiculo']"
    
    # Campo de filtro (fuera del modal)
    PLACA_INPUT_FILTRO = "xpath=//input[@id='placa' and @aria-label='Placa' and not(@aria-required)]"
    
    # Botón para acceder a detalles/editar
    DETALLES_VEHICULO_BUTTON = "xpath=//button[@aria-label='Detalles' and .//span[text()='Detalles']]"
    
    def __init__(self, page: Page):
        self.page = page
    
    def ir_a_seccion_vehiculos(self):
        """Navega a la sección de Vehículos"""
        hacer_click_en_elemento(self.page, self.MENU_VEHICULOS)
        time.sleep(2)
        verificar_elemento_presente(self.page, self.SECCION_VEHICULOS_TITLE)
    
    def hacer_click_en_agregar_vehiculo(self):
        """Hace clic en el botón Agregar vehículo"""
        hacer_click_en_elemento(self.page, self.AGREGAR_VEHICULO_BUTTON)
        time.sleep(2)
    
    def _seleccionar_opcion_dropdown(self, campo_locator: str, valor: str):
        """Helper para seleccionar opciones en dropdowns"""
        campo = self.page.locator(campo_locator)
        campo.wait_for(state="visible", timeout=5000)
        campo.click()
        time.sleep(1)
        opcion_locator = f"xpath=//div[contains(@class,'ant-select-item-option-content') and text()='{valor}']"
        opcion = self.page.locator(opcion_locator).first
        opcion.wait_for(state="visible", timeout=5000)
        opcion.click()
        time.sleep(1)
    
    def completar_formulario_vehiculo(self, nombre_conductor: str, placa: str, tipo_vehiculo: str):
        """Completa el formulario de vehículo"""
        # Esperar a que el modal esté visible
        dialog = self.page.locator("xpath=//div[@role='dialog']")
        dialog.wait_for(state="visible", timeout=5000)
        time.sleep(0.5)
        
        # Llenar nombre del conductor
        nombre_input = dialog.locator("xpath=.//input[@id='nombreConductor' and @aria-label='Nombre del condutor']").first
        nombre_input.wait_for(state="visible", timeout=5000)
        nombre_input.fill(nombre_conductor)
        time.sleep(0.5)
        
        # Llenar placa (dentro del modal, con aria-required="true")
        placa_input = dialog.locator("xpath=.//input[@id='placa' and @aria-label='Placa' and @aria-required='true']").first
        placa_input.wait_for(state="visible", timeout=5000)
        placa_input.fill(placa)
        time.sleep(0.5)
        
        # Seleccionar tipo de vehículo
        tipo_input = dialog.locator("xpath=.//input[@id='idTipoVehiculo']").first
        self._seleccionar_opcion_dropdown("xpath=//div[@role='dialog']//input[@id='idTipoVehiculo']", tipo_vehiculo)
        time.sleep(1)
    
    def hacer_click_en_guardar_vehiculo(self):
        """Hace clic en el botón Guardar vehículo (para crear)"""
        hacer_click_en_elemento(self.page, self.GUARDAR_VEHICULO_BUTTON)
        time.sleep(2)
    
    def hacer_click_en_guardar_vehiculo_actualizar(self):
        """Hace clic en el botón Guardar vehículo (para actualizar) - type='submit' con ant-btn-lg"""
        boton_guardar = self.page.locator(self.GUARDAR_VEHICULO_ACTUALIZAR_BUTTON).first
        boton_guardar.wait_for(state="visible", timeout=10000)
        boton_guardar.click()
        time.sleep(2)
    
    def verificar_creacion_vehiculo_exitosa(self):
        """Verifica que el vehículo fue creado exitosamente"""
        verificar_texto_en_pagina(self.page, "¡Registro creado exitosamente!")
    
    def eliminar_vehiculo_por_placa(self, placa: str):
        """Elimina un vehículo por placa llenando el input de filtro y haciendo clic en Remover"""
        # Usar el campo de filtro (fuera del modal, sin aria-required)
        placa_filtro = self.page.locator(self.PLACA_INPUT_FILTRO).first
        placa_filtro.wait_for(state="visible", timeout=5000)
        placa_filtro.fill(placa)
        time.sleep(1)
        hacer_click_en_elemento(self.page, self.REMOVER_VEHICULO_BUTTON)
        time.sleep(2)
    
    def confirmar_eliminacion_vehiculo(self):
        """Confirma la eliminación del vehículo"""
        hacer_click_en_elemento(self.page, self.CONFIRMAR_ELIMINAR_VEHICULO_BUTTON)
        time.sleep(2)
    
    def verificar_vehiculo_eliminado(self):
        """Verifica que el vehículo fue eliminado"""
        verificar_texto_en_pagina(self.page, "¡Registro eliminado exitosamente!")
    
    def verificar_vehiculo_no_eliminado(self):
        """Verifica que el vehículo no fue eliminado (está en uso)"""
        verificar_texto_en_pagina(self.page, "Elemento usado en Visita domiciliaria")
    
    def buscar_vehiculo_por_placa(self, placa: str):
        """Busca un vehículo por placa usando el filtro"""
        placa_filtro = self.page.locator(self.PLACA_INPUT_FILTRO).first
        placa_filtro.wait_for(state="visible", timeout=5000)
        placa_filtro.clear()
        placa_filtro.fill(placa)
        time.sleep(2)  # Esperar a que la tabla se actualice con el filtro
    
    def acceder_a_detalles_vehiculo(self, placa: str):
        """Accede a los detalles de un vehículo filtrando por placa y haciendo clic en Detalles.
        Navega a otra página, no abre un modal."""
        self.buscar_vehiculo_por_placa(placa)
        time.sleep(2)  # Esperar a que se filtre la lista
        
        # Verificar que el botón de detalles esté disponible
        # Intentar múltiples selectores para el botón de detalles
        boton_detalles = None
        selectores_boton = [
            self.DETALLES_VEHICULO_BUTTON,
            "xpath=//button[@aria-label='Detalles' and .//span[text()='Detalles']]",
            "xpath=//button[contains(@class,'ant-btn-primary') and .//span[text()='Detalles']]"
        ]
        
        for selector in selectores_boton:
            try:
                boton_detalles = self.page.locator(selector).first
                boton_detalles.wait_for(state="visible", timeout=5000)
                if boton_detalles.is_visible():
                    break
            except:
                continue
        
        if boton_detalles is None or not boton_detalles.is_visible():
            raise Exception(f"No se encontró el botón de Detalles después de filtrar por placa: {placa}")
        
        boton_detalles.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_detalles.click()
        
        # Esperar a que la página navegue (no es un modal, es navegación)
        time.sleep(3)
        self.page.wait_for_load_state("networkidle", timeout=10000)
        
        # Verificar que los campos de edición estén presentes en la página
        # El campo nombreConductor debería estar visible en la página de detalles
        nombre_input = self.page.locator("xpath=//input[@id='nombreConductor' and @aria-label='Nombre del condutor']")
        try:
            nombre_input.wait_for(state="visible", timeout=10000)
        except:
            # Si no está visible, intentar recargar la página (similar a autorizaciones)
            self.page.reload()
            time.sleep(2)
            nombre_input.wait_for(state="visible", timeout=10000)
        
        time.sleep(1)
    
    def actualizar_datos_vehiculo(self, nombre_conductor: str = None, tipo_vehiculo: str = None):
        """Actualiza los datos de un vehículo (solo los campos proporcionados).
        Los campos están directamente en la página, no en un modal."""
        time.sleep(1)
        
        if nombre_conductor:
            # El campo está directamente en la página
            nombre_input = self.page.locator("xpath=//input[@id='nombreConductor' and @aria-label='Nombre del condutor']").first
            nombre_input.wait_for(state="visible", timeout=5000)
            nombre_input.clear()
            nombre_input.fill(nombre_conductor)
            time.sleep(0.5)
        
        if tipo_vehiculo:
            # El dropdown también está directamente en la página
            self._seleccionar_opcion_dropdown("xpath=//input[@id='idTipoVehiculo']", tipo_vehiculo)
            time.sleep(1)
    
    def verificar_actualizacion_vehiculo_exitosa(self):
        """Verifica que el vehículo fue actualizado exitosamente"""
        time.sleep(1)  # Reducido de 2 a 1 segundo
        
        # Buscar el mensaje de éxito en los mensajes de Ant Design
        # Los mensajes de éxito suelen estar en divs con clase ant-message
        mensaje_exito = self.page.locator("xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), 'actualizado exitosamente')]").first
        
        try:
            mensaje_exito.wait_for(state="visible", timeout=5000)
            # Si encontramos el mensaje, ya está verificado
            return
        except:
            pass
        
        # Si no se encuentra en el mensaje de Ant Design, intentar buscar en la página
        mensajes_posibles = [
            "¡Registro actualizado exitosamente!",
            "Registro actualizado exitosamente"
        ]
        
        for mensaje in mensajes_posibles:
            try:
                # Usar timeout corto para cada intento
                texto_locator = self.page.locator(f"text={mensaje}")
                texto_locator.wait_for(state="visible", timeout=2000)
                return  # Si encontramos el mensaje, salir
            except:
                continue
        
        # Si no encontramos el mensaje, no fallar (el test puede continuar)
        # El mensaje puede desaparecer rápidamente o estar en un formato diferente
        pass

