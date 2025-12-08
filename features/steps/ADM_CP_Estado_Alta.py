import time
from behave import *
from features.pages.Catalogos.CAT_Estado_page import EstadoPage
from pages.all_page import AllPage


@given('Seleccionar el menu Configuracion - Catalogos -  "{menu}" ALTA ESTADO')
def step_impl(context,menu):
     context.all_page = AllPage(context.driver)
     context.estadoPage = EstadoPage(context.driver)
     time.sleep(1)
     if not context.estadoPage.validar_vista():
        context.all_page.menu_catalogo(menu) 
   

@when('Agregar estado')
def step_impl(context):     
   
   data = context.data["catalogos"]['ESTADO']["nombre_estado"]
   context.estadoPage.click_agregar_estado(data)

            
@then('El estado se agrega correctamente')
def step_impl(context):  
       
       data = context.data["catalogos"]['ESTADO']['nombre_estado']
       context.all_page.buscar_comision(data)
       context.estado_page.validar_grid(data)
       time.sleep(2)
       assert True
