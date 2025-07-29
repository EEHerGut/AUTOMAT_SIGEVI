
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



@given('Al terminar la prueba')
def step_impl(context):
    
    
    context.driver.execute_script("document.body.style.zoom='80%'")

    time.sleep(3)
    pass 

@when('Dar clic en el botón de cerrar sesión')
def step_impl(context):
    
    cerrar_sesion = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//li[contains(@class, "nav-item")]//img[contains(@src, "box-arrow-right")]/parent::a'))
    )
    cerrar_sesion.click()

@then('Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial')
def step_impl(context):

    cerrar_sesion = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//app-modal//button[contains(@class, "btn-primary") or contains(text(), "C")][2]'))
    )
    cerrar_sesion.click()
    time.sleep(3)
