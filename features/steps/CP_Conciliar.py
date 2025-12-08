import time
from behave import *
from pages.all_page import AllPage
from features.pages.conciliar_page import ConciliarPage
from config import NUMERO_COMISIÓN


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" conciliar comproabación')

def step_impl(context,estatus):

    time.sleep(2)
    context.all_page = AllPage(context.driver)
    context.conciliar = ConciliarPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de Conciliar comisión')
def step_impl(context):
  
    context.conciliar.seleccionar_menu_conciliar()

@when('La comisión se concilia correctamente')
def step_impl(context):

    context.conciliar.click_confirmar_conciliar()
    context.all_page.menu_comision()

