"""
Feature: Gestión de Módulos (Regulaciones)
Equivalente a test_suites/features/regulaciones/gestion_modulos.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.modulos_page import ModulosPage
from config.config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.regulaciones
@pytest.mark.modulos
@pytest.mark.crear
@pytest.mark.positivo
def test_registrar_nuevo_modulo(page: Page):
    """
    Given que el usuario está en la sección de "Módulos".
    When hace clic en el botón "Agregar".
    And completa el formulario con los datos del nuevo módulo y hace clic en "Guardar".
    Then el nuevo módulo se registra en el sistema.
    Equivalente a: Registrar Nuevo Modulo
    """
    login_page = LoginPage(page)
    modulos_page = ModulosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección módulos
    modulos_page.el_usuario_esta_en_seccion_modulos()
    
    # Agregar nuevo módulo
    modulos_page.hacer_click_en_agregar_modulo()
    modulos_page.completar_formulario_modulo(
        tenencia="Propia",
        estado="Bueno",
        fondo="10.5",
        frente="5.2",
        alto="3.0",
        tipo_modulo="Oriental",
        tipo_otro_modulo="Tipo 1",
        sector_modulo="Estadio"
    )
    modulos_page.hacer_click_en_guardar_modulo()
    modulos_page.verificar_creacion_modulo_exitosa()


@pytest.mark.regulaciones
@pytest.mark.modulos
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_informacion_modulo_existente(page: Page):
    """
    Given que el usuario está en la sección de "Módulos".
    When selecciona un módulo y hace clic en "Detalles".
    And modifica los datos del módulo y hace clic en "Guardar".
    Then la información del módulo es actualizada.
    Equivalente a: Actualizar Informacion Modulo Existente
    """
    login_page = LoginPage(page)
    modulos_page = ModulosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección módulos
    modulos_page.el_usuario_esta_en_seccion_modulos()
    
    # Filtrar y editar módulo
    modulos_page.filtrar_modulo_por_serial("10-AVPL-002")
    modulos_page.hacer_click_en_detalles_modulo()
    page.reload()
    modulos_page.hacer_click_en_guardar_modulo_actualizar()
    modulos_page.verificar_actualizacion_modulo_exitosa()


@pytest.mark.regulaciones
@pytest.mark.modulos
@pytest.mark.eliminar
@pytest.mark.positivo
def test_eliminar_modulo(page: Page):
    """
    Given que el usuario está en la lista de "Módulos".
    When hace clic en "Eliminar" en un módulo específico.
    And confirma la eliminación.
    Then el módulo es eliminado del sistema.
    Equivalente a: Eliminar Modulo
    """
    login_page = LoginPage(page)
    modulos_page = ModulosPage(page)
    
    # Navegar y hacer login
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    
    # Ir a sección módulos
    modulos_page.el_usuario_esta_en_seccion_modulos()
    
    # Filtrar y eliminar módulo
    modulos_page.filtrar_modulo_por_serial("10-AVPL-002")
    modulos_page.hacer_click_en_eliminar_modulo()
    # Nota: Puede requerir confirmación adicional según la implementación


@pytest.mark.regulaciones
@pytest.mark.modulos
@pytest.mark.reporte
@pytest.mark.excel
@pytest.mark.positivo
def test_generar_reporte_excel_modulos(page: Page):
    """
    Generar reporte Excel de módulos
    Equivalente a: Generar reporte Excel de módulos
    """
    login_page = LoginPage(page)
    modulos_page = ModulosPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    modulos_page.el_usuario_esta_en_seccion_modulos()
    modulos_page.hacer_click_en_boton_excel()


@pytest.mark.regulaciones
@pytest.mark.modulos
@pytest.mark.eliminar
@pytest.mark.negativo
def test_eliminar_modulo_en_uso(page: Page):
    """
    Intentar eliminar un módulo que está en uso
    Equivalente a: Eliminar un módulo (en uso)
    """
    login_page = LoginPage(page)
    modulos_page = ModulosPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    modulos_page.el_usuario_esta_en_seccion_modulos()
    
    # Filtrar un módulo que esté en uso (debe existir uno previamente)
    # Nota: Se necesita un serial de un módulo que esté en uso
    modulos_page.filtrar_modulo_por_serial("10-AVPL-002")
    modulos_page.hacer_click_en_eliminar_modulo()
    modulos_page.confirmar_eliminacion_modulo()
    modulos_page.verificar_modulo_no_eliminado()

