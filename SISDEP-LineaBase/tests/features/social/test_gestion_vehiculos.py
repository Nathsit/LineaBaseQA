"""
Feature: Gestión de Vehículos (Social)
Equivalente a test_suites/features/social/gestion_vehiculos.robot
"""
import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page
from page_objects.login_page import LoginPage
from page_objects.vehiculos_page import VehiculosPage
from config.config import VALID_USERNAME, VALID_PASSWORD
from data.test_data import NOMBRE_CONDUCTOR, PLACA_VEHICULO, TIPO_VEHICULO, PLACA_VEHICULO_EN_USO


@pytest.mark.social
@pytest.mark.vehiculos
@pytest.mark.crear
@pytest.mark.positivo
def test_01_registrar_nuevo_vehiculo(page: Page):
    """
    Registrar un nuevo vehículo
    Equivalente a: Registrar Nuevo Vehiculo
    """
    login_page = LoginPage(page)
    vehiculos_page = VehiculosPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    vehiculos_page.ir_a_seccion_vehiculos()
    vehiculos_page.hacer_click_en_agregar_vehiculo()
    vehiculos_page.completar_formulario_vehiculo(
        nombre_conductor=NOMBRE_CONDUCTOR,
        placa=PLACA_VEHICULO,
        tipo_vehiculo=TIPO_VEHICULO
    )
    vehiculos_page.hacer_click_en_guardar_vehiculo()
    vehiculos_page.verificar_creacion_vehiculo_exitosa()
    # Guardar la placa para usar en el test de actualizar
    pytest.placa_vehiculo_creado = PLACA_VEHICULO


@pytest.mark.social
@pytest.mark.vehiculos
@pytest.mark.actualizar
@pytest.mark.positivo
def test_02_actualizar_vehiculo(page: Page):
    """
    Actualizar un vehículo existente
    Equivalente a: Actualizar Vehiculo
    """
    login_page = LoginPage(page)
    vehiculos_page = VehiculosPage(page)
    
    # Usar la placa del vehículo creado en el test anterior
    placa = getattr(pytest, 'placa_vehiculo_creado', PLACA_VEHICULO)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    vehiculos_page.ir_a_seccion_vehiculos()
    # Filtrar por el vehículo creado y acceder a detalles
    vehiculos_page.acceder_a_detalles_vehiculo(placa)
    # Actualizar solo el nombre del conductor
    vehiculos_page.actualizar_datos_vehiculo(
        nombre_conductor="Conductor Actualizado Test"
    )
    # Usar el botón de actualizar (type="submit" con ant-btn-lg)
    vehiculos_page.hacer_click_en_guardar_vehiculo_actualizar()
    vehiculos_page.verificar_actualizacion_vehiculo_exitosa()


@pytest.mark.social
@pytest.mark.vehiculos
@pytest.mark.eliminar
@pytest.mark.positivo
def test_03_eliminar_vehiculo_no_utilizado(page: Page):
    """
    Eliminar un vehículo que no está en uso
    Equivalente a: Eliminar Vehiculo No Utilizado
    """
    login_page = LoginPage(page)
    vehiculos_page = VehiculosPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    vehiculos_page.ir_a_seccion_vehiculos()
    vehiculos_page.eliminar_vehiculo_por_placa(PLACA_VEHICULO)
    vehiculos_page.confirmar_eliminacion_vehiculo()
    vehiculos_page.verificar_vehiculo_eliminado()


@pytest.mark.social
@pytest.mark.vehiculos
@pytest.mark.eliminar
@pytest.mark.negativo
def test_04_eliminar_vehiculo_utilizado(page: Page):
    """
    Intentar eliminar un vehículo que está en uso
    Equivalente a: Eliminar Vehiculo Utilizado
    """
    login_page = LoginPage(page)
    vehiculos_page = VehiculosPage(page)
    
    login_page.navegar_a_sisdep()
    login_page.realizar_login_sisdep(VALID_USERNAME, VALID_PASSWORD)
    vehiculos_page.ir_a_seccion_vehiculos()
    vehiculos_page.eliminar_vehiculo_por_placa(PLACA_VEHICULO_EN_USO)
    vehiculos_page.confirmar_eliminacion_vehiculo()
    vehiculos_page.verificar_vehiculo_no_eliminado()




