"""
Script para mejorar el reporte HTML de pytest con CSS y JS personalizados
"""
import os
import re
from pathlib import Path

def mejorar_reporte_html(html_path="reports/report.html"):
    """Mejora el reporte HTML agregando CSS y JS personalizados"""
    
    if not os.path.exists(html_path):
        print(f"[ERROR] Archivo no encontrado: {html_path}")
        return False
    
    # Leer el contenido del HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Agregar CSS personalizado si no está
    css_link = '<link rel="stylesheet" href="custom.css">'
    if 'custom.css' not in content:
        # Buscar el cierre de </head> y agregar antes
        content = re.sub(r'</head>', f'    {css_link}\n</head>', content, count=1)
        print("[OK] CSS personalizado agregado")
    
    # Agregar JS personalizado si no está
    js_script = '<script src="custom.js"></script>'
    if 'custom.js' not in content:
        # Buscar el cierre de </body> y agregar antes
        content = re.sub(r'</body>', f'    {js_script}\n</body>', content, count=1)
        print("[OK] JavaScript personalizado agregado")
    
    # Mejorar el título si es necesario
    if '<title>' in content:
        content = re.sub(
            r'<title>.*?</title>',
            '<title>SISDEP - Reporte de Pruebas Automatizadas</title>',
            content
        )
    
    # Guardar el HTML mejorado
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] Reporte mejorado: {html_path}")
    return True

if __name__ == "__main__":
    import sys
    
    # Si se pasa un argumento, usar ese archivo
    html_file = sys.argv[1] if len(sys.argv) > 1 else "reports/report.html"
    
    mejorar_reporte_html(html_file)

