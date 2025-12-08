
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

@given('Al terminar la prueba')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context)
 
@when('Dar clic en el boton de cerrar sesion')
def step_impl(context):
    
    time.sleep(1)
    context.login_page.cerrar_sesion()
    
@then('Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial')
def step_impl(context):
    context.logger.info(f"[TEST]  Cerrando sesión")
    time.sleep(3)
 
 
