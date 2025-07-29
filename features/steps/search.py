from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import NUMERO_COMISIÓN, ESTATUS_COMISIÓN
import logging
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

@given('Visualizar el grid de comisiones')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='body']/main/app-root/app-commissions/div/div/h1"))
        )
        logging.info("Grid de comisiones visible correctamente")
    except TimeoutException:
        logging.error("No se pudo visualizar el grid de comisiones")
        raise

@when('Agregar numero de comisión')
def step_impl(context):
    try:
        search_field = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.ID, "table-filtering-search"))
        )
        search_field.clear()
        search_field.send_keys(NUMERO_COMISIÓN)
        logging.info(f"Búsqueda realizada para comisión: {NUMERO_COMISIÓN}")
    except Exception as e:
        logging.error(f"Error al buscar comisión: {str(e)}")
        raise

@then('Visualizar la comisión y dar clic en detalle')
def step_impl(context):
    try:
        comision = ESTATUS_COMISIÓN
        boton = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{comision}')]"))
        )
        
        texto_boton = boton.text
        if comision != texto_boton:
            raise AssertionError(f"❌ La comisión no está en estado esperado. Esperado: {comision}, Actual: {texto_boton}")
        
        try:
            boton.click()
            logging.info(f"Clic exitoso en botón con texto: {comision}")
        except ElementClickInterceptedException:
            context.driver.execute_script("arguments[0].click();", boton)
            logging.info(f"Clic realizado con JavaScript en botón: {comision}")
            
    except Exception as e:
        logging.error(f"Error al interactuar con la comisión: {str(e)}")
        raise