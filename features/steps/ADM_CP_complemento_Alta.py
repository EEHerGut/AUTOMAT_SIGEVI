
from behave import *
from pages.complementos_page import ComplementosPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" complemento')

def step_impl(context,estatus):
    context.all_page = AllPage(context.driver)
    context.complementos = ComplementosPage(context.driver)
    time.sleep(1)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
   
@given('Seleccionar menu de Complementos')
def step_impl(context):

    context.complementos.seleccionar_menu_complementos()
   
@when('Seleccionar el botón de alta de complemento')
def step_impl(context):

    context.complementos.alta_complemento()
   
@when('Agregar información del formulario, junto con el impuesto')
def step_impl(context):
  
    data = context.data["formularios"]['COMPLEMENTOS'] 
    data1 = context.data["formularios"]['IMPUESTOS_COMPLEMENTO'] 
    paths = context.data["formularios"]['PATHS']
    context.complementos.agregar_formulario(data,data1,paths)

@then('Visualizar el complemento')
def step_impl(context):

    assert True
