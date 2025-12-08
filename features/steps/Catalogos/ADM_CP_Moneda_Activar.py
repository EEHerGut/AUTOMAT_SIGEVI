import time
from behave import *
from pages.Catalogos.CAT_Moneda_page import MonedaPage
from pages.all_page import AllPage

@given('Seleccionar el menu Configuración - Catálogos - "{estatus}" ACTIVAR/DESACTIVAR moneda')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.monedaPage = MonedaPage(context.driver)
     time.sleep(1)
     if not context.estadoPage.validar_vista():
        context.all_page.menu_catalogo(estatus) 
        
@when('Buscar la moneda para activar/desactivar')
def step_impl(context):     
   data = context.data["catalogos"]['MONEDA']['nombre_moneda_m']
   context.all_page.buscar_comision(data)
   time.sleep(3)
   context.monedaPage.act_moneda()

            
@Then('La moneda se activa/desactiva correctamente')
def step_impl(context):  
     time.sleep(3)
     data = context.data["catalogos"]['MONEDA']['nombre_moneda_m']
     context.all_page.buscar_comision(data)
     context.monedaPage.validar_grid(data)
     time.sleep(2)
     assert True
