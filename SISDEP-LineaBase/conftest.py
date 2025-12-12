"""
Configuración de pytest y fixtures para Playwright
Equivalente a la configuración de Suite Setup/Teardown en Robot Framework
"""
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from config.config import (
    BROWSER,
    BROWSER_HEADLESS,
    IMPLICIT_WAIT,
    PAGE_LOAD_TIMEOUT,
    SISDEP_URL
)
import os


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configuración de argumentos del navegador"""
    return {
        "headless": BROWSER_HEADLESS,
        "args": [
            "--ignore-ssl-errors",
            "--ignore-certificate-errors",
            "--allow-running-insecure-content",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-plugins"
        ]
    }


@pytest.fixture(scope="session")
def browser(browser_type_launch_args):
    """Fixture para crear el navegador (sesión completa)"""
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        # Seleccionar el tipo de navegador
        if BROWSER == "chromium":
            browser = p.chromium.launch(**browser_type_launch_args)
        elif BROWSER == "firefox":
            browser = p.firefox.launch(**browser_type_launch_args)
        elif BROWSER == "webkit":
            browser = p.webkit.launch(**browser_type_launch_args)
        else:
            browser = p.chromium.launch(**browser_type_launch_args)
        
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    """Fixture para crear un contexto de navegador (por test)"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )
    context.set_default_timeout(IMPLICIT_WAIT)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Fixture para crear una página (por test)
    Equivalente a Setup/Teardown en Robot Framework
    """
    page = context.new_page()
    page.set_default_timeout(IMPLICIT_WAIT)
    page.set_default_navigation_timeout(PAGE_LOAD_TIMEOUT)
    
    yield page
    
    # Teardown: cerrar página
    page.close()


def pytest_configure(config):
    """Configuración inicial de pytest"""
    # Crear directorios necesarios
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    # Agregar CSS y JS personalizados al reporte HTML
    if hasattr(config.option, 'htmlpath'):
        enhance_html_report(config)


def enhance_html_report(config):
    """Mejora el reporte HTML con CSS y JS personalizados"""
    try:
        # Esto se ejecutará después de que pytest genere el HTML
        # El CSS y JS se agregarán automáticamente si están en la carpeta reports
        pass
    except Exception as e:
        print(f"Nota: No se pudo mejorar el reporte HTML: {e}")


def pytest_html_report_title(report):
    """Personaliza el título del reporte HTML"""
    report.title = "SISDEP - Reporte de Pruebas Automatizadas"


def pytest_html_results_summary(prefix, summary, postfix):
    """Personaliza el resumen del reporte HTML"""
    # Agregar información adicional al resumen
    prefix.extend([
        '<div class="header">',
        '<h1>🧪 SISDEP - Reporte de Pruebas</h1>',
        '<div class="subtitle">Pruebas Automatizadas con Playwright</div>',
        '</div>'
    ])


def pytest_sessionfinish(session, exitstatus):
    """Limpieza al finalizar la sesión de pruebas"""
    # Agregar CSS y JS al reporte HTML generado
    try:
        html_path = "reports/report.html"
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Agregar CSS personalizado
            css_link = '<link rel="stylesheet" href="custom.css">'
            if 'custom.css' not in content:
                content = content.replace('</head>', f'    {css_link}\n</head>')
            
            # Agregar JS personalizado
            js_script = '<script src="custom.js"></script>'
            if 'custom.js' not in content:
                content = content.replace('</body>', f'    {js_script}\n</body>')
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f"Nota: No se pudo mejorar el reporte HTML: {e}")
