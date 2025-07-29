# environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pickle


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Configuración automática del driver
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
def before_scenario(context, scenario):
    # Verifica si el usuario ya está logueado
    if hasattr(context, 'login_exitoso') and context.login_exitoso:
        print("\n[INFO] Sesión ya activa, omitiendo login...")
    else:
        print("\n[INFO] Iniciando nuevo escenario...")

def after_scenario(context, scenario):
    # Guarda cookies para persistencia (excepto en el último escenario)
  """  if scenario.name != "Dar de alta ciudad":  # No guardar en el último escenario
        cookies_path = "features/cookies.pkl"
        with open(cookies_path, 'wb') as cookies_file:
            pickle.dump(context.driver.get_cookies(), cookies_file)
"""
def after_all(context):
    # Cierra el navegador SOLO al final de todos los escenarios
    if hasattr(context, 'driver'):
        context.driver.quit()
        print("\n[INFO] Navegador cerrado (fin de la ejecución).")