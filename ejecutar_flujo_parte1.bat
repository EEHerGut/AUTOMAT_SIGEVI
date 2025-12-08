@echo off
cd /d "C:\Users\Lenovo\Documents\AUTOMAT_SIGEVI"
echo.
echo 🚀 FLUJO SECUENCIAL - PARTE 1 (Pasos 1-5)
echo =====================================
echo.

echo 1. Operador - editar_solicitud.feature
behave features\Comision\Operador\editar_solicitud.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 1 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 1 COMPLETADO
echo.

echo 2. Autorizador - autorizar_solicitud.feature
behave features\Comision\Autorizador_SIGEVI\autorizar_solicitud.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 2 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 2 COMPLETADO
echo.

echo 5. Autorizador - depositar.feature
behave features\Comision\Autorizador_SIGEVI\depositar.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 5 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 5 COMPLETADO
echo.

echo ===================================================
echo ✅ PARTE 1 COMPLETADA EXITOSAMENTE!
echo 📝 Continúa con la Parte 2 para completar el flujo
echo.
pause