from behave import *
from pages.comprobacion_page import ComprobacionPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN
import time


@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" comprobación')
def step_impl(context,estatus):
        
        context.comprobacion = ComprobacionPage(context.driver)
        context.all_page = AllPage(context.driver)
        context.all_page.menu_comision()
        time.sleep(4)
        context.all_page.buscar_comision(NUMERO_COMISIÓN)
        context.all_page.seleccionar_comision(estatus)

@given('Seleccionar menu de autorizar Consultar/Modificar comprobación')
def step_impl(context):
        context.comprobacion.clic_consultar()

@When('Agregar comprobación con gasto con comprobante y agregar impuesto')
def step_impl(context):
        data = context.data["formularios"]['COMPROBACION']
        context.comprobacion = ComprobacionPage(context.driver)
        context.comprobacion.clic_comprobar()
        context.comprobacion.clic_select()
        PATH_PDF = r"C:/Users/Lenovo/Downloads/Recibo.pdf"
        PATH_XML = r"C:/Users/Lenovo/Downloads/Recibo.xml"
        context.comprobacion.cargar_archivos(PATH_PDF,PATH_XML)
        context.comprobacion.cargar_formulario_comprobación(data)

@then('Visualizar el registro creado en el grid de comprobación')
def step_impl(context):
      
        record_data = {
            'column': 'Concepto',
            'registro': 'Alimentos',
            'num': False
        }

        assert context.comprobacion.validar_grid(record_data), \
                f"El registro no apareció en el grid"
        
