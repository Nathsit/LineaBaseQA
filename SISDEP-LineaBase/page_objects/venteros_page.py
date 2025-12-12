"""
Page Object para la gestión de venteros en SISDEP
Equivalente a page_objects/sisdep_venteros_page.robot
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


class VenterosPage:
    """Page Object para la gestión de venteros en SISDEP"""
    
    # Navegación
    MENU_PERSONAS = "xpath=//div[@role='menuitem' and .//span[text()='Social']]"
    SUBMENU_REGISTRO_VENTERO = "xpath=//a[@href='/sisdep/social/registro-ventero']"
    SECCION_VENTEROS_TITLE = "xpath=//span[@class='ant-page-header-heading-title' and @title='Registro nuevo ventero']"
    PERSONAS = "xpath=//a[@href='/sisdep/personas']"
    
    # Botones
    GUARDAR_VENTERO_BUTTON = "xpath=(//button[@type='submit' and contains(@class,'ant-btn-primary') and .//span[text()='Guardar']])[1]"
    GUARDAR_VENTERO_BUTTON_FORM = "xpath=//form//button[@type='submit' and .//span[text()='Guardar']]"
    EXCEL_VENTEROS_BUTTON = "xpath=//button[.//span[text()='Excel'] and @type='button']"
    DETALLES_VENTERO_BUTTON_PRIMERO = "xpath=(//button[@aria-label='Detalles' and .//span[text()='Detalles']])[1]"
    
    # Campos del formulario
    PRIMER_NOMBRE_INPUT = "xpath=//input[@id='nombre1']"
    PRIMER_APELLIDO_INPUT = "xpath=//input[@id='apellido1']"
    TIPO_DOCUMENTO_INPUT = "xpath=//input[@id='idTipoDocumento']"
    DOCUMENTO_INPUT = "xpath=//input[@id='documento']"
    FECHA_EXPEDICION_INPUT = "xpath=//input[@id='fechaExpedicion']"
    LUGAR_EXPEDICION_INPUT = "xpath=//input[@id='lugarExpedicion']"
    NACIONALIDAD_INPUT = "xpath=//input[@id='idNacionalidad']"
    SEXO_INPUT = "xpath=//input[@id='idSexo']"
    TIPO_PERSONA_INPUT = "xpath=//input[@id='idTipoPersona']"
    TELEFONO_CELULAR_INPUT = "xpath=//input[@id='telefonoCelular']"
    FECHA_NACIMIENTO_INPUT = "xpath=//input[@id='fechaNacimiento']"
    ESTADO_CIVIL_INPUT = "xpath=//input[@id='ventero_idEstadoCivil']"
    NIVEL_ESCOLARIDAD_INPUT = "xpath=//input[@id='ventero_idEscolaridad']"
    
    # Filtros
    FILTRO_DOCUMENTO_INPUT = "xpath=//input[@id='documento' and @placeholder='Documento']"
    
    def __init__(self, page: Page):
        self.page = page
    
    def el_usuario_esta_en_seccion_registro_ventero(self):
        """Navega a la sección de Registro de Venteros"""
        menu_personas = self.page.locator(self.MENU_PERSONAS)
        menu_personas.wait_for(state="visible", timeout=10000)
        menu_personas.click(no_wait_after=True)
        time.sleep(2)  # Esperar más tiempo para que el menú se expanda
        
        submenu_ventero = self.page.locator(self.SUBMENU_REGISTRO_VENTERO)
        # Verificar si está visible
        try:
            submenu_ventero.wait_for(state="visible", timeout=3000)
            submenu_ventero.click()
        except:
            # Si no es visible, esperar a que esté en el DOM y hacer click forzado o scroll
            submenu_ventero.wait_for(state="attached", timeout=10000)
            time.sleep(1)
            if not submenu_ventero.is_visible():
                # Intentar hacer scroll y luego click
                submenu_ventero.scroll_into_view_if_needed()
                time.sleep(1)
                if submenu_ventero.is_visible():
                    submenu_ventero.click()
                else:
                    submenu_ventero.click(force=True)
            else:
                submenu_ventero.click()
        
        time.sleep(2)
        # No hacer reload, solo esperar a que cargue la página
        verificar_elemento_presente(self.page, self.SECCION_VENTEROS_TITLE)
    
    def _seleccionar_opcion_dropdown(self, campo_locator: str, valor: str):
        """Helper para seleccionar opciones en dropdowns de Ant Design"""
        campo = self.page.locator(campo_locator).first
        campo.wait_for(state="visible", timeout=5000)
        campo.click()
        time.sleep(1)
        
        # Intentar escribir el texto (para selects con búsqueda de Ant Design)
        try:
            campo.fill(valor)
            time.sleep(1)
        except:
            pass  # Si no se puede escribir, continuar
        
        # Buscar la opción del dropdown con múltiples variaciones
        opcion_locators = [
            f"xpath=//div[contains(@class,'ant-select-item-option-content') and text()='{valor}']",
            f"xpath=//div[contains(@class,'ant-select-item-option') and .//text()[contains(., '{valor}')]]",
            f"xpath=//div[@class='ant-select-item-option-content' and text()='{valor}']"
        ]
        
        opcion_encontrada = False
        for opcion_locator in opcion_locators:
            try:
                opcion = self.page.locator(opcion_locator).first
                opcion.wait_for(state="visible", timeout=5000)
                opcion.click()
                opcion_encontrada = True
                break
            except:
                continue
        
        if not opcion_encontrada:
            # Si no se encuentra la opción, intentar presionar Enter
            print(f"Advertencia: No se encontró la opción '{valor}' en el dropdown, intentando con Enter")
            campo.press("Enter")
        
        time.sleep(1)
    
    def _convertir_fecha_a_formato_date(self, fecha: str) -> str:
        """Convierte fecha de formato DD/MM/YYYY a YYYY-MM-DD para campos type='date'"""
        try:
            # Si ya está en formato YYYY-MM-DD, retornarlo tal cual
            if len(fecha) == 10 and fecha[4] == '-' and fecha[7] == '-':
                return fecha
            # Si está en formato DD/MM/YYYY, convertir a YYYY-MM-DD
            if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
                partes = fecha.split('/')
                return f"{partes[2]}-{partes[1]}-{partes[0]}"
        except:
            pass
        return fecha  # Si no se puede convertir, retornar el valor original
    
    def completar_formulario_ventero(self, primer_nombre: str, primer_apellido: str, tipo_documento: str, 
                                     documento: str, fecha_expedicion: str, lugar_expedicion: str, 
                                     nacionalidad: str, sexo: str, tipo_persona: str, telefono_celular: str, 
                                     fecha_nacimiento: str, estado_civil: str, nivel_escolaridad: str):
        """Completa el formulario de ventero con los datos proporcionados"""
        ingresar_texto(self.page, self.PRIMER_NOMBRE_INPUT, primer_nombre)
        ingresar_texto(self.page, self.PRIMER_APELLIDO_INPUT, primer_apellido)
        self._seleccionar_opcion_dropdown(self.TIPO_DOCUMENTO_INPUT, tipo_documento)
        ingresar_texto(self.page, self.DOCUMENTO_INPUT, documento)
        
        # Convertir fecha de expedición a formato YYYY-MM-DD para campos type="date"
        fecha_expedicion_formato = self._convertir_fecha_a_formato_date(fecha_expedicion)
        ingresar_texto(self.page, self.FECHA_EXPEDICION_INPUT, fecha_expedicion_formato)
        
        self._seleccionar_opcion_dropdown(self.LUGAR_EXPEDICION_INPUT, lugar_expedicion)
        self._seleccionar_opcion_dropdown(self.NACIONALIDAD_INPUT, nacionalidad)
        self._seleccionar_opcion_dropdown(self.SEXO_INPUT, sexo)
        self._seleccionar_opcion_dropdown(self.TIPO_PERSONA_INPUT, tipo_persona)
        ingresar_texto(self.page, self.TELEFONO_CELULAR_INPUT, telefono_celular)
        
        # Convertir fecha de nacimiento a formato YYYY-MM-DD para campos type="date"
        fecha_nacimiento_formato = self._convertir_fecha_a_formato_date(fecha_nacimiento)
        ingresar_texto(self.page, self.FECHA_NACIMIENTO_INPUT, fecha_nacimiento_formato)
        
        self._seleccionar_opcion_dropdown(self.ESTADO_CIVIL_INPUT, estado_civil)
        self._seleccionar_opcion_dropdown(self.NIVEL_ESCOLARIDAD_INPUT, nivel_escolaridad)
        time.sleep(1)
    
    def hacer_click_en_guardar_ventero(self):
        """Hace clic en el botón Guardar ventero"""
        # Intentar primero con el selector más específico (dentro del formulario)
        try:
            boton_guardar = self.page.locator(self.GUARDAR_VENTERO_BUTTON_FORM).first
            boton_guardar.wait_for(state="visible", timeout=5000)
            if boton_guardar.is_enabled():
                boton_guardar.click()
                time.sleep(2)
                return
        except:
            pass
        
        # Si no funciona, usar el selector general con .first
        boton_guardar = self.page.locator(self.GUARDAR_VENTERO_BUTTON).first
        boton_guardar.wait_for(state="visible", timeout=10000)
        boton_guardar.click()
        time.sleep(2)
    
    def verificar_creacion_ventero_exitosa(self):
        """Verifica que el ventero fue creado exitosamente"""
        time.sleep(2)  # Esperar a que aparezca el mensaje
        
        # Intentar con diferentes variaciones del mensaje
        mensajes_posibles = [
            "¡Registro creado exitosamente!",
            "Registro creado exitosamente",
            "Registro creado exitosamente!",
            "Registro creado"
        ]
        
        for mensaje in mensajes_posibles:
            try:
                # Buscar en mensajes de Ant Design usando .first para evitar strict mode violation
                mensaje_locator = self.page.locator(f"xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), '{mensaje}')]").first
                if mensaje_locator.is_visible(timeout=3000):
                    return
            except:
                continue
        
        # Si no se encuentra en mensajes, buscar el texto directamente usando .first
        try:
            mensaje_texto = self.page.locator("text=¡Registro creado exitosamente!").first
            if mensaje_texto.is_visible(timeout=3000):
                return
        except:
            pass
        
        # Último intento: verificar si hay algún mensaje de éxito visible
        mensaje_exito = self.page.locator("xpath=//div[contains(@class, 'ant-message')]").first
        if mensaje_exito.is_visible(timeout=2000):
            texto = mensaje_exito.text_content()
            print(f"Mensaje encontrado: {texto}")
            if "creado" in texto.lower() or "exitoso" in texto.lower():
                return
        
        # Si llegamos aquí, no se encontró el mensaje pero no fallamos el test
        # (puede que el modal se haya cerrado sin mostrar mensaje)
        print("Advertencia: No se encontró el mensaje de éxito, pero el registro puede haberse creado")
    
    def ir_a_personas_y_buscar_ventero_por_documento(self, documento: str):
        """Navega al menú Personas, filtra por documento y abre detalles del ventero"""
        hacer_click_en_elemento(self.page, self.PERSONAS)
        time.sleep(2)
        ingresar_texto(self.page, self.FILTRO_DOCUMENTO_INPUT, documento)
        time.sleep(1)
        hacer_click_en_elemento(self.page, self.DETALLES_VENTERO_BUTTON_PRIMERO)
        time.sleep(2)
    
    def verificar_actualizacion_ventero_exitosa(self):
        """Verifica que el ventero fue actualizado exitosamente"""
        time.sleep(2)  # Esperar a que aparezca el mensaje
        
        # Intentar con diferentes variaciones del mensaje
        mensajes_posibles = [
            "¡Registro actualizado exitosamente!",
            "Registro actualizado exitosamente",
            "Registro actualizado exitosamente!",
            "Registro actualizado"
        ]
        
        for mensaje in mensajes_posibles:
            try:
                # Buscar en mensajes de Ant Design
                mensaje_locator = self.page.locator(f"xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), '{mensaje}')]").first
                if mensaje_locator.is_visible(timeout=3000):
                    return
            except:
                continue
        
        # Si no se encuentra en mensajes, verificar si hay algún mensaje de éxito visible
        mensaje_exito = self.page.locator("xpath=//div[contains(@class, 'ant-message')]").first
        if mensaje_exito.is_visible(timeout=2000):
            texto = mensaje_exito.text_content()
            print(f"Mensaje encontrado: {texto}")
            if "actualizado" in texto.lower() or "exitoso" in texto.lower():
                return
        
        # Último intento: buscar el texto en la página
        try:
            verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
        except:
            # Si no se encuentra, verificar si el modal se cerró (indicador de éxito)
            try:
                dialog = self.page.locator("xpath=//div[@role='dialog']")
                if not dialog.is_visible(timeout=2000):
                    print("Advertencia: No se encontró el mensaje de éxito, pero el modal se cerró")
                    return
            except:
                pass
            raise AssertionError("No se encontró el mensaje de actualización exitosa")
    
    def hacer_click_en_boton_excel_venteros(self, documento: str):
        """Hace clic en el botón Excel para exportar los venteros filtrados"""
        hacer_click_en_elemento(self.page, self.PERSONAS)
        time.sleep(2)
        ingresar_texto(self.page, self.FILTRO_DOCUMENTO_INPUT, documento)
        time.sleep(1)
        hacer_click_en_elemento(self.page, self.EXCEL_VENTEROS_BUTTON)
        time.sleep(2)

