import time
from behave import *
from config import CIUDAD,NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.ciudad_page import CiudadPage
from pages.all_page import AllPage

"""@given('El usuario se encuentra en el grid de comisiones ciudad')
def step_impl(context):

      assert 10
"""
@given('La solicitud esta con estatus "{estatus}" ciudad y selecionar la comisión para agregar ciudad')
def step_impl(context,estatus):
     context.all_page = AllPage(context.driver)
     context.ciudad_page = CiudadPage(context.driver)
     time.sleep(1)
     context.all_page.menu_comision()
     time.sleep(3)
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(estatus)

@when('Seleccionar menu de ciudades')
def step_impl(context):
    
    context.ciudad_page.seleccionar_menu_ciudades()

@when('Dar clic en el boton Agregar municipio')
def step_impl(context):
    
    context.ciudad_page.click_agregar_ciudad()

@when('Agregar municipio')
def step_impl(context):     
   estado = CIUDAD['state']
   municipio = CIUDAD['town']

   time.sleep(3)
   context.all_page.refresh_page()
   time.sleep(3)
   context.driver.refresh()
   context.driver.execute_script("document.body.style.zoom='80%'") 
   context.ciudad_page = CiudadPage(context.driver)
   time.sleep(2)
   context.ciudad_page.click_agregar_ciudad()
   time.sleep(3)
   context.ciudad_page.seleccionar_estado(estado)
   context.ciudad_page \
        .seleccionar_municipio(municipio) \
        .guardar_ciudad() \

            
@Then('La ciudad se agrega correctamente')
def step_impl(context):  
     time.sleep(1)
     context.ciudad_page.verificar_creacion_exitosa()
     time.sleep(1)
     assert context.ciudad_page.cerrar_mensaje_exito()
