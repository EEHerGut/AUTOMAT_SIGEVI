from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('visualizar la pagina principal')
def step_impl(context):
        textos_esperados = [
            "Inicio"
        ]
        elemento = WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='body']/main/app-root/app-home/app-navbar/app-breadcrumb/div/ol/li[2]")
            )
        )
        texto_actual = elemento.text.strip()
        ##print(f"Texto encontrado: {texto_actual}") 

        if any(texto in texto_actual for texto in textos_esperados):
            context.login_exitoso = True

@when('Seleccionar el menu comision y despues comisiones')
def step_impl(context):
    menu_comision = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Comisión')]"))
    )
    menu_comision.click()
    
    submenu_comisiones = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Comisiones')]"))
    )
    submenu_comisiones.click()

@then('Visualizar el detalle de comisiones')
def step_impl(context):
    WebDriverWait(context.driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='body']/main/app-root/app-commissions/div/div/h1"))
    )