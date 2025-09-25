import time
from behave import *
from pages.all_page import AllPage
from features.pages.Aut_Rec_Can_page import Autorizar_Rechazar_CancelarPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" cancelar solicitud')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.autorizar_page = Autorizar_Rechazar_CancelarPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de cancelar solicitud')
def step_impl(context):
  
    context.autorizar_page.seleccionar_menu_cancelar()

@when('Cancelar la solicitud y aceptar')
def step_impl(context):

    context.autorizar_page.confirmar_cancelación()
    context.all_page.menu_comision()
 

@then('Validar el estatus de la comisión "{estatus}" cancelar solicitud')
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
 
    


    