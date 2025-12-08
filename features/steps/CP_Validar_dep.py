from behave import *
from pages.all_page import AllPage
from pages.archivos_page import ArchivosPage
from pages.validar_dotacion_page import ValidardotacionPage
from config import NUMERO_COMISIÓN
import time

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" validar deposito')

def step_impl(context,estatus):
 
    context.all_page = AllPage(context.driver)
    context.archivosPage = ArchivosPage(context.driver)
    context.dotacion = ValidardotacionPage(context.driver)
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
    ###context.archivosPage.seleccionar_menu_archivos()
    
@when('Cargar comprobante y enviar a validar deposito')
def step_impl(context):
    time.sleep(1)
    context.archivosPage.seleccionar_menu_archivos()
    data = context.data["formularios"]['ARCHIVOS_COMPROBANTE']
    context.archivosPage.click_archivo_dep(data)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision("Comprobación autorizada a cargo del comisionado")
    context.dotacion.seleccionar_menu_validardep()
  

@Then('Validar el estatus de la comisión "{estatus}" validar depósito')
def step_impl(context,estatus):
    
    time.sleep(1)
    record_data=context.all_page.registro_txt(NUMERO_COMISIÓN,estatus)

    assert context.comision_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 

    
    ##context.comision_page.verificar_creacion_exitosa()
    
  