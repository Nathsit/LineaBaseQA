"""
Feature: Gestión de Grupos y Permisos (Administración)
Equivalente a test_suites/features/administracion/gestion_grupos_permisos.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.grupos_page import GruposPage
from config.config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.administracion
@pytest.mark.grupos
@pytest.mark.permisos
@pytest.mark.positivo
@pytest.mark.funcional
def test_creacion_de_nuevo_grupo_con_permisos_especificos(page: Page):
    """
    Given que el administrador está en la sección "Administración - Grupos y Permisos".
    Equivalente a: Creacion De Nuevo Grupo Con Permisos Especificos
    """
    login_page = LoginPage(page)
    grupos_page = GruposPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección grupos y permisos
    grupos_page.ir_a_seccion_grupos_y_permisos()
    grupos_page.crear_nuevo_grupo_con_permisos("Grupo Prueba", "Permiso1,Permiso2")
    grupos_page.verificar_grupo_creado("Grupo Prueba")


@pytest.mark.administracion
@pytest.mark.grupos
@pytest.mark.permisos
@pytest.mark.funcional
def test_actualizacion_de_permisos_de_grupo(page: Page):
    """
    Given que el administrador está en la sección "Administración - Grupos y Permisos".
    Equivalente a: Actualizacion De Permisos De Grupo
    """
    login_page = LoginPage(page)
    grupos_page = GruposPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección grupos y permisos
    grupos_page.ir_a_seccion_grupos_y_permisos()
    grupos_page.seleccionar_grupo_para_editar("Grupo Prueba")
    grupos_page.actualizar_permisos_de_grupo("Permiso3,Permiso4")
    grupos_page.verificar_permisos_actualizados()


@pytest.mark.administracion
@pytest.mark.grupos
@pytest.mark.permisos
@pytest.mark.funcional
def test_eliminacion_de_grupo(page: Page):
    """
    Given que el administrador se encuentra en la sección de "Grupos y Permisos".
    Equivalente a: Eliminacion De Grupo
    """
    login_page = LoginPage(page)
    grupos_page = GruposPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección grupos y permisos
    grupos_page.ir_a_seccion_grupos_y_permisos()
    grupos_page.seleccionar_grupo_para_eliminar("Grupo Prueba")
    grupos_page.eliminar_grupo()

