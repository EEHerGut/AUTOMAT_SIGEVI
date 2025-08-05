import time
from behave import *
from config import CIUDAD,NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.ciudad_page import CiudadPage
from pages.all_page import AllPage

@given('El usuario se encuentra en el grid de comisiones ciudad')
def step_impl(context):

      assert 10

@given('la solicitud esta con estatus "Solicitud de comisión en registro" ciudad y selecionar la comisión para agregar ciudad')
def step_impl(context):
     context.ciudad_page = CiudadPage(context.driver)
     context.all_page = AllPage(context.driver)
     context.all_page.menu_comision()
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(ESTATUS_COMISIÓN)

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
   context.ciudad_page.click_agregar_ciudad()
   time.sleep(3)
   context.ciudad_page.seleccionar_estado(estado)
   context.ciudad_page \
        .seleccionar_municipio(municipio) \
        .guardar_ciudad() \

            
@Then('La ciudad se agrega correctamente')
def step_impl(context):  
     time.sleep(2)
     context.ciudad_page.verificar_creacion_exitosa()
     time.sleep(3)
     assert context.ciudad_page.cerrar_mensaje_exito()
