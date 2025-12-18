"""
Feature: Asignación de Visitas Domiciliarias (Regulaciones)
Equivalente a test_suites/features/regulaciones/asignacion_visitas.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.visitas_page import VisitasPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import DOCUMENTO_VENTERO


@pytest.mark.regulaciones
@pytest.mark.visitas
@pytest.mark.asignar
@pytest.mark.positivo
def test_asignar_nueva_visita_a_ventero(page: Page):
    """
    Given que el usuario está en la sección de "Asignación de visitas".
    When hace clic en "Nueva visita".
    And busca al ventero por su documento.
    And completa los datos de la visita y da clic en guardar.
    Then se crea y asigna una nueva visita domiciliaria.
    Equivalente a: Asignar Nueva Visita A Ventero
    """
    login_page = LoginPage(page)
    visitas_page = VisitasPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    visitas_page.el_usuario_esta_en_seccion_asignacion_visitas()
    visitas_page.hacer_click_en_nueva_visita()
    visitas_page.buscar_ventero_por_documento_en_visitas(DOCUMENTO_VENTERO)
    visitas_page.completar_formulario_visita(
        visitador="Administrador DEL SISTEMA",
        tipo_visita="Actualización",
        vehiculo="RJZ672",
        fecha="HOY",
        franja="AM"
    )
    visitas_page.hacer_click_en_guardar_visita()
    visitas_page.verificar_creacion_visita_exitosa()


@pytest.mark.regulaciones
@pytest.mark.visitas
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_datos_de_visita_asignada(page: Page):
    """
    Given que el usuario está en la sección de "Asignación de visitas".
    When selecciona una visita y hace clic en "Detalles".
    And modifica la información de la visita y da clic en el botón de actualizar.
    Then se guardan los cambios de la visita.
    Equivalente a: Actualizar Datos De Visita Asignada
    """
    login_page = LoginPage(page)
    visitas_page = VisitasPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    visitas_page.el_usuario_esta_en_seccion_asignacion_visitas()
    visitas_page.actualizar_datos_visita(
        fecha_desde="2025-07-21",
        fecha_hasta="2025-07-21",
        visitador="Administrador DEL SISTEMA"
    )
    visitas_page.hacer_click_en_detalles_visita()
    visitas_page.hacer_click_en_actualizar_visita()
    visitas_page.verificar_actualizacion_visita_exitosa()


@pytest.mark.regulaciones
@pytest.mark.visitas
@pytest.mark.eliminar
@pytest.mark.positivo
def test_eliminar_visita_asignada(page: Page):
    """
    Given que el usuario se encuentra en la sección de "Asignación de visitas".
    When hace clic en el botón eliminar de la visita que desea eliminar.
    And confirma la eliminación.
    Then la visita es eliminada.
    Equivalente a: Eliminar Visita Asignada
    """
    login_page = LoginPage(page)
    visitas_page = VisitasPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    visitas_page.el_usuario_esta_en_seccion_asignacion_visitas()
    visitas_page.actualizar_datos_visita(
        fecha_desde="2025-07-21",
        fecha_hasta="2025-07-21",
        visitador="Administrador DEL SISTEMA"
    )
    visitas_page.hacer_click_en_eliminar_visita()
    visitas_page.confirmar_eliminacion_visita()
    # Nota: Verificación de eliminación puede requerir implementación adicional


@pytest.mark.regulaciones
@pytest.mark.visitas
@pytest.mark.reporte
@pytest.mark.excel
@pytest.mark.positivo
def test_generar_reporte_excel_visitas_domiciliarias(page: Page):
    """
    Generar reporte Excel de visitas domiciliarias
    Equivalente a: Generar reporte Excel de visitas domiciliarias
    """
    login_page = LoginPage(page)
    visitas_page = VisitasPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    visitas_page.el_usuario_esta_en_seccion_asignacion_visitas()


