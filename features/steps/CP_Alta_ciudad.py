import time
from behave import *
from config import NUMERO_COMISIÓN
from pages.ciudad_page import CiudadPage
from pages.all_page import AllPage


@given('La solicitud esta con estatus "{estatus}", selecionar la comisión para agregar ciudad')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.ciudad_page = CiudadPage(context.driver)
     time.sleep(1)
     context.all_page.menu_comision()
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(estatus)
     context.ciudad_page.seleccionar_menu_ciudades()

@when('Agregar municipio y/o ciudad')
def step_impl(context):     
   data = context.data["formularios"]['CIUDAD']
   time.sleep(1)
   context.all_page.refresh_page()
   context.ciudad_page = CiudadPage(context.driver)
   context.ciudad_page.click_agregar_ciudad()
   time.sleep(3)
   context.tipo=context.ciudad_page.guardar_ciudad(data)
   
            
@Then('La ciudad se agrega correctamente')
def step_impl(context):  
     context.ciudad_page.verificar_creacion_exitosa(context.tipo)
     context.ciudad_page.cerrar_mensaje_exito()

     assert True