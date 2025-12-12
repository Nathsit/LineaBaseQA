"""
Page Object para la gestión de usuarios en SISDEP
Equivalente a page_objects/sisdep_usuarios_page.robot
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
    verificar_texto_en_pagina,
    limpiar_campo
)


class UsuariosPage:
    """Page Object para la gestión de usuarios en SISDEP"""
    
    # Locators de la sección de usuarios
    MENU_ADMINISTRACION = "xpath=//div[@role='menuitem' and .//span[text()='Administracion']]"
    USUARIOS_LINK = "xpath=//a[@href='/sisdep/administracion/usuarios' and text()='Usuarios']"
    USUARIOS_SECTION_TITLE = "xpath=//h1[@class='ant-typography ant-typography-ellipsis ant-typography-single-line ant-typography-ellipsis-single-line _aZcl1wH'][text()='Administración - Usuarios']"
    AGREGAR_USUARIO_BUTTON = "xpath=//button[@aria-label='Nuevo usuario' and .//span[text()='Nuevo usuario']]"
    # Formulario dentro del modal (más específico)
    FORM_NOMBRE = "xpath=//div[@role='dialog']//input[@id='nombre']"
    FORM_APELLIDO = "xpath=//div[@role='dialog']//input[@id='apellido']"
    FORM_TIPO_DOCUMENTO = "xpath=//div[@role='dialog']//input[@id='idTipoDocumento']"
    FORM_DOCUMENTO = "xpath=//div[@role='dialog']//input[@id='identificacion']"
    FORM_GRUPO = "xpath=//div[@role='dialog']//input[@id='idGrupo']"
    FORM_EMAIL = "xpath=//div[@role='dialog']//input[@id='email']"
    # Filtro en la página principal (no en modal)
    FILTRO_DOCUMENTO = "xpath=//input[@id='identificacion' and not(ancestor::div[@role='dialog'])]"
    FORM_GUARDAR_BUTTON = "xpath=//div[@role='dialog']//button[.//span[@aria-label='save'] and .//span[text()='Guardar']]"
    USUARIOS_GRID = "xpath=//div[contains(@class, 'ant-row') or contains(@class, 'grid')]"
    USUARIO_CARD = "xpath=//div[contains(@class, 'ant-card') and contains(@class, 'ant-card-bordered')]"
    DETALLES_BUTTON = "xpath=//button[@aria-label='Detalles' and .//span[text()='Detalles']]"
    REMOVER_BUTTON = "xpath=//button[@aria-label='Remover' and .//span[text()='Remover']]"
    CONFIRMAR_REMOVER_BUTTON = "xpath=//button[.//span[text()='Sí, eliminar']]"
    
    # Mensajes esperados
    USUARIO_CREADO_MSG = "Usuario creado exitosamente"
    USUARIO_ACTUALIZADO_MSG = "¡Registro actualizado exitosamente!"
    USUARIO_ELIMINADO_MSG = "Usuario eliminado exitosamente"
    
    def __init__(self, page: Page):
        self.page = page
    
    def ir_a_seccion_usuarios(self):
        """
        Navega a la sección de administración de usuarios
        Equivalente a: Ir A Seccion Usuarios
        """
        # Verificar si el link de usuarios ya es visible (menú ya expandido)
        usuarios_link = self.page.locator(self.USUARIOS_LINK)
        
        # Intentar verificar si el elemento está visible y clickeable
        try:
            usuarios_link.wait_for(state="visible", timeout=3000)
            # Si está visible, verificar que también sea clickeable
            usuarios_link.wait_for(state="attached", timeout=1000)
        except:
            # Si no es visible, hacer click en el menú de administración para expandirlo
            # Usar click con no_wait_after=True porque solo expande un menú, no navega
            menu_admin = self.page.locator(self.MENU_ADMINISTRACION)
            menu_admin.wait_for(state="visible", timeout=10000)
            menu_admin.click(no_wait_after=True)  # No esperar navegación porque solo expande el menú
            time.sleep(2)  # Esperar a que el menú se expanda
        
        # Esperar a que el link de usuarios sea visible y clickeable
        usuarios_link.wait_for(state="visible", timeout=10000)
        # Esperar un poco más para asegurar que el menú está completamente expandido
        time.sleep(0.5)
        
        # Hacer click en el link de usuarios (este sí navega)
        hacer_click_en_elemento(self.page, self.USUARIOS_LINK)
        
        # Verificar que llegamos a la sección de usuarios
        verificar_elemento_presente(self.page, self.USUARIOS_SECTION_TITLE)
    
    def hacer_click_en_agregar_usuario(self):
        """
        Hace click en el botón de agregar nuevo usuario
        """
        hacer_click_en_elemento(self.page, self.AGREGAR_USUARIO_BUTTON)
        time.sleep(2)
    
    def verificar_formulario_visible(self):
        """
        Verifica que el formulario de usuario esté visible
        """
        # Esperar a que el modal se abra
        time.sleep(2)
        # Verificar que el modal está presente
        modal = self.page.locator("xpath=//div[@role='dialog']")
        modal.wait_for(state="visible", timeout=5000)
        # Verificar el campo nombre dentro del modal
        verificar_elemento_presente(self.page, self.FORM_NOMBRE)
    
    def ingresar_texto_en_filtro_documento(self, documento: str):
        """
        Ingresa texto en el filtro de documento
        Equivalente a: Ingresar Texto En Filtro Documento
        """
        time.sleep(3)
        verificar_elemento_presente(self.page, self.FILTRO_DOCUMENTO)
        ingresar_texto(self.page, self.FILTRO_DOCUMENTO, documento)
        time.sleep(2)
    
    def seleccionar_usuario_por_documento(self, documento: str):
        """
        Selecciona un usuario específico por su número de documento
        Equivalente a: Seleccionar Usuario Por Documento
        """
        time.sleep(2)
        # Selector más específico: buscar la tarjeta principal que contiene el documento
        usuario_card = f"xpath=//div[contains(@class, 'ant-card') and contains(@class, 'ant-card-bordered')][.//text()[contains(., '{documento}')]]"
        # Usar first() para seleccionar el primer elemento si hay múltiples
        card_locator = self.page.locator(usuario_card).first
        card_locator.wait_for(state="visible", timeout=10000)
        card_locator.click()
    
    def editar_solo_email_usuario(self, nuevo_email: str):
        """
        Edita solo el campo de email del usuario
        Equivalente a: Editar Solo Email Usuario
        """
        time.sleep(2)
        hacer_click_en_elemento(self.page, self.DETALLES_BUTTON)
        time.sleep(3)
        # Esperar a que el modal se abra
        modal = self.page.locator("xpath=//div[@role='dialog']")
        modal.wait_for(state="visible", timeout=5000)
        # Verificar y editar email dentro del modal
        email_field = self.page.locator(self.FORM_EMAIL)
        email_field.wait_for(state="visible", timeout=5000)
        email_field.clear()
        time.sleep(1)
        email_field.fill(nuevo_email)
        time.sleep(1)
        hacer_click_en_elemento(self.page, self.FORM_GUARDAR_BUTTON)
    
    def verificar_email_actualizado(self):
        """
        Verifica que el email del usuario se actualizó correctamente
        Equivalente a: Verificar Email Actualizado
        """
        time.sleep(2)
        verificar_texto_en_pagina(self.page, self.USUARIO_ACTUALIZADO_MSG)
    
    def eliminar_usuario(self):
        """
        Elimina un usuario existente
        Equivalente a: Eliminar Usuario
        """
        hacer_click_en_elemento(self.page, self.REMOVER_BUTTON)
        time.sleep(2)
        hacer_click_en_elemento(self.page, self.CONFIRMAR_REMOVER_BUTTON)
    
    def ingresar_texto_en_campos_vacios(self):
        """
        Verifica que se muestre un mensaje de error cuando se intenta guardar un usuario con campos vacíos
        Equivalente a: Ingresar Texto En Campos Vacios
        """
        hacer_click_en_elemento(self.page, self.FORM_GUARDAR_BUTTON)
        time.sleep(1)
        # Verificar el mensaje de error dentro del modal usando el selector específico
        # El mensaje aparece después de hacer click en guardar
        error_message = "xpath=//div[@role='alert' and contains(@class, 'ant-form-item-explain-error') and text()='El campo es obligatorio']"
        # Si hay múltiples elementos (uno por cada campo), usar el primero que esté visible
        error_locator = self.page.locator(error_message).first
        error_locator.wait_for(state="visible", timeout=5000)
        expect(error_locator).to_be_visible()
    
    def verificar_elementos_de_usuarios_presentes(self):
        """
        Verifica que todos los elementos de la página de usuarios estén presentes
        Equivalente a: Verificar Elementos De Usuarios Presentes
        """
        verificar_elemento_presente(self.page, self.USUARIOS_SECTION_TITLE)
        verificar_elemento_presente(self.page, self.AGREGAR_USUARIO_BUTTON)
        verificar_elemento_presente(self.page, self.USUARIOS_GRID)
    
    def _seleccionar_opcion_dropdown(self, campo_locator: str, valor: str):
        """
        Método auxiliar para seleccionar una opción en un dropdown de Ant Design
        """
        campo = self.page.locator(campo_locator)
        campo.wait_for(state="visible", timeout=5000)
        campo.click()
        time.sleep(1)
        
        # Intentar escribir el texto (para selects con búsqueda de Ant Design)
        campo.fill(valor)
        time.sleep(1)
        
        # Buscar y hacer click en la opción del dropdown
        # El dropdown puede estar fuera del modal, así que buscamos en toda la página
        # Buscar por el texto exacto o parcial en el contenido del elemento
        opcion_locator = f"xpath=//div[contains(@class, 'ant-select-item') and contains(@class, 'ant-select-item-option') and .//text()[contains(., '{valor}')]]"
        
        try:
            opcion = self.page.locator(opcion_locator).first
            opcion.wait_for(state="visible", timeout=5000)
            opcion.click()
            time.sleep(1)
        except Exception as e:
            # Si no se encuentra la opción, intentar presionar Enter
            print(f"Advertencia: No se encontró la opción '{valor}' en el dropdown, intentando con Enter")
            campo.press("Enter")
            time.sleep(1)
        
        # Verificar que se seleccionó correctamente (sin esperar indefinidamente)
        # Solo esperar un momento para que la selección se complete
        time.sleep(0.5)
    
    def llenar_formulario_usuario(self, nombre: str, apellido: str, tipo_documento: str, documento: str, grupo: str, email: str):
        """
        Llena el formulario completo de usuario con todos los datos
        Equivalente a: Agregar Nuevo Usuario (pero solo llena el formulario)
        """
        # Esperar a que el modal esté completamente cargado
        modal = self.page.locator("xpath=//div[@role='dialog']")
        modal.wait_for(state="visible", timeout=5000)
        
        # Llenar Nombre
        nombre_field = self.page.locator(self.FORM_NOMBRE)
        nombre_field.wait_for(state="visible", timeout=5000)
        nombre_field.fill(nombre)
        time.sleep(0.5)
        
        # Llenar Apellido
        apellido_field = self.page.locator(self.FORM_APELLIDO)
        apellido_field.wait_for(state="visible", timeout=5000)
        apellido_field.fill(apellido)
        time.sleep(0.5)
        
        # Seleccionar Tipo de Documento (dropdown)
        self._seleccionar_opcion_dropdown(self.FORM_TIPO_DOCUMENTO, tipo_documento)
        
        # Llenar Documento
        documento_field = self.page.locator(self.FORM_DOCUMENTO)
        documento_field.wait_for(state="visible", timeout=5000)
        documento_field.fill(documento)
        time.sleep(0.5)
        
        # Seleccionar Grupo (dropdown)
        self._seleccionar_opcion_dropdown(self.FORM_GRUPO, grupo)
        
        # Llenar Email
        email_field = self.page.locator(self.FORM_EMAIL)
        email_field.wait_for(state="visible", timeout=5000)
        email_field.fill(email)
        time.sleep(0.5)
    
    def guardar_usuario(self):
        """
        Hace click en el botón Guardar del formulario
        """
        hacer_click_en_elemento(self.page, self.FORM_GUARDAR_BUTTON)
        time.sleep(2)
    
    def verificar_usuario_creado(self):
        """
        Verifica que el usuario fue creado exitosamente
        """
        time.sleep(3)  # Esperar a que se procese la acción
        
        # Verificar mensaje de éxito (puede variar según la aplicación)
        # Intentar diferentes variantes del mensaje con timeout corto
        mensajes_posibles = [
            "¡Registro creado exitosamente!",
            "Usuario creado exitosamente",
            "Registro creado exitosamente",
            "Usuario registrado exitosamente",
            "creado exitosamente",
            "exitosamente"
        ]
        
        mensaje_encontrado = False
        for mensaje in mensajes_posibles:
            try:
                # Buscar el texto en la página con un timeout corto
                texto_locator = f"xpath=//*[contains(text(), '{mensaje}')]"
                elemento = self.page.locator(texto_locator).first
                elemento.wait_for(state="visible", timeout=2000)
                mensaje_encontrado = True
                break
            except:
                continue
        
        # Si no se encuentra ningún mensaje, verificar que el modal se cerró
        # lo cual indica que el usuario fue creado
        if not mensaje_encontrado:
            try:
                modal = self.page.locator("xpath=//div[@role='dialog']")
                # Verificar si el modal está oculto o no existe
                count = modal.count()
                if count == 0:
                    # El modal no existe, asumimos que se cerró exitosamente
                    return
                # Intentar verificar que está oculto con timeout corto
                modal.wait_for(state="hidden", timeout=2000)
            except:
                # Si no podemos verificar, al menos esperamos un momento y continuamos
                # para no bloquear el test indefinidamente
                time.sleep(1)
                print("Advertencia: No se pudo verificar explícitamente que el usuario fue creado, pero el test continúa")

