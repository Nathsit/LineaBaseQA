"""
Feature: Gestión de Usuarios (Administración)
Equivalente a test_suites/features/administracion/gestion_usuarios.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.usuarios_page import UsuariosPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import NUEVO_USUARIO, EMAIL_USUARIO_ACTUALIZADO


@pytest.mark.administracion
@pytest.mark.usuarios
@pytest.mark.positivo
@pytest.mark.funcional
def test_registro_de_nuevo_usuario_exitoso(page: Page):
    """
    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    Equivalente a: Registro De Nuevo Usuario Exitoso
    """
    login_page = LoginPage(page)
    usuarios_page = UsuariosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección usuarios
    usuarios_page.ir_a_seccion_usuarios()
    
    # Abrir formulario de nuevo usuario
    usuarios_page.hacer_click_en_agregar_usuario()
    usuarios_page.verificar_formulario_visible()
    
    # Llenar todos los campos del formulario
    usuarios_page.llenar_formulario_usuario(
        nombre=NUEVO_USUARIO["nombre"],
        apellido=NUEVO_USUARIO["apellido"],
        tipo_documento=NUEVO_USUARIO["tipo_documento"],
        documento=NUEVO_USUARIO["documento"],
        grupo=NUEVO_USUARIO["grupo"],
        email=NUEVO_USUARIO["email"]
    )
    
    # Guardar el usuario
    usuarios_page.guardar_usuario()
    
    # Verificar que el usuario fue creado exitosamente
    usuarios_page.verificar_usuario_creado()

@pytest.mark.administracion
@pytest.mark.usuarios
@pytest.mark.positivo
@pytest.mark.funcional
def test_registro_de_nuevo_usuario_ya_existente(page: Page):
    """
    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    Equivalente a: Registro De Nuevo Usuario ya Existente
    Nota: Este test intenta crear un usuario con el mismo documento que NUEVO_USUARIO
    """
    login_page = LoginPage(page)
    usuarios_page = UsuariosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección usuarios
    usuarios_page.ir_a_seccion_usuarios()
    
    # Abrir formulario
    usuarios_page.hacer_click_en_agregar_usuario()
    usuarios_page.verificar_formulario_visible()
    
    # Intentar crear un usuario con el mismo documento que NUEVO_USUARIO
    # (esto debería fallar porque el usuario ya existe)
    usuarios_page.llenar_formulario_usuario(
        nombre="Otro",
        apellido="Usuario",
        tipo_documento=NUEVO_USUARIO["tipo_documento"],
        documento=NUEVO_USUARIO["documento"],  # Mismo documento
        grupo=NUEVO_USUARIO["grupo"],
        email="otro.usuario@prueba.com"
    )
    
    usuarios_page.guardar_usuario()
    
@pytest.mark.administracion
@pytest.mark.usuarios
@pytest.mark.funcional
def test_actualizacion_de_informacion_de_usuario(page: Page):
    """
    Given que el administrador está en la sección "Administración - Usuarios".
    Equivalente a: Actualizacion De Informacion De Usuario
    Nota: Este test actualiza el usuario creado en test_registro_de_nuevo_usuario_exitoso
    """
    login_page = LoginPage(page)
    usuarios_page = UsuariosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección usuarios
    usuarios_page.ir_a_seccion_usuarios()
    
    # Buscar y editar usuario usando el documento del NUEVO_USUARIO
    usuarios_page.ingresar_texto_en_filtro_documento(NUEVO_USUARIO["documento"])
    usuarios_page.seleccionar_usuario_por_documento(NUEVO_USUARIO["documento"])
    usuarios_page.editar_solo_email_usuario(EMAIL_USUARIO_ACTUALIZADO)
    usuarios_page.verificar_email_actualizado()


@pytest.mark.administracion
@pytest.mark.usuarios
@pytest.mark.funcional
def test_eliminacion_de_usuario_existente(page: Page):
    """
    Given que el administrador está en la sección "Administración - Usuarios".
    Equivalente a: Eliminacion De Usuario Existente
    Nota: Este test elimina el usuario creado en test_registro_de_nuevo_usuario_exitoso
    """
    login_page = LoginPage(page)
    usuarios_page = UsuariosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección usuarios
    usuarios_page.ir_a_seccion_usuarios()
    
    # Buscar y eliminar usuario usando el documento del NUEVO_USUARIO
    usuarios_page.ingresar_texto_en_filtro_documento(NUEVO_USUARIO["documento"])
    usuarios_page.seleccionar_usuario_por_documento(NUEVO_USUARIO["documento"])
    usuarios_page.eliminar_usuario()


@pytest.mark.administracion
@pytest.mark.usuarios
@pytest.mark.positivo
@pytest.mark.funcional
def test_registro_de_nuevo_usuario_campos_vacios(page: Page):
    """
    Given que el administrador ha iniciado sesión y se encuentra en la sección "Administración - Usuarios".
    Equivalente a: Registro De Nuevo Usuario Campos Vacios
    """
    login_page = LoginPage(page)
    usuarios_page = UsuariosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección usuarios
    usuarios_page.ir_a_seccion_usuarios()
    
    # Abrir formulario y verificar validación
    usuarios_page.hacer_click_en_agregar_usuario()
    usuarios_page.verificar_formulario_visible()
    usuarios_page.ingresar_texto_en_campos_vacios()




