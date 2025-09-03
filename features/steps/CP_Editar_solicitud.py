import time
from behave import *
from pages.comision_page import ComisionPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" editar solicitud')
def step_impl(context,estatus):
   
    context.comision_page = ComisionPage(context.driver)
    context.all_page = AllPage(context.driver)
    
    context.all_page.refresh_page()
    time.sleep(1)
    context.all_page.menu_comision()
    time.sleep(1)
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)

    
@when('Seleccionar menu de solicitud y editar la solicitud y guardar la solicitud')
def step_impl(context):

        context.comision_page.seleccionar_menu_solicitud()
        data = context.data["formularios"]['SOLICITUD_ANTICIPO']
        context.comision_page.editar_solicitud(data)
      
@Then('Validar que la solicitud cuente con el estatus "{estatus}" editar solicitud')
def step_impl(context,estatus):
        context.all_page.buscar_comision(NUMERO_COMISIÓN)
        data = context.data["formularios"]['SOLICITUD_ANTICIPO']['anticipo']
        anticipo=context.all_page.anticipo(data)

        time.sleep(0.5)
        record_data = {
                'column': 'Estado ',
                'registro': estatus,
                'num': NUMERO_COMISIÓN
                }

        assert context.comision_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"

 