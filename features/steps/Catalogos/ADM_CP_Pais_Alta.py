import time
from behave import *
from pages.Catalogos.CAT_Pais_page import PaisPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos -  "{estatus}" país')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.paisPage = PaisPage(context.driver)
     time.sleep(1)
     context.all_page.menu_catalogo(estatus)
   

@when('Agregar país')
def step_impl(context):     
   
   context.paisPage.click_agregar_pais()
   data = context.data["catalogos"]['PAIS']
   context.paisPage.guardar_pais(data)

            
@Then('El país se agrega correctamente')
def step_impl(context):  
       
       data = context.data["catalogos"]['PAIS']['nombre_pais']
       context.all_page.buscar_comision(data)
       context.paisPage.validar_grid(data)
       time.sleep(2)
       assert True
