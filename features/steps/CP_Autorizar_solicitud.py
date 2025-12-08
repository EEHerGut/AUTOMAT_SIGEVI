import time
from behave import *
from pages.all_page import AllPage
from features.pages.Aut_Rec_Can_page import Autorizar_Rechazar_CancelarPage
from pages.autorizar_dotacion import AutorizarDotacionPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}"')
def step_impl(context,estatus):

    context.all_page = AllPage(context.driver)
    context.autorizar_page = Autorizar_Rechazar_CancelarPage(context.driver)
    context.dotación = AutorizarDotacionPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de autorizar')
def step_impl(context):
  
    context.autorizar_page.seleccionar_menu_autorizar()

@when('Autorizar la solicitud y aceptar "{estatus}"')
def step_impl(context,estatus):

    context.autorizar_page.confirmar_autorizar()
    time.sleep(2)
    context.all_page.seleccionar_comision(estatus)
    time.sleep(1)
    context.dotación.seleccionar_menu_autorizar()
    time.sleep(1)
    context.dotación.confirmar_autorizar_con()
    time.sleep(1)

@then('Validar el estatus de la comisión "{estatus}" autorizar solicitud')
def step_impl(context,estatus):
    record_data=context.all_page.registro_txt(NUMERO_COMISIÓN,estatus)

    assert context.autorizar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    


    