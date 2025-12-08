import time
from behave import *
from pages.Catalogos.CAT_Moneda_page import MonedaPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuración - Catálogos -  "{estatus}" ALTA moneda')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.monedaPage = MonedaPage(context.driver)
     time.sleep(1)
     if not context.estadoPage.validar_vista():
        context.all_page.menu_catalogo(estatus) 
   

@when('Agregar Moneda')
def step_impl(context):     
   
   context.monedaPage.click_agregar_moneda()
   data = context.data["catalogos"]['MONEDA']
   context.monedaPage.guardar_moneda(data)

            
@Then('La Moneda se agrega correctamente')
def step_impl(context):  
       
       data = context.data["catalogos"]['MONEDA']['nombre_moneda']
       context.all_page.buscar_comision(data)
       context.monedaPage.validar_grid(data)
       time.sleep(1)
       assert True
