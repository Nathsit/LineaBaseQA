"""
Feature: Gestión de Autorizaciones (Regulaciones)
Equivalente a test_suites/features/regulaciones/gestion_autorizaciones.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.autorizaciones_page import AutorizacionesPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import DOCUMENTO_VENTERO, RADICADO_MERCURIO, FECHA_INICIAL, HORA_INICIO, HORA_FIN


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.crear
@pytest.mark.positivo
def test_creacion_nueva_solicitud_autorizacion(page: Page):
    """
    Crear una nueva solicitud de autorización para un ventero
    Equivalente a: Creacion Nueva Solicitud Autorizacion
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.buscar_ventero_por_documento(DOCUMENTO_VENTERO)
    autorizaciones_page.completar_datos_solicitud_autorizacion(
        RADICADO_MERCURIO, FECHA_INICIAL, HORA_INICIO, HORA_FIN
    )
    autorizaciones_page.hacer_click_en_guardar_solicitud()
    autorizaciones_page.el_sistema_crea_nueva_solicitud_autorizacion()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.visita
@pytest.mark.positivo
def test_agregar_visita_administrativa_a_autorizacion(page: Page):
    """
    Agregar una visita administrativa a una autorización existente
    Equivalente a: Agregar Visita Administrativa A Autorizacion
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.acceder_a_detalles_autorizacion(RADICADO_MERCURIO)
    autorizaciones_page.hacer_click_en_agregar_visita_administrativa()
    autorizaciones_page.agregar_visita_administrativa_a_autorizacion()
    autorizaciones_page.el_sistema_registra_visita_administrativa()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.resolucion
@pytest.mark.positivo
def test_agregar_resolucion_a_solicitud_autorizacion(page: Page):
    """
    Agregar una resolución a una solicitud de autorización
    Equivalente a: Agregar Resolucion A Solicitud Autorizacion
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.acceder_a_detalles_autorizacion(RADICADO_MERCURIO)
    autorizaciones_page.hacer_click_en_agregar_resolucion()
    # Nota: Completar formulario de resolución según implementación


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.resolucion
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_resolucion(page: Page):
    """
    Actualizar una resolución de una autorización existente
    Equivalente a: Actualizar Resolucion
    Flujo: Filtrar por radicado -> Detalle -> Recargar -> Guardar
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    # Actualizar la resolución usando el radicado del primer test
    autorizaciones_page.actualizar_resolucion(RADICADO_MERCURIO)
    autorizaciones_page.verificar_actualizacion_resolucion_exitosa()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_informacion_general_autorizacion(page: Page):
    """
    Actualizar la información general de una autorización existente
    Equivalente a: Actualizar Informacion General Autorizacion
    Flujo: Filtrar por radicado -> Detalle -> Recargar -> Guardar
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    # Actualizar la información general usando el radicado del primer test
    autorizaciones_page.actualizar_informacion_general_autorizacion(RADICADO_MERCURIO)
    autorizaciones_page.verificar_actualizacion_autorizacion_exitosa()

@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.visita
@pytest.mark.actualizar
@pytest.mark.positivo
def test_actualizar_visita_administrativa(page: Page):
    """
    Actualizar una visita administrativa de una autorización existente
    Equivalente a: Actualizar Visita Administrativa
    Flujo: Filtrar por radicado -> Detalle -> Ver visita domiciliaria -> OK
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    # Actualizar la visita administrativa usando el radicado del primer test
    autorizaciones_page.actualizar_visita_administrativa(RADICADO_MERCURIO)
    autorizaciones_page.verificar_actualizacion_visita_administrativa_exitosa()

@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.resolucion
@pytest.mark.negativo
def test_agregar_resolucion_con_fechas_diferentes(page: Page):
    """
    Agregar una resolución a una solicitud de autorización con fechas diferentes
    Equivalente a: Agregar Resolucion A Solicitud Autorizacion con fechas diferentes
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.acceder_a_detalles_autorizacion(RADICADO_MERCURIO)
    autorizaciones_page.el_sistema_muestra_que_las_fechas_no_pueden_ser_diferentes()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.eliminar
@pytest.mark.positivo
def test_eliminar_autorizacion(page: Page):
    """
    Eliminar una autorización del sistema
    Equivalente a: Eliminar Autorizacion
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.hacer_click_en_eliminar_autorizacion(RADICADO_MERCURIO)
    autorizaciones_page.confirmar_eliminacion_autorizacion()
    autorizaciones_page.el_sistema_elimina_la_autorizacion()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.reporte
@pytest.mark.excel
@pytest.mark.positivo
def test_generar_reporte_autorizaciones_excel(page: Page):
    """
    Generar reporte de autorizaciones en Excel
    Equivalente a: Generar Reporte Autorizaciones Excel
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.hacer_click_en_boton_excel()


@pytest.mark.regulaciones
@pytest.mark.autorizaciones
@pytest.mark.crear
@pytest.mark.negativo
def test_creacion_nueva_solicitud_autorizacion_ventero_no_existente(page: Page):
    """
    Crear una nueva solicitud de autorización para un ventero que no existe
    Equivalente a: Creacion Nueva Solicitud Autorizacion ventero no existente
    """
    login_page = LoginPage(page)
    autorizaciones_page = AutorizacionesPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    autorizaciones_page.el_usuario_esta_en_seccion_autorizaciones()
    autorizaciones_page.buscar_ventero_por_documento("1001022434")
    autorizaciones_page.el_sistema_muestra_que_el_ventero_no_existe()




