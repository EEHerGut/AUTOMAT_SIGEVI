
from behave import *
from pages.complementos_page import ComplementosPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" complemento baja')

def step_impl(context,estatus):
    context.all_page = AllPage(context.driver)
    context.complementos = ComplementosPage(context.driver)
    time.sleep(1)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
   
@given('Seleccionar menu de Complementos baja')
def step_impl(context):

    context.complementos.seleccionar_menu_complementos()
   
@when('Seleccionar el botón de baja de complemento')
def step_impl(context):

    context.complementos.baja_complemento()

@then('No visualizar el complemento')
def step_impl(context):
        
     assert True 