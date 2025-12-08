from behave import *
from config import NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.all_page import AllPage
from pages.enviar_sol_page import EnvioPage
import time

@given('Visualizar el grid de comisiones enviar al área de pagos con estatus "{estatus}"')
def step_impl(context,estatus):
     

     context.all_page = AllPage(context.driver)
     context.envio_page = EnvioPage(context.driver)
     context.all_page.menu_comision()
     time.sleep(2)
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar el menu de envio a autorización')
def step_impl(context):
    
    context.envio_page.seleccionar_menu_envio()

@when('Confirmar el envío')
def step_impl(context):
  
    context.envio_page.confirmar_envío()

@then('Validar que la solicitud cuente con el estatus "{estatus}"')
def step_impl(context,estatus):

    record_data=context.all_page.registro_txt(NUMERO_COMISIÓN,estatus)

    assert context.envio_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"

 
    