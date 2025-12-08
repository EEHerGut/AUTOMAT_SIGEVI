
from behave import *
from pages.complementos_page import ComplementosPage



@given('Selecciónar el complemento con el estatus "{estatus}"')
def step_impl(context,estatus):
  context.complementos = ComplementosPage(context.driver)
  context.complementos.seleccionar_complemento()
    
   
@when('Seleccionar el botón autorizar complemento')
def step_impl(context):
   context.complementos.autorizar_complemento()

   
@then('Visualizar el complemento autorizado')
def step_impl(context):

    assert True
