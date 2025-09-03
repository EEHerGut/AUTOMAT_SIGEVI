# environment.py


import os
import logging
import allure
import csv
import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from logging.handlers import RotatingFileHandler
from datetime import datetime
from allure_commons.types import AttachmentType
from utils.data_loader import load_json
from features import config
#from . import config
import importlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')




def before_all(context):

    # Configuración avanzada de logging
    context.logger = logging.getLogger('automatizacion')
    context.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    importlib.reload(config)
    # Handler para archivo (rotativo)
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    file_handler = RotatingFileHandler(
        f'{log_dir}/automation_{datetime.now().strftime("%Y%m%d")}.log',
        maxBytes=1_000_000,
        backupCount=3,
        encoding='utf-8' 
    )


    file_handler.setFormatter(formatter)
    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    context.logger.addHandler(file_handler)
    context.logger.addHandler(console_handler)
    context.logger.info("[TEST] 🚀 Inicializando configuración global...")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # Configuración automática del driver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    context.logger.info("[TEST] 🛠️ Navegador Chrome configurado + [NETWORK] logs de red activados")
  

def before_scenario(context, scenario):
    context.scenario_start_time = datetime.now()  # Registra inicio del escenario
    context.data = {
        "roles": load_json("roles.json"),
        "formularios": load_json("formularios.json"),
        "entornos": load_json("entornos.json")
    }

    context.logger.info(f"[TEST] 📌 Iniciando escenario: {scenario.name}")
 

    # Verifica si el usuario ya está logueado
    if hasattr(context, 'login_exitoso') and context.login_exitoso:
        context.logger.warning("[TEST] ⚠️ Sesión activa detectada - Omitiendo login")
        url_principal = context.data["entornos"]["develop"]["BASE_URL"]
        context.driver.get(url_principal)
    else:
       context.logger.debug("Nueva sesion requerida")

def after_step(context, step):
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"error_{step.name}",
            attachment_type=AttachmentType.PNG
        )

def after_scenario(context, scenario):
    # Cálculo de tiempo de ejecución
    elapsed = datetime.now() - context.scenario_start_time
    elapsed_seconds = round(elapsed.total_seconds(), 2)

     # Log y almacenamiento
    
    if elapsed_seconds > 5:  # Ajusta el valor según tu SLA
        context.logger.warning(f"[PERFORMANCE] ⏱️🚨 ALERTA: El escenario '{scenario.name}' tardó {elapsed_seconds}s (más de 5s)")
    else:
        context.logger.info(f"[PERFORMANCE] ⏱️ Escenario '{scenario.name}' tomó {elapsed_seconds}s")

    # Guardar en CSV (para análisis posterior)
    with open('performance_metrics.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([scenario.name, elapsed_seconds])

        # Integración con Allure
    allure.dynamic.label('execution_time', str(elapsed_seconds))
    allure.attach(
        f"Tiempo ejecución: {elapsed_seconds}s",
        name="performance_data",
        attachment_type=allure.attachment_type.TEXT
    )

    if scenario.status == "failed":
        error_dir = "logs/errors"
        os.makedirs(error_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"{error_dir}/FAIL_{scenario.name}_{timestamp}.png"
        context.driver.save_screenshot(screenshot_path)
        context.logger.error(f"[TEST] ❌ Fallo en escenario: {scenario.name}. Captura en {screenshot_path}")
   
   ##NETWORK
"""
    if hasattr(context, 'driver'):
        logs = context.driver.get_log('performance')
        network_entries = []

    for entry in logs:
        try:
            log_data = eval(entry['message'])['message']
            if 'Network.responseReceived' in log_data.get('method', ''):
                response = log_data['params']['response']
                url = response.get('url', '')
                timing = response.get('timing', {})
                
                # Filtrar recursos estáticos (opcional)
                if url and timing and url.startswith(('http', 'https')) and 'image' not in response.get('mimeType', ''):
                    latency = timing.get('receiveHeadersEnd', 0)
                    network_entries.append((url, latency))
                    
                    # Logear TODAS las latencias (no solo las >500ms)
                    context.logger.info(f"[NETWORK]  🌐 {url} - Latencia: {latency}ms")
                    
                    # Opcional: Destacar las lentas
                    if latency > 500:
                        context.logger.warning(f"[NETWORK-SLOW] 🌐🚨  {url} - Latencia alta: {latency}ms")
        except Exception as e:
            context.logger.debug(f"[NETWORK] ⚠️ Error procesando log: {str(e)}")
            continue
    
        
    if network_entries:
        summary = "\n".join([f"{url}: {latency}ms" for url, latency in network_entries])
        allure.attach(summary, name="network_performance", attachment_type=allure.attachment_type.TEXT)
"""

def before_feature(context, feature):
    context.test_data = load_json("formularios.json")
    

def after_all(context):
    # Cierra el navegador SOLO al final de todos los escenarios
    if hasattr(context, 'driver'):
        context.logger.info("[TEST] 🛑 Cerrando navegador...")
        context.driver.quit()
    context.logger.info("[TEST] 🏁 Ejecución finalizada\n" + "="*50)


"""Información general	print("[INFO] Mensaje")	context.logger.info("Mensaje")
Advertencias	print("[WARN] Alerta")	context.logger.warning("Alerta")
Errores	print("[ERROR] Fallo crítico")	context.logger.error("Fallo crítico")
Debug (detalles técnicos)	print("[DEBUG] Valor variable: x")	context.logger.debug("Valor variable: %s", x)"""
