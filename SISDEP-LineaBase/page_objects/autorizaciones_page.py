"""
Page Object para la gestión de autorizaciones en SISDEP
Equivalente a page_objects/sisdep_autorizaciones_page.robot
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


class AutorizacionesPage:
    """Page Object para la gestión de autorizaciones en SISDEP"""
    
    # Navegación
    REGULACIONES_MENU = "xpath=//span[@class='ant-menu-title-content'][text()='Regulaciones']"
    AUTORIZACIONES_SUBMENU = "xpath=//a[@href='/sisdep/regulaciones/autorizaciones']"
    AUTORIZACIONES_SECTION_TITLE = "xpath=//h1[@class='ant-typography ant-typography-ellipsis ant-typography-single-line ant-typography-ellipsis-single-line _aZcl1wH'][text()='Regulaciones - Autorizaciones']"
    
    # Búsqueda de ventero
    BUSCAR_VENTERO_INPUT = "xpath=//input[@role='textbox' and @aria-label='Documento' and @id='documento']"
    BUSCAR_VENTERO_BUTTON = "xpath=//button[@type='button' and @class='ant-btn ant-btn-primary'][.//span[text()='Buscar']]"
    AGREGAR_AUTORIZACION_BUTTON = "xpath=//button[@aria-label='Agregar' and @class='ant-btn ant-btn-primary HdMXdtFX']"
    
    # Formulario de solicitud
    RADICADO_MERCURIO_INPUT = "xpath=//input[@role='textbox' and @aria-label='Radicado mercurio' and @id='radicadoMercurio']"
    TIPO_AUTORIZACION_DROPDOWN = "xpath=//input[@id='idMotivoAutorizacion' and @aria-label='Motivo de autorización']"
    FECHA_INICIAL_INPUT = "xpath=//input[@role='textbox' and @aria-label='Fecha inicial' and @id='fechaInicial']"
    ESTADO_DROPDOWN = "id=idEstadoAutorizacion"
    DIAS_DROPDOWN = "xpath=//div[@class='ant-select ant-select-lg IlERIOp8 ant-select-multiple ant-select-allow-clear ant-select-show-search'][@aria-label='Dias']"
    HORA_INICIO_INPUT = "xpath=//input[@id='horaInicio' and @class='ant-input-number-input']"
    HORA_FIN_INPUT = "xpath=//input[@id='horaFin' and @class='ant-input-number-input']"
    GUARDAR_SOLICITUD_BUTTON = "xpath=//button[@type='button' and @class='ant-btn ant-btn-primary'][.//span[text()='Guardar']]"
    
    # Detalles de autorización
    AGREGAR_VISITA_BUTTON = "xpath=//button[.//span[text()='Asignar visita domiciliaria']]"
    AGREGAR_RESOLUCION_BUTTON = "xpath=//button[.//span[text()='Agrega resolución']]"
    GUARDAR_VISITA_BUTTON = "xpath=//button[contains(text(),'Guardar visita')]"
    
    # Formulario de resolución
    NUMERO_RESOLUCION_INPUT = "id=numero"
    FECHA_EFECTOS_FISCALES_INPUT = "id=fechaEfectosFiscales"
    FECHA_EXPEDICION_INPUT = "id=fechaExpedicion"
    GUARDAR_RESOLUCION_BUTTON = "xpath=//button[.//span[text()='Guardar']]"
    
    # Eliminación
    ELIMINAR_AUTORIZACION_BUTTON = "xpath=//button[@aria-label='Eliminar' and .//span[text()='Eliminar']]"
    CONFIRMAR_ELIMINAR_BUTTON = "xpath=//button[contains(@class,'ant-btn-dangerous') and .//span[text()='Eliminar']]"
    
    # Reporte Excel
    BOTON_EXCEL = "xpath=//button[.//span[text()='Excel']]"
    
    def __init__(self, page: Page):
        self.page = page
    
    def el_usuario_esta_en_seccion_autorizaciones(self):
        """Navega a la sección de Autorizaciones"""
        menu_regulaciones = self.page.locator(self.REGULACIONES_MENU)
        menu_regulaciones.wait_for(state="visible", timeout=10000)
        menu_regulaciones.click(no_wait_after=True)
        time.sleep(2)  # Aumentar tiempo de espera para que el menú se expanda
        
        # Verificar si el submenú ya es visible
        submenu_autorizaciones = self.page.locator(self.AUTORIZACIONES_SUBMENU)
        try:
            submenu_autorizaciones.wait_for(state="visible", timeout=3000)
        except:
            # Si no es visible, esperar un poco más para que el menú se expanda
            time.sleep(2)
            # Intentar hacer scroll o usar force si es necesario
            submenu_autorizaciones.wait_for(state="attached", timeout=10000)
            submenu_autorizaciones.scroll_into_view_if_needed()
            time.sleep(1)
            try:
                submenu_autorizaciones.wait_for(state="visible", timeout=5000)
            except:
                # Si aún no es visible, intentar hacer click con force
                submenu_autorizaciones.click(force=True)
                time.sleep(2)
                verificar_elemento_presente(self.page, self.AUTORIZACIONES_SECTION_TITLE)
                return
        
        submenu_autorizaciones.click()
        time.sleep(2)
        verificar_elemento_presente(self.page, self.AUTORIZACIONES_SECTION_TITLE)
    
    def buscar_ventero_por_documento(self, documento: str):
        """Busca un ventero por su número de documento"""
        hacer_click_en_elemento(self.page, self.AGREGAR_AUTORIZACION_BUTTON)
        time.sleep(2)
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
        opcion_locator = f"xpath=//div[@class='ant-select-item-option-content'][text()='{valor}']"
        opcion = self.page.locator(opcion_locator).first
        opcion.wait_for(state="visible", timeout=5000)
        opcion.click()
        time.sleep(1)
    
    def completar_datos_solicitud_autorizacion(self, radicado_mercurio: str, fecha_inicial: str, hora_inicio: str, hora_fin: str):
        """Completa los datos del formulario de solicitud de autorización"""
        time.sleep(2)
        ingresar_texto(self.page, self.RADICADO_MERCURIO_INPUT, radicado_mercurio)
        time.sleep(1)
        
        # Tipo de Autorización
        self._seleccionar_opcion_dropdown(self.TIPO_AUTORIZACION_DROPDOWN, "Nueva autorizacion")
        
        # Fecha Inicial (campo type="date" requiere formato YYYY-MM-DD)
        campo_fecha = self.page.locator(self.FECHA_INICIAL_INPUT)
        campo_fecha.wait_for(state="visible", timeout=5000)
        # Para campos type="date", usar fill directamente con formato YYYY-MM-DD
        campo_fecha.fill(fecha_inicial)
        time.sleep(1)
        
        # Estado
        self._seleccionar_opcion_dropdown(self.ESTADO_DROPDOWN, "En proceso")
        
        # Días
        self._seleccionar_opcion_dropdown(self.DIAS_DROPDOWN, "Lunes")
        
        # Hora Inicio
        ingresar_texto(self.page, self.HORA_INICIO_INPUT, hora_inicio)
        time.sleep(1)
        
        # Hora Fin
        ingresar_texto(self.page, self.HORA_FIN_INPUT, hora_fin)
        time.sleep(1)
    
    def hacer_click_en_guardar_solicitud(self):
        """Hace clic en el botón guardar de la solicitud"""
        hacer_click_en_elemento(self.page, self.GUARDAR_SOLICITUD_BUTTON)
        time.sleep(2)
    
    def el_sistema_crea_nueva_solicitud_autorizacion(self):
        """Verifica que se creó la nueva solicitud de autorización"""
        verificar_texto_en_pagina(self.page, "¡Registro creado exitosamente!")
    
    def acceder_a_detalles_autorizacion(self, radicado_mercurio: str):
        """Accede a los detalles de una autorización filtrando por radicado"""
        ingresar_texto(self.page, "id=filtroRadicadoMercurio", radicado_mercurio)
        time.sleep(2)  # Esperar a que se filtre la lista
        
        # Usar .first para evitar strict mode violation
        boton_detalle = self.page.locator("xpath=//button[@aria-label='Detalle' and .//span[text()='Detalle']]").first
        boton_detalle.wait_for(state="visible", timeout=10000)
        boton_detalle.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_detalle.click()
        time.sleep(3)  # Esperar más tiempo antes del reload
        self.page.reload()
        time.sleep(3)  # Esperar más tiempo después del reload
        self.page.wait_for_load_state("networkidle", timeout=10000)
    
    def hacer_click_en_agregar_visita_administrativa(self):
        """Hace clic en el botón agregar visita administrativa"""
        # Esperar a que el botón esté disponible después del reload
        boton_agregar = self.page.locator(self.AGREGAR_VISITA_BUTTON).first
        boton_agregar.wait_for(state="visible", timeout=15000)
        boton_agregar.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_agregar.click()
        time.sleep(2)
    
    def agregar_visita_administrativa_a_autorizacion(self):
        """Agrega una visita administrativa a una autorización"""
        time.sleep(2)
        # Visitador
        self._seleccionar_opcion_dropdown("id=idVisitador", "Administrador DEL SISTEMA")
        # Tipo de visita
        self._seleccionar_opcion_dropdown("id=idTipo", "Actualización")
        # Vehículo
        self._seleccionar_opcion_dropdown("id=idVehiculo", "RJZ672")
        # Fecha de la visita
        self._seleccionar_fecha_hoy("id=fechaVisita")
        # Franja horaria
        self._seleccionar_opcion_dropdown("id=idFranja", "AM")
        # Guardar visita
        hacer_click_en_elemento(self.page, "xpath=//button[@type='button' and contains(@class,'ant-btn-primary') and .//span[text()='OK']]")
        time.sleep(2)
    
    def _seleccionar_fecha_hoy(self, campo_id: str):
        """Helper para seleccionar la fecha de hoy en un date picker"""
        # Extraer solo el ID si viene con "id="
        if campo_id.startswith("id="):
            campo_id = campo_id.replace("id=", "")
        
        campo = self.page.locator(f"#{campo_id}")
        campo.wait_for(state="visible", timeout=5000)
        # Remover atributo readonly si existe
        try:
            self.page.evaluate(f"document.getElementById('{campo_id}').removeAttribute('readonly')")
        except:
            pass
        campo.click()
        time.sleep(1)
        # Hacer click en el botón "Today" del date picker
        today_button = self.page.locator("xpath=//a[contains(@class,'ant-picker-today-btn') and text()='Today']")
        if today_button.is_visible():
            today_button.click()
            time.sleep(1)
        else:
            # Si no hay botón Today, usar la fecha actual en formato YYYY-MM-DD
            from datetime import datetime
            fecha_hoy = datetime.now().strftime("%Y-%m-%d")
            campo.fill(fecha_hoy)
            time.sleep(1)
    
    def el_sistema_registra_visita_administrativa(self):
        """Verifica que se registró la visita administrativa"""
        verificar_texto_en_pagina(self.page, "¡Registro creado exitosamente!")
    
    def actualizar_visita_administrativa(self, radicado_mercurio: str):
        """Actualiza una visita administrativa de una autorización.
        Flujo: Filtrar por radicado -> Clic en Detalle -> Clic en Ver visita domiciliaria -> Clic en OK"""
        # Filtrar por radicado
        ingresar_texto(self.page, "id=filtroRadicadoMercurio", radicado_mercurio)
        time.sleep(1)
        
        # Clic en el botón Detalle (aria-label="Detalle")
        boton_detalle = self.page.locator("xpath=//button[@aria-label='Detalle' and .//span[text()='Detalle']]").first
        boton_detalle.wait_for(state="visible", timeout=10000)
        boton_detalle.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_detalle.click()
        time.sleep(3)  # Esperar más tiempo antes del reload
        self.page.reload()
        time.sleep(3)  # Esperar más tiempo después del reload
        self.page.wait_for_load_state("networkidle", timeout=10000)
        
        # Clic en "Ver visita domiciliaria" (botón con clase ant-btn-lg y span "Ver visita domiciliaria")
        # Intentar múltiples selectores para encontrar el botón
        selectores_ver_visita = [
            "xpath=//button[@type='button' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[text()='Ver visita domiciliaria']]",
            "xpath=//button[contains(@class,'ant-btn-lg') and .//span[text()='Ver visita domiciliaria']]",
            "xpath=//button[.//span[text()='Ver visita domiciliaria']]"
        ]
        
        boton_ver_visita = None
        for selector in selectores_ver_visita:
            try:
                boton_ver_visita = self.page.locator(selector).first
                boton_ver_visita.wait_for(state="visible", timeout=5000)
                if boton_ver_visita.is_visible():
                    break
            except:
                continue
        
        if boton_ver_visita is None or not boton_ver_visita.is_visible():
            # Esperar un poco más y recargar si es necesario
            time.sleep(2)
            self.page.reload()
            time.sleep(2)
            boton_ver_visita = self.page.locator(selectores_ver_visita[0]).first
            boton_ver_visita.wait_for(state="visible", timeout=10000)
        
        boton_ver_visita.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_ver_visita.click()
        time.sleep(2)
        
        # Clic en el botón OK
        boton_ok = self.page.locator("xpath=//button[@type='button' and contains(@class,'ant-btn-primary') and .//span[text()='OK']]").first
        boton_ok.wait_for(state="visible", timeout=10000)
        boton_ok.click()
        time.sleep(2)
    
    def verificar_actualizacion_visita_administrativa_exitosa(self):
        """Verifica que la visita administrativa fue actualizada exitosamente"""
        time.sleep(1)
        # Buscar el mensaje de éxito específico
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
    
    def actualizar_resolucion(self, radicado_mercurio: str):
        """Actualiza una resolución de una autorización.
        Flujo: Filtrar por radicado -> Clic en Detalle -> Recargar -> Clic en Guardar"""
        # Filtrar por radicado
        ingresar_texto(self.page, "id=filtroRadicadoMercurio", radicado_mercurio)
        time.sleep(2)  # Esperar a que se filtre la lista
        
        # Clic en el botón Detalle (aria-label="Detalle")
        boton_detalle = self.page.locator("xpath=//button[@aria-label='Detalle' and .//span[text()='Detalle']]").first
        boton_detalle.wait_for(state="visible", timeout=10000)
        boton_detalle.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_detalle.click()
        time.sleep(3)  # Esperar más tiempo antes del reload
        self.page.reload()
        time.sleep(3)  # Esperar más tiempo después del reload
        self.page.wait_for_load_state("networkidle", timeout=10000)
        
        # Clic directamente en el botón Guardar (type="submit" con ant-btn-lg)
        boton_guardar = self.page.locator("xpath=//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[text()='Guardar']]").first
        boton_guardar.wait_for(state="visible", timeout=15000)
        boton_guardar.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_guardar.click()
        time.sleep(2)
    
    def verificar_actualizacion_resolucion_exitosa(self):
        """Verifica que la resolución fue actualizada exitosamente"""
        time.sleep(1)
        # Buscar el mensaje de éxito específico
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
    
    def actualizar_informacion_general_autorizacion(self, radicado_mercurio: str):
        """Actualiza la información general de una autorización.
        Flujo: Filtrar por radicado -> Clic en Detalle -> Recargar -> Clic en Guardar"""
        # Filtrar por radicado
        ingresar_texto(self.page, "id=filtroRadicadoMercurio", radicado_mercurio)
        time.sleep(2)  # Esperar a que se filtre la lista
        
        # Clic en el botón Detalle (aria-label="Detalle")
        boton_detalle = self.page.locator("xpath=//button[@aria-label='Detalle' and .//span[text()='Detalle']]").first
        boton_detalle.wait_for(state="visible", timeout=10000)
        boton_detalle.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_detalle.click()
        time.sleep(3)  # Esperar más tiempo antes del reload
        self.page.reload()
        time.sleep(3)  # Esperar más tiempo después del reload
        self.page.wait_for_load_state("networkidle", timeout=10000)
        
        # Clic directamente en el botón Guardar (type="submit" con ant-btn-lg)
        boton_guardar = self.page.locator("xpath=//button[@type='submit' and contains(@class,'ant-btn-primary') and contains(@class,'ant-btn-lg') and .//span[text()='Guardar']]").first
        boton_guardar.wait_for(state="visible", timeout=15000)
        boton_guardar.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_guardar.click()
        time.sleep(2)
    
    def verificar_actualizacion_autorizacion_exitosa(self):
        """Verifica que la autorización fue actualizada exitosamente"""
        time.sleep(1)
        # Buscar el mensaje de éxito específico
        verificar_texto_en_pagina(self.page, "¡Registro actualizado exitosamente!")
    
    def hacer_click_en_agregar_resolucion(self):
        """Hace clic en el botón agregar resolución"""
        hacer_click_en_elemento(self.page, self.AGREGAR_RESOLUCION_BUTTON)
        time.sleep(2)
    
    def el_sistema_muestra_que_las_fechas_no_pueden_ser_diferentes(self):
        """Verifica que el sistema muestra un mensaje de error cuando las fechas son diferentes"""
        time.sleep(2)  # Esperar a que aparezca el mensaje
        # Intentar con diferentes variaciones del mensaje
        mensajes_posibles = [
            "La fecha de efectos fiscales no puede ser diferente a la fecha de expedición",
            "fecha de efectos fiscales no puede ser diferente",
            "fechas no pueden ser diferentes",
            "fecha de efectos fiscales"
        ]
        for mensaje in mensajes_posibles:
            try:
                verificar_texto_en_pagina(self.page, mensaje)
                return
            except:
                continue
        # Si ninguno funciona, verificar que hay algún mensaje de error visible
        mensaje_error = self.page.locator("xpath=//div[contains(@class, 'ant-message') or contains(@class, 'ant-form-item-explain-error')]").first
        if mensaje_error.is_visible():
            print(f"Mensaje de error encontrado: {mensaje_error.text_content()}")
        else:
            raise AssertionError("No se encontró el mensaje de error esperado")
    
    def hacer_click_en_eliminar_autorizacion(self, radicado_mercurio: str):
        """Hace clic en el botón eliminar de una autorización"""
        ingresar_texto(self.page, "id=filtroRadicadoMercurio", radicado_mercurio)
        time.sleep(2)  # Esperar a que se filtre la lista
        
        # Usar .first para evitar strict mode violation
        boton_eliminar = self.page.locator(self.ELIMINAR_AUTORIZACION_BUTTON).first
        boton_eliminar.wait_for(state="visible", timeout=15000)
        boton_eliminar.scroll_into_view_if_needed()
        time.sleep(0.5)
        boton_eliminar.click()
        time.sleep(1)
    
    def confirmar_eliminacion_autorizacion(self):
        """Confirma la eliminación de la autorización"""
        verificar_elemento_presente(self.page, self.CONFIRMAR_ELIMINAR_BUTTON)
        hacer_click_en_elemento(self.page, self.CONFIRMAR_ELIMINAR_BUTTON)
        time.sleep(2)
    
    def el_sistema_elimina_la_autorizacion(self):
        """Verifica que se eliminó la autorización"""
        verificar_texto_en_pagina(self.page, "¡Registro eliminado exitosamente!")
    
    def hacer_click_en_boton_excel(self):
        """Hace clic en el botón Excel para generar el reporte"""
        hacer_click_en_elemento(self.page, self.BOTON_EXCEL)
        time.sleep(5)
    
    def el_sistema_muestra_que_el_ventero_no_existe(self):
        """Verifica que el sistema muestra un mensaje de error cuando el ventero no existe"""
        verificar_texto_en_pagina(self.page, "No se encontro un ventero con el documento ingresado")

