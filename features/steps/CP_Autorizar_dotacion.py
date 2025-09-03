import time
from behave import *
from pages.all_page import AllPage
from pages.autorizar_dotacion import AutorizarDotacionPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" autorizar dotación')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.autorizar_page = AutorizarDotacionPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de autorizar dotación')
def step_impl(context):
  
    context.autorizar_page.seleccionar_menu_autorizar()

@when('Autorizar la solicitud y aceptar autorizar dotación')
def step_impl(context):

    context.autorizar_page.confirmar_autorizar_sin()

@then('Validar el estatus de la comisión "{estatus}" autorizar dotación')
def step_impl(context,estatus):
    time.sleep(1)
    context.all_page.menu_comision()
    time.sleep(1)
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.autorizar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    
   
    

    