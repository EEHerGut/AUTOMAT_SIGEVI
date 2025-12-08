import time
from behave import *
from pages.Catalogos.CAT_Aerolinea_page import AerolineaPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos - "{estatus}"')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.aerolinea_page = AerolineaPage(context.driver)
     time.sleep(1)
     
   # validar_vista() YA retorna True/False - solo úsalo
     if not context.aerolinea_page.validar_vista():
        context.all_page.menu_catalogo(estatus) 
   

@when('Agregar aerolinea')
def step_impl(context):     
   data = context.data["catalogos"]['AEROLINEA']["nombre_aerolinea"]
   context.aerolinea_page.click_agregar_aerolinea(data)

            
@Then('La Aerolinea se agrega correctamente')
def step_impl(context):  
       
       data = context.data["catalogos"]['AEROLINEA']['nombre_aerolinea']
       context.all_page.buscar_comision(data)
       context.aerolinea_page.validar_grid(data)
       time.sleep(2)
       assert True
