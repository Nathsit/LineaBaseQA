"""
Script para generar reportes HTML separados por feature
Cada feature (administracion, autenticacion, regulaciones, social) 
generará su propio reporte en una carpeta específica
"""
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Mapeo de features a sus rutas
FEATURES = {
    "autenticacion": "tests/features/autenticacion",
    "administracion": "tests/features/administracion",
    "regulaciones": "tests/features/regulaciones",
    "social": "tests/features/social"
}

def crear_directorio_reports(feature_name: str):
    """Crea el directorio de reportes para un feature"""
    reports_dir = Path(f"reports/{feature_name}")
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir

def ejecutar_tests_feature(feature_name: str, feature_path: str):
    """Ejecuta los tests de un feature y genera su reporte"""
    print(f"\n{'='*60}")
    print(f"  Ejecutando tests de: {feature_name.upper()}")
    print(f"{'='*60}\n")
    
    # Crear directorio de reportes para este feature
    reports_dir = crear_directorio_reports(feature_name)
    report_path = reports_dir / "report.html"
    
    # Comando pytest para ejecutar el feature
    cmd = [
        sys.executable, "-m", "pytest",
        feature_path,
        "-v",
        f"--html={report_path}",
        "--self-contained-html"
    ]
    
    try:
        # Ejecutar los tests
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Mostrar salida
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        
        # Mejorar el reporte con CSS personalizado
        mejorar_reporte(report_path)
        
        print(f"\n✓ Reporte generado: {report_path}")
        return result.returncode == 0
        
    except Exception as e:
        print(f"✗ Error ejecutando tests de {feature_name}: {e}")
        return False

def mejorar_reporte(report_path: Path):
    """Mejora el reporte HTML con CSS personalizado"""
    try:
        from mejorar_reporte import mejorar_reporte_html
        mejorar_reporte_html(str(report_path))
    except Exception as e:
        print(f"  Nota: No se pudo mejorar el reporte: {e}")

def generar_reporte_consolidado():
    """Genera un reporte consolidado con todos los features"""
    print(f"\n{'='*60}")
    print(f"  Generando reporte consolidado")
    print(f"{'='*60}\n")
    
    reports_dir = Path("reports")
    report_path = reports_dir / "report.html"
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/features",
        "-v",
        f"--html={report_path}",
        "--self-contained-html"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        mejorar_reporte(report_path)
        print(f"\n✓ Reporte consolidado generado: {report_path}")
        return result.returncode == 0
    except Exception as e:
        print(f"✗ Error generando reporte consolidado: {e}")
        return False

def main():
    """Función principal"""
    print("="*60)
    print("  GENERADOR DE REPORTES POR FEATURE")
    print("="*60)
    print(f"\nFecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Crear directorio principal de reportes
    Path("reports").mkdir(exist_ok=True)
    
    resultados = {}
    
    # Ejecutar tests de cada feature
    for feature_name, feature_path in FEATURES.items():
        if Path(feature_path).exists():
            exito = ejecutar_tests_feature(feature_name, feature_path)
            resultados[feature_name] = exito
        else:
            print(f"\n⚠ Feature '{feature_name}' no encontrado en {feature_path}")
            resultados[feature_name] = False
    
    # Generar reporte consolidado
    generar_reporte_consolidado()
    
    # Resumen
    print(f"\n{'='*60}")
    print("  RESUMEN DE EJECUCIÓN")
    print(f"{'='*60}\n")
    
    for feature_name, exito in resultados.items():
        status = "✓ EXITOSO" if exito else "✗ FALLIDO"
        report_path = Path(f"reports/{feature_name}/report.html")
        print(f"  {feature_name.upper():20} {status:15} -> {report_path}")
    
    print(f"\n  Reporte consolidado -> reports/report.html")
    print(f"\n{'='*60}\n")
    
    # Abrir reportes si se solicita
    print("¿Deseas abrir algún reporte?")
    print("  1. Autenticación")
    print("  2. Administración")
    print("  3. Regulaciones")
    print("  4. Social")
    print("  5. Consolidado")
    print("  0. No abrir")
    
    try:
        opcion = input("\nOpción: ").strip()
        reportes = {
            "1": "reports/autenticacion/report.html",
            "2": "reports/administracion/report.html",
            "3": "reports/regulaciones/report.html",
            "4": "reports/social/report.html",
            "5": "reports/report.html"
        }
        
        if opcion in reportes:
            report_path = Path(reportes[opcion])
            if report_path.exists():
                import webbrowser
                webbrowser.open(f"file://{report_path.absolute()}")
            else:
                print(f"El reporte {report_path} no existe")
    except:
        pass

if __name__ == "__main__":
    main()

