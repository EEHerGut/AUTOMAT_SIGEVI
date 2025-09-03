from behave import *
from pages.vuelo_page import VuelosPage
from config import NUMERO_COMISIÓN
from pages.all_page import AllPage
import time



@given('Visualizar el grid de comisiones vuelo con estatus "{estatus}"')
def step_impl(context,estatus):


    context.all_page = AllPage(context.driver)
    context.vuelo_page = VuelosPage(context.driver)
    time.sleep(1)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)

  
@when('Seleccionar el menu de vuelos')
def step_impl(context):
    context.all_page = AllPage(context.driver)
    context.vuelo_page.seleccionar_menu_vuelos()

@when('Dar clic en el botón Agregar vuelo y seleccionar tipo de vuelo')
def step_impl(context):
    data = context.data["formularios"]['VUELO']
    context.vuelo_page.click_agregar_vuelo()
    context.vuelo_page.seleccionar_tipo_vuelo(data)

@when('Agregar datos de vuelo, seleccionar agregar y selecionar Aceptar - Aceptar')
def step_impl(context):
    data = context.data["formularios"]['VUELO']
    time.sleep(1)
    context.all_page.refresh_page()
    context.vuelo_page.click_agregar_vuelo()
    context.vuelo_page.seleccionar_tipo_vuelo(data)
    time.sleep(2)
    context.vuelo_page.ingresar_datos_vuelo(data)
    context.vuelo_page.guardar_vuelo()
    context.all_page.refresh_page()
    time.sleep(2)

@then('Validar registro en el grid vuelo')
def step_impl(context):
  
    aerolinea = context.data["formularios"]["VUELO"]["aeroline"]
    record_data = {
            'column': 'Areolínea',
            'registro': aerolinea,
            'num': False
        }

    assert context.vuelo_page.validar_grid(record_data), \
                f"El registro Areolínea con el dato {aerolinea} no apareció en el grid"
        
   
 
    