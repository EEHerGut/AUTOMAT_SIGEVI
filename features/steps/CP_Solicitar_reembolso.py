import time
from behave import *
from pages.all_page import AllPage
from features.pages.reembolsar_page import ReembolsarPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" reembolso')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.reembolsar = ReembolsarPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de reembolso')
def step_impl(context):
  
    context.reembolsar.seleccionar_menu_reembolsar()

@when('Rembolsar la comisión y aceptar')
def step_impl(context):

    context.reembolsar.confirmar_autorizar()

@then('Validar el estatus de la comisión "{estatus}" reembolsar comisión')
def step_impl(context,estatus):
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.reembolsar.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    
   
    
