from behave import *
from pages.comision_page import ComisionPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN
import time

@given('Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud')

def step_impl(context):
 
    context.comision_page = ComisionPage(context.driver)
    context.all_page = AllPage(context.driver)
    context.all_page.refresh_page()
    context.all_page.menu_comision()
    context.comision_page.click_nueva_solicitud()  

@given('Deberíamos ver el formulario de solicitud de comisión')
def step_impl(context):
    context.comision_page.verificar_formulario_visible()

@given('Completamos los campos obligatorios')
def step_impl(context):
  
    data = context.data["formularios"]['SIN_ANTICIPO']
    context.comision_page.completar_campos_obligatorios(data)
    
@when('Guardamos la solicitud')
def step_impl(context):
    context.comision_page.guardar_solicitud()

@then('La solicitud se crea exitosamente')
def step_impl(context):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    tipo_comision=context.all_page.validar_tipo_comisión()
    tipo_anticipo=context.all_page.validar_anticipo()
    record_data = {
            'column': 'Estado ',
            'registro': 'Solicitud de comisión en registro',
            'num': NUMERO_COMISIÓN,
            'nac/inter': tipo_comision,
            'anticipo': tipo_anticipo
        }


    assert context.comision_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 

    
    ##context.comision_page.verificar_creacion_exitosa()
    
  