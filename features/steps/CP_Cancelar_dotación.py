import time
from behave import *
from pages.all_page import AllPage
from features.pages.revertir_cancelar_dotacion import Revertir_CancelarDotacionPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" cancelar dotación')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.cancelar_page = Revertir_CancelarDotacionPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de cancelar dotación')
def step_impl(context):
  
    context.cancelar_page.seleccionar_menu_cancelar()

@when('Cancelar la dotación y aceptar')
def step_impl(context):

    context.cancelar_page.confirmar_cancelación()
    context.all_page.menu_comision()
 

@then('Validar el estatus de la comisión "{estatus}" cancelar dotación')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.cancelar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    


    