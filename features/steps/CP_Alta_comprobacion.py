from behave import *
from pages.comprobacion_page import ComprobacionPage
from features.pages.enviar_comprobacion_page import EnviarcomprobacionPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" comprobación')
def step_impl(context,estatus):
        
        context.comprobacion = ComprobacionPage(context.driver)
        context.enviar = EnviarcomprobacionPage(context.driver)
        context.all_page = AllPage(context.driver)
        context.all_page.menu_comision()
        time.sleep(4)
        context.all_page.buscar_comision(NUMERO_COMISIÓN)
        context.all_page.seleccionar_comision(estatus)

@given('Seleccionar menu de autorizar Consultar/Modificar comprobación')
def step_impl(context):
        context.comprobacion.clic_consultar()

@When('Agregar comprobación con gasto con comprobante y agregar impuesto, pasar al estatus "{estatus}"')
def step_impl(context,estatus):
        data = context.data["formularios"]['COMPROBACION']
        context.comprobacion = ComprobacionPage(context.driver)
        context.comprobacion.clic_comprobar()
        context.comprobacion.clic_select()
        PATH_PDF = r"C:/Users/Lenovo/Downloads/Recibo.pdf"
        PATH_XML = r"C:/Users/Lenovo/Downloads/Recibo.xml"
        context.comprobacion.cargar_archivos(PATH_PDF,PATH_XML)
        context.comprobacion.cargar_formulario_comprobación(data)

        time.sleep(2)
        context.all_page.menu_comision()
        context.all_page.buscar_comision(NUMERO_COMISIÓN)
        context.all_page.seleccionar_comision(estatus)
        time.sleep(1)
        context.enviar.seleccionar_menu()
        time.sleep(1)
        context.enviar.confirmar_envio()

@then('Validar el estatus de la comisión "{estatus}" comprobación')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data=context.all_page.registro_txt(NUMERO_COMISIÓN,estatus)
    assert context.depositar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
     
