"""
Helpers comunes reutilizables para el proyecto SISDEP
Equivalente a resources/common_keywords.robot
"""
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from playwright.sync_api import Page, expect
from typing import Optional
import os
from datetime import datetime
from config.config import SCREENSHOT_DIR, EXPLICIT_WAIT


def esperar_elemento_visible(page: Page, locator: str, timeout: Optional[int] = None):
    """
    Espera a que un elemento sea visible
    Equivalente a: Esperar Elemento Visible
    """
    timeout = timeout or EXPLICIT_WAIT
    page.wait_for_selector(locator, state="visible", timeout=timeout)


def esperar_elemento_clickable(page: Page, locator: str, timeout: Optional[int] = None):
    """
    Espera a que un elemento sea clickeable
    Equivalente a: Esperar Elemento Clickable
    """
    timeout = timeout or EXPLICIT_WAIT
    page.wait_for_selector(locator, state="visible", timeout=timeout)
    # Verificar que el elemento esté habilitado
    element = page.locator(locator)
    expect(element).to_be_enabled(timeout=timeout)


def hacer_click_en_elemento(page: Page, locator: str, timeout: Optional[int] = None):
    """
    Hace click en un elemento después de esperar que sea clickeable
    Equivalente a: Hacer Click En Elemento
    """
    esperar_elemento_clickable(page, locator, timeout)
    page.click(locator)


def ingresar_texto(page: Page, locator: str, texto: str, timeout: Optional[int] = None):
    """
    Ingresa texto en un campo después de esperar que sea visible
    Equivalente a: Ingresar Texto
    """
    esperar_elemento_visible(page, locator, timeout)
    page.fill(locator, texto)


def verificar_texto_en_pagina(page: Page, texto: str, timeout: Optional[int] = None):
    """
    Verifica que un texto esté presente en la página
    Equivalente a: Verificar Texto En Página
    """
    timeout = timeout or EXPLICIT_WAIT
    expect(page.locator(f"text={texto}")).to_be_visible(timeout=timeout)


def verificar_url_contiene(page: Page, texto: str, timeout: Optional[int] = None):
    """
    Verifica que la URL actual contenga un texto específico
    Equivalente a: Verificar URL Contiene
    """
    timeout = timeout or EXPLICIT_WAIT
    page.wait_for_url(f"*{texto}*", timeout=timeout)


def tomar_screenshot(page: Page, nombre: str = "screenshot"):
    """
    Toma una captura de pantalla con nombre personalizado
    Equivalente a: Tomar Screenshot
    """
    # Asegurar que el directorio existe
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{nombre}_{timestamp}.png"
    screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
    
    page.screenshot(path=screenshot_path)
    print(f"Screenshot guardado como: {screenshot_path}")
    return screenshot_path


def verificar_elemento_presente(page: Page, locator: str, timeout: Optional[int] = None):
    """
    Verifica que un elemento esté presente en la página
    Equivalente a: Verificar Elemento Presente
    Si hay múltiples elementos, usa el primero
    """
    timeout = timeout or EXPLICIT_WAIT
    locator_obj = page.locator(locator)
    # Si hay múltiples elementos, usar el primero
    if locator_obj.count() > 1:
        expect(locator_obj.first).to_be_visible(timeout=timeout)
    else:
        expect(locator_obj).to_be_visible(timeout=timeout)


def limpiar_campo(page: Page, locator: str):
    """
    Limpia el contenido de un campo de texto
    Equivalente a: Limpiar Campo
    """
    page.fill(locator, "")


def navegar_a_sisdep_con_reintentos(page: Page, url: str, max_intentos: int = 3):
    """
    Navega a SISDEP con reintentos en caso de error de conectividad
    Equivalente a: Navegar A SISDEP Con Reintentos
    """
    import time
    
    for intento in range(1, max_intentos + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_selector("body", timeout=10000)
            print(f"Navegación exitosa en intento {intento}")
            return
        except Exception as error:
            print(f"Intento {intento} falló: {error}")
            if intento < max_intentos:
                time.sleep(5)
            else:
                raise Exception(f"No se pudo conectar después de {max_intentos} intentos")

