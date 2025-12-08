import time
from behave import *
from pages.Catalogos.CAT_Pais_page import PaisPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos - "{estatus}" EDITAR PAÍS')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.pais_page = PaisPage(context.driver)
     
     context.all_page.menu_catalogo(estatus)
     time.sleep(5)
@when('Buscar el país y editar')
def step_impl(context):     
  
   data = context.data["catalogos"]['PAIS']['nombre_pais']
   context.all_page.buscar_comision(data)
   time.sleep(3)
   data = context.data["catalogos"]['PAIS']['nombre_pais_m']
   context.pais_page.editar_pais(data)

            
@Then('El país se edita correctamente')
def step_impl(context):  
     time.sleep(2)
     data = context.data["catalogos"]['PAIS']['nombre_pais_m']
     context.all_page.buscar_comision(data)
     context.pais_page.validar_grid(data)
     assert True
