from behave import *
from pages.archivos_page import ArchivosPage
from config import NUMERO_COMISIÓN
from pages.all_page import AllPage
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" alta de archivo')
def step_impl(context,estatus):


    context.all_page = AllPage(context.driver)
    context.archivosPage = ArchivosPage(context.driver)
    time.sleep(1)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)

  
@when('Seleccionar menu de archivos')
def step_impl(context):
    context.all_page = AllPage(context.driver)
    context.archivosPage.seleccionar_menu_archivos()

@when('Agregar archivos a la comisión')
def step_impl(context):
    data = context.data["formularios"]['ARCHIVOS']
    context.archivosPage.click_agregar_archivo(data)
    data = context.data["formularios"]['ARCHIVOS_']
    context.archivosPage.click_agregar_archivo(data)


@then('Validar registro en el grid archivos')
def step_impl(context):
  
    docto = context.data["formularios"]["ARCHIVOS"]["tipo_archivo"]
    record_data = {
            'column': 'Areolínea',
            'registro': docto,
            'num': False
        }

    assert context.archivosPage.validar_grid(record_data), \
                f"El registro Areolínea con el dato {docto} no apareció en el grid"
        
   