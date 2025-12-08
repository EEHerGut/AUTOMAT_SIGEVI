import time
from behave import *
from features.pages.Catalogos.CAT_Estado_page import EstadoPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuracion - Catalogos - "Estado-municipio/ciudad (NAL)" EDITAR ESTADO')
def step_impl(context):
     context.all_page = AllPage(context.driver)
     context.estado_page = EstadoPage(context.driver)
     time.sleep(2)
     if not context.estado_page.validar_vista():
        context.all_page.menu_catalogo("Estado-municipio/ciudad (NAL)") 


@when('Buscar el estado y editar')
def step_impl(context):     
   
  
   data = context.data["catalogos"]['ESTADO']['nombre_estado']
   context.all_page.buscar_comision(data)
   time.sleep(3)
   data = context.data["catalogos"]['ESTADO']['nombre_estado_m']
   context.estado_page.editar_estado(data)

            

            
@then('El estado se edita correctamente')
def step_impl(context):  
       
       data = context.data["catalogos"]['ESTADO']['nombre_estado']
       context.all_page.buscar_comision(data)
       context.estado_page.validar_grid(data)
       time.sleep(2)
       assert True
