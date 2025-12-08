import time
from behave import *
from pages.Catalogos.CAT_Aerolinea_page import AerolineaPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos - "{estatus}" EDITAR AEROLINEA')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.aerolinea_page = AerolineaPage(context.driver)
     
  # validar_vista() YA retorna True/False - solo úsalo
     if not context.aerolinea_page.validar_vista():
        context.all_page.menu_catalogo(estatus) 
     time.sleep(3)
@when('Buscar la aerolinea y editar')
def step_impl(context):     
  
   data = context.data["catalogos"]['AEROLINEA']['nombre_aerolinea']
   context.all_page.buscar_comision(data)
   time.sleep(3)
   context.aerolinea_page.editar_aerolinea(data)

            
@Then('La aerolinea se edita correctamente')
def step_impl(context):  
     time.sleep(4)
     data = context.data["catalogos"]['AEROLINEA']['nombre_aerolinea'] + " - EDITADO"
     context.all_page.buscar_comision(data)
     context.aerolinea_page.validar_grid(data)
     time.sleep(2)
     assert True
