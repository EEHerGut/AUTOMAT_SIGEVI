from behave import *
from pages.enviar_comprobacion import EnviarcomprobacionPage
from config import NUMERO_COMISIÓN
from pages.all_page import AllPage
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" envío comprobación')
def step_impl(context,estatus):
        
    context.all_page = AllPage(context.driver)
    context.enviar = EnviarcomprobacionPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)

@When('Seleccionar menu de Envío a comprobación')
def step_impl(context):
        
    context.enviar.seleccionar_menu()

@when('Enviar la comisión y aceptar')
def step_impl(context):

    context.enviar.confirmar_envio()

@then('Validar el estatus de la comisión "{estatus}"')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.enviar.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
  
