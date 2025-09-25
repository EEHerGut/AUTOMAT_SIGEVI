import time
from behave import *
from pages.all_page import AllPage
from features.pages.revertir_cancelar_dotacion import Revertir_CancelarDotacionPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" revertir dotación')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.revertir_page = Revertir_CancelarDotacionPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de revertir dotación')
def step_impl(context):
  
    context.revertir_page.seleccionar_menu_revertir()

@when('Revertir dotación de la comisión y aceptar')
def step_impl(context):

    context.revertir_page.confirmar_reversión()

@then('Validar el estatus de la comisión "{estatus}" revertir dotación de la comisión')
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

    assert context.revertir_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    
   
    

    