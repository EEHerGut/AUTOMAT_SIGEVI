import time
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import CIUDAD
from pages.ciudad_page import CiudadPage
from pages.comision_page import ComisionPage

@given('El usuario se encuentra en el grid de comisiones ciudad')
def step_impl(context):

      assert 10

@given('la solicitud esta con estatus "Solicitud de comisión en registro" ciudad y selecionar la comisión para agregar ciudad')
def step_impl(context):
    
    context.execute_steps('''
            Given Visualizar el grid de comisiones
            When Agregar numero de comisión
            Then Visualizar la comisión y dar clic en detalle
        ''')

@when('Seleccionar menu de ciudades')
def step_impl(context):
    
    context.ciudad_page = CiudadPage(context.driver)
    context.ciudad_page.seleccionar_menu_ciudades()

@when('Dar clic en el boton Agregar municipio')
def step_impl(context):
    context.ciudad_page = CiudadPage(context.driver)
    context.ciudad_page.click_agregar_ciudad()

@when('Agregar municipio')
def step_impl(context):     

   estado = CIUDAD['state']
   municipio = CIUDAD['town']
    
   context.ciudad_page = CiudadPage(context.driver)

 
   context.ciudad_page \
        .seleccionar_estado(estado) \
        .seleccionar_municipio(municipio) \
        .guardar_ciudad() \

            
@Then('La ciudad se agrega correctamente')
def step_impl(context):     
     time.sleep(2)
     context.ciudad_page.verificar_creacion_exitosa()
     time.sleep(3)
     assert context.ciudad_page.cerrar_mensaje_exito()
