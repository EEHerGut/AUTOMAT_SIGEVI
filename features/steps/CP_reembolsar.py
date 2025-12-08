import time
from behave import *
from pages.all_page import AllPage
from features.pages.reembolso_page import ReembolsoPage
from config import NUMERO_COMISIÓN


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" solicitar reembolso')

def step_impl(context,estatus):

    time.sleep(2)
    context.all_page = AllPage(context.driver)
    context.rembolso = ReembolsoPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de Solicitar reembolso')
def step_impl(context):
  
    context.rembolso.seleccionar_menu_reembolso()

@when('Autorizar la solicitud y aceptar el reembolso')
def step_impl(context):

    context.rembolso.confirmar_autorizar()

@then(' Validar el estatus de la comisión "{estatus}" rembolso')
def step_impl(context, estatus):

    time.sleep(1)
    record_data=context.all_page.registro_txt(NUMERO_COMISIÓN,estatus)
    assert context.rembolso.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
   


