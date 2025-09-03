import time
from behave import *
from pages.all_page import AllPage
from pages.autorizar_comprobacion import AutorizarComprobacionPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" autorizar comproabación')
def step_impl(context,estatus):

    time.sleep(2)
    context.all_page = AllPage(context.driver)
    context.autorizar_page = AutorizarComprobacionPage(context.driver)
    context.all_page.refresh_page()
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de autorizar comprobación')
def step_impl(context):
  
    context.autorizar_page.seleccionar_menu_autorizar()

@when('Autorizar la solicitud y aceptar autorizar comprobación')
def step_impl(context):

    context.autorizar_page.confirmar_autorizar()

@then('Validar el estatus de la comisión "{estatus}" autorizar comprobación')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.autorizar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
     


    