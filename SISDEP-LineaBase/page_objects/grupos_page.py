"""
Page Object para la gestión de grupos y permisos en SISDEP
Equivalente a page_objects/sisdep_grupos_page.robot
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


class GruposPage:
    """Page Object para la gestión de grupos y permisos en SISDEP"""
    
    # Locators
    GRUPOS_SECTION_TITLE = "xpath=//h1[contains(., 'Grupos y Permisos')]"
    NUEVO_GRUPO_BUTTON = "xpath=//button[@aria-label='Nuevo grupo' and .//span[text()='Nuevo grupo']]"
    NOMBRE_GRUPO_FIELD = "css=#nombre"
    DESCRIPCION_GRUPO_FIELD = "css=#descripcion"
    CHECK_ES_SOCIAL = "css=#esSocial"
    CHECK_OTRO = "xpath=(//button[@role='switch'])[2]"
    GUARDAR_GRUPO_BUTTON = "xpath=//button[@aria-label='Guardar permisos' and .//span[text()='Guardar']]"
    EDITAR_GRUPO_BUTTON = "xpath=//button[@aria-label='Detalles' and .//span[text()='Detalles']]"
    REMOVER_GRUPO_BUTTON = "xpath=//button[@aria-label='Remover' and .//span[text()='Remover']]"
    CONFIRMAR_REMOVER_BUTTON = "xpath=//button[.//span[contains(., 'Sí, eliminar')]]"
    MENU_ADMINISTRACION = "xpath=//div[@role='menuitem' and .//span[text()='Administracion']]"
    GRUPOS_PERMISOS_LINK = "xpath=//a[@href='/sisdep/administracion/grupos' and text()='Grupos y permisos']"
    
    def __init__(self, page: Page):
        self.page = page
    
    def ir_a_seccion_grupos_y_permisos(self):
        """
        Navega a la sección de administración de grupos y permisos
        Equivalente a: Ir A Seccion Grupos Y Permisos
        """
        hacer_click_en_elemento(self.page, self.MENU_ADMINISTRACION)
        hacer_click_en_elemento(self.page, self.GRUPOS_PERMISOS_LINK)
        verificar_elemento_presente(self.page, self.GRUPOS_SECTION_TITLE)
    
    def crear_nuevo_grupo_con_permisos(self, nombre_grupo: str, permisos: str = ""):
        """
        Crea un nuevo grupo y asigna permisos
        Equivalente a: Crear Nuevo Grupo Con Permisos
        """
        hacer_click_en_elemento(self.page, self.NUEVO_GRUPO_BUTTON)
        time.sleep(3)
        ingresar_texto(self.page, self.NOMBRE_GRUPO_FIELD, nombre_grupo)
        ingresar_texto(self.page, self.DESCRIPCION_GRUPO_FIELD, "Grupo de prueba automatizado")
        hacer_click_en_elemento(self.page, self.CHECK_ES_SOCIAL)
        hacer_click_en_elemento(self.page, self.CHECK_OTRO)
        hacer_click_en_elemento(self.page, self.GUARDAR_GRUPO_BUTTON)
    
    def verificar_grupo_creado(self, nombre_grupo: str):
        """
        Verifica que el grupo fue creado correctamente
        Equivalente a: Verificar Grupo Creado
        """
        time.sleep(3)  # Esperar a que el mensaje aparezca
        
        # Buscar el mensaje más reciente dentro del contenedor de mensajes de Ant Design
        # El mensaje más reciente suele estar en el último contenedor de mensajes
        mensaje_locator = "xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), '¡Registro creado exitosamente!')]"
        
        # Esperar a que el mensaje esté visible y usar el primero (más reciente)
        mensaje = self.page.locator(mensaje_locator).first
        mensaje.wait_for(state="visible", timeout=5000)
        
        # Verificar que el mensaje está visible
        expect(mensaje).to_be_visible()
    
    def verificar_grupo_con_el_mismo_nombre(self, nombre_grupo: str):
        """
        Verifica que el grupo no se puede crear con el mismo nombre
        Equivalente a: Verificar Grupo Con el mismo nombre
        """
        time.sleep(3)  # Esperar a que el mensaje aparezca
        
        # Buscar el mensaje de error más reciente dentro del contenedor de mensajes de Ant Design
        mensaje_locator = "xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), 'Error al crear el grupo')]"
        
        # Esperar a que el mensaje esté visible y usar el primero (más reciente)
        mensaje = self.page.locator(mensaje_locator).first
        mensaje.wait_for(state="visible", timeout=5000)
        
        # Verificar que el mensaje está visible
        expect(mensaje).to_be_visible()
    
    def seleccionar_grupo_para_editar(self, nombre_grupo: str):
        """
        Selecciona un grupo para editar
        Equivalente a: Seleccionar Grupo Para Editar
        """
        self.filtrar_grupo_por_nombre(nombre_grupo)
        hacer_click_en_elemento(self.page, self.EDITAR_GRUPO_BUTTON)
    
    def actualizar_permisos_de_grupo(self, nueva_descripcion: str):
        """
        Actualiza la descripción del grupo
        Equivalente a: Actualizar Permisos De Grupo
        """
        ingresar_texto(self.page, self.DESCRIPCION_GRUPO_FIELD, nueva_descripcion)
        hacer_click_en_elemento(self.page, self.GUARDAR_GRUPO_BUTTON)
    
    def verificar_permisos_actualizados(self):
        """
        Verifica que el grupo fue actualizado exitosamente
        Equivalente a: Verificar Permisos Actualizados
        """
        time.sleep(3)  # Esperar a que el mensaje aparezca
        
        # Buscar el mensaje más reciente dentro del contenedor de mensajes de Ant Design
        mensaje_locator = "xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), '¡Registro actualizado exitosamente!')]"
        
        # Esperar a que el mensaje esté visible y usar el primero (más reciente)
        mensaje = self.page.locator(mensaje_locator).first
        mensaje.wait_for(state="visible", timeout=5000)
        
        # Verificar que el mensaje está visible
        expect(mensaje).to_be_visible()
    
    def seleccionar_grupo_para_eliminar(self, nombre_grupo: str):
        """
        Selecciona un grupo para eliminar
        Equivalente a: Seleccionar Grupo Para Eliminar
        """
        self.filtrar_grupo_por_nombre(nombre_grupo)
        hacer_click_en_elemento(self.page, self.REMOVER_GRUPO_BUTTON)
    
    def eliminar_grupo(self):
        """
        Elimina el grupo seleccionado
        Equivalente a: Eliminar Grupo
        """
        try:
            hacer_click_en_elemento(self.page, self.REMOVER_GRUPO_BUTTON)
        except:
            pass  # Ignorar error si el botón no está presente
    
    def verificar_grupo_eliminado(self):
        """
        Verifica que el grupo fue eliminado exitosamente
        Equivalente a: Verificar Grupo Eliminado
        """
        time.sleep(3)  # Esperar a que el mensaje aparezca
        
        # Buscar el mensaje más reciente dentro del contenedor de mensajes de Ant Design
        mensaje_locator = "xpath=//div[contains(@class, 'ant-message')]//span[contains(text(), '¡Registro eliminado exitosamente!')]"
        
        # Esperar a que el mensaje esté visible y usar el primero (más reciente)
        mensaje = self.page.locator(mensaje_locator).first
        mensaje.wait_for(state="visible", timeout=5000)
        
        # Verificar que el mensaje está visible
        expect(mensaje).to_be_visible()
    
    def filtrar_grupo_por_nombre(self, nombre_grupo: str):
        """
        Filtra la lista de grupos por nombre
        Equivalente a: Filtrar Grupo Por Nombre
        """
        ingresar_texto(self.page, self.NOMBRE_GRUPO_FIELD, nombre_grupo)
        time.sleep(1)

