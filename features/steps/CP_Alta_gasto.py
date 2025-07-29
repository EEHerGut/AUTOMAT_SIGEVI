from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import GASTO,NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.gasto_page import GastosPage
from pages.all_page import AllPage

@given('Visualizar el grid de comisiones gasto')
def step_impl(context):
     context.all_page = AllPage(context.driver)
     context.all_page.menu_comision()
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(ESTATUS_COMISIÓN)

@When('Seleccionar el menu de gasto')
def step_impl(context):
   
    gasto_page = GastosPage(context.driver)
    gasto_page.seleccionar_menu_gastos()



@When('Dar clic en el botón Agregar gasto, seleccionar tipo de gasto, monto y dar clic en agregar')
def step_impl(context):
    gasto_page = GastosPage(context.driver)
    gasto_page.click_agregar_gasto()

    gasto_page.seleccionar_tipo_gasto(GASTO['concept'])    
    gasto_page.agregar_monto(GASTO['amount'])
    gasto_page.guardar_gasto()

   
    context.driver.refresh() 
    context.driver.execute_script("document.body.style.zoom='80%'")
    
    assert context.failed is False

@Then('Validar registro en el grid de gasto')
def step_impl(context):
    context.execute_steps('''
			  Given Al terminar la prueba
              When Dar clic en el botón de cerrar sesión
              Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')