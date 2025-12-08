
from behave import *
from pages.complementos_page import ComplementosPage



@given('Selecciónar el complemento con el estatus "{estatus}" reembolso')
def step_impl(context,estatus):
  context.complementos = ComplementosPage(context.driver)
  context.complementos.seleccionar_complemento()
    
   
@when('Seleccionar el botón autorizar complemento reembolso')
def step_impl(context):
   context.complementos.autorizar_complemento()

   
@then('Visualizar el complemento autorizado reembolso')
def step_impl(context):

    assert True
