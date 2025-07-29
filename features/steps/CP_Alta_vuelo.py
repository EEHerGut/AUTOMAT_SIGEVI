from behave import *
from pages.vuelo_page import VuelosPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import VUELO,NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.all_page import AllPage
import time

origen=VUELO["origen"]
destino=VUELO["arrive"]
aerolinea=VUELO["aeroline"]


@given('Visualizar el grid de comisiones vuelo')
def step_impl(context):
    context.all_page = AllPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(ESTATUS_COMISIÓN)
  


@when('Seleccionar el menu de vuelos')
def step_impl(context):
    vuelo_page = VuelosPage(context.driver)
    vuelo_page.seleccionar_menu_vuelos()

@when('Dar clic en el botón Agregar vuelo y seleccionar tipo de vuelo')
def step_impl(context):
    vuelo_page = VuelosPage(context.driver)
    vuelo_page.click_agregar_vuelo()
    vuelo_page.seleccionar_tipo_vuelo(VUELO['trip'])

@when('Agregar datos de vuelo, seleccionar agregar y selecionar Aceptar - Aceptar')
def step_impl(context):
    vuelo_page = VuelosPage(context.driver)
    time.sleep(2)
    context.driver.refresh()
    context.driver.execute_script("document.body.style.zoom='80%'") 
    time.sleep(2)
    vuelo_page.click_agregar_vuelo()
    vuelo_page.seleccionar_tipo_vuelo(VUELO['trip'])
    time.sleep(2)
    vuelo_page.ingresar_datos_vuelo(origen,destino,aerolinea)
    vuelo_page.guardar_vuelo()
    vuelo_page.refresh_page()

@then('Validar registro en el grid vuelo')
def step_impl(context):
  
    validator =  AllPage(context.driver)
    datos = {
        "Areolínea": aerolinea
    }
    xpath="//app-add-flights//table[@role='grid' or contains(@class, 'table table-striped table-hover')]"
    
    if not validator.validar_registro_tabla(datos,xpath,10):
        raise AssertionError(f"No se encontró vuelo {aerolinea}-{aerolinea}")
 
    