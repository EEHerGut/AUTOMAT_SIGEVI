import pickle
from venv import logger
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

@given('Hemos abierto la página inicial del sistema login')
def step_impl(context):
        # Inicializa la página de login si no existe
        if not hasattr(context, 'login_page'):
            context.login_page = LoginPage(context.driver)
    
    # Si ya está logueado, no hagas nada
        if hasattr(context, 'login_exitoso') and context.login_exitoso:
            return
    
    # Resto del código de login...
        context.login_page.navigate_to_login_page()
        context.logged_in = True
        context.login_exitoso = True  # Marca como logueado

@when('Capturas el usuario "{usuario}" , contraseña "{password}"')
def step_impl(context,usuario,password):
    time.sleep(2)
    #Autorizador_SIGEVI
    #OPERADOR_SIGEVI
    context.login_page.enter_credentials(usuario, password)
    
@when('Seleccionar iniciar sesión')
def step_impl(context):
   context.login_page.click_login_button()

@when('Seleccionar el rol "{rol}" y dar clic en continuar')
def step_impl(context,rol):
    context.login_page.select_role(rol)
    context.login_page.click_confirm_button()

@Then('El sistema nos permite visualizar el panel principal')
def step_impl(context):
    try:
        # Verificar que estamos en el panel principal
        WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//app-navbar//img[@alt='Inicio' or contains(@src, 'assets/images/notifications24.png') or @aria-label='Logo principal']")))
        
        # Guardar cookies solo si el contexto tiene la ruta configurada
        if hasattr(context, 'cookies_path'):
            with open(context.cookies_path, 'wb') as f:
                pickle.dump(context.driver.get_cookies(), f)
        else:
            logger.warning("No se pudo guardar cookies - ruta no configurada")
    except Exception as e:
        logger.error(f"Error al verificar panel principal: {str(e)}")
        raise