@echo off
echo ========================================
echo   Generando Reporte HTML Mejorado
echo ========================================
echo.

echo [1/2] Ejecutando tests...
pytest tests/features -v --html=reports/report.html --self-contained-html

echo.
echo [2/2] Mejorando reporte con CSS y JS personalizados...
python mejorar_reporte.py reports/report.html

echo.
echo ========================================
echo   Reporte generado exitosamente!
echo ========================================
echo.
echo Reporte disponible en: reports/report.html
echo.
echo ¿Deseas abrir el reporte ahora? (S/N)
set /p respuesta=
if /i "%respuesta%"=="S" (
    start reports\report.html
)

pause

