import time
from behave import *
from features.pages.Catalogos.CAT_Estado_page import EstadoPage
from pages.all_page import AllPage

@given('Seleccionar el menu Configuracion - Catalogos - "{menu}" ACTIVAR/DESACTIVAR ESTADO')
def step_impl(context,menu):
     context.all_page = AllPage(context.driver)
     context.estado_page = EstadoPage(context.driver)
     time.sleep(1)
       # validar_vista() YA retorna True/False - solo úsalo
     if not context.estado_page.validar_vista():
        context.all_page.menu_catalogo(menu) 
   
@when('Buscar el estado para activar/desactivar')
def step_impl(context):     
   data = context.data["catalogos"]['ESTADO']['nombre_estado']
   context.all_page.buscar_comision(data)
   time.sleep(2)
   context.estado_page.act_estado()

            
@then('El estado se activa/desactiva correctamente')
def step_impl(context):  
     time.sleep(3)
     data = context.data["catalogos"]['ESTADO']['nombre_estado']
     context.all_page.buscar_comision(data)
     context.estado_page.validar_grid(data)
     time.sleep(2)
     assert True
