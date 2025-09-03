import time
from behave import *
from pages.all_page import AllPage
from features.pages.depositar_page import DepositarPage
from config import NUMERO_COMISIÓN


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" depositar')
def step_impl(context,estatus):

    time.sleep(2)
    context.all_page = AllPage(context.driver)
    context.depositar_page = DepositarPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de depositar')
def step_impl(context):
  
    context.depositar_page.seleccionar_menu_depositar()

@when('Autorizar la dotación y aceptar')
def step_impl(context):

    context.depositar_page.click_confirmar_depósito()
    context.all_page.menu_comision()


@then('Validar el estatus de la comisión "{estatus}" autorizar solicitud depositar')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
            'num': NUMERO_COMISIÓN
        }

    assert context.depositar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
     


    