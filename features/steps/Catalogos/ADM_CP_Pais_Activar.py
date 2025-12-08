import time
from behave import *
from pages.Catalogos.CAT_Pais_page import PaisPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos - "{estatus}" activar/desactivar país')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.pais_page = PaisPage(context.driver)
     time.sleep(1)
     context.all_page.menu_catalogo(estatus)
   
@when('Buscar el país para activar/desactivar')
def step_impl(context):     
   data = context.data["catalogos"]['PAIS']['nombre_pais']
   context.all_page.buscar_comision(data)
   time.sleep(3)
   context.pais_page.act_pais()

            
@Then('El país se activa/desactiva correctamente')
def step_impl(context):  
     time.sleep(3)
     data = context.data["catalogos"]['PAIS']['nombre_pais']
     context.all_page.buscar_comision(data)
     context.pais_page.validar_grid(data)
     time.sleep(2)
     assert True
