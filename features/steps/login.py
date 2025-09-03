import pickle
from venv import logger
from behave import *
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.data_loader import load_json


@given('Inicio sesión como "{rol}"')
def step_impl(context,rol):
        # Inicializa la página de login si no existe
       
        if not hasattr(context, 'login_page'):
            context.login_page = LoginPage(context.driver,context)
    
    # Si ya está logueado, no hagas nada
        if hasattr(context, 'login_exitoso') and context.login_exitoso:
            return
    
    # Resto del código de login...
        data = load_json("roles.json")[rol]
        context.login_page.navigate_to_login_page()
        context.logged_in = True
        context.login_exitoso = True  # Marca como logueado
        context.login_page.enter_credentials(data)

@Then('El sistema nos permite visualizar el panel principal')
def step_impl(context):
    try:
        panel_principal = (By.XPATH, "//app-navbar//*[self::img[@alt='Inicio'] or self::img[contains(@src, 'notifications24')] or self::img[@aria-label='Logo principal']]")
        context.login_page.wait_for_element(panel_principal, timeout=20)

        # Guardar cookies solo si el contexto tiene la ruta configurada
        if hasattr(context, 'cookies_path'):
            with open(context.cookies_path, 'wb') as f:
                pickle.dump(context.driver.get_cookies(), f)
        else:
            logger.warning("No se pudo guardar cookies - ruta no configurada")
    except Exception as e:
        logger.error(f"Error al verificar panel principal: {str(e)}")
        raise