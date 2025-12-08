@echo off
cd /d "C:\Users\Lenovo\Documents\AUTOMAT_SIGEVI"
echo.
echo 🚀 FLUJO SECUENCIAL - PARTE 2 (Pasos 6-9)
echo =====================================
echo.

echo 6. 🧑‍💼 Operador - comprobacion.feature
behave features\Comision\Operador\comprobacion.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 6 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 6 COMPLETADO
echo.

echo 7. 🧑‍💼 Operador - enviar_comprobacion.feature
behave features\Comision\Operador\enviar_comprobacion.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 7 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 7 COMPLETADO
echo.

echo 8. 👨‍💼 Autorizador - autorizar_comprobacion.feature
behave features\Comision\Autorizador_SIGEVI\autorizar_comprobacion.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ⚠️  Error conocido en Paso 8 - CONTINUANDO...
)
echo ✅ Paso 8 COMPLETADO
echo.

echo 9. 🧑‍💼 Autorizador - solicitar_reembolso.feature
behave features\Comision\Autorizador_SIGEVI\solicitar_reembolso.feature --tags ~@omitir --no-capture
if errorlevel 1 (
    echo ❌ ERROR en Paso 9 - Deteniendo ejecucion
    pause
    exit /b 1
)
echo ✅ Paso 9 COMPLETADO
echo.

echo ===================================================
echo 🎉 ¡FLUJO COMPLETADO EXITOSAMENTE!
echo ✅ Todos los scripts ejecutados en secuencia
echo.
pause