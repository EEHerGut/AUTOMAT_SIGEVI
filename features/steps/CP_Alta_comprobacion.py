from behave import *
from pages.comprobacion_page import ComprobacionPage
from config import COMPROBACION,NUMERO_COMISIÓN
from pages.all_page import AllPage

concepto=COMPROBACION["concepto"]
monto=COMPROBACION["monto"]
concepto_impuesto=COMPROBACION["concepto_impuesto"]
monto_impuesto=COMPROBACION["monto_impuesto"]

"""
@given('El usuario se encuentra en el grid de comisiones comprobación')
def step_impl(context):
     if not hasattr(context, 'login_exitoso'):
        context.execute_steps('''
              Given Hemos abierto la página inicial del sistema login
			  When Capturas el usuario y contraseña
			  And Seleccionar iniciar sesión
			  When Seleccionar el rol y dar clic en continuar
              Then El sistema nos permite visualizar el panel principal
        ''')
        context.login_exitoso = True

       
  """

@given('Seleccionar solicitud que cuenta con el estatus "{estatus}" comprobación')
def step_impl(context,estatus):
        
        context.all_page = AllPage(context.driver)
        context.comision_page = ComprobacionPage(context.driver)
        context.all_page.menu_comision()
        context.all_page.buscar_comision(NUMERO_COMISIÓN)
        context.all_page.seleccionar_comision(estatus)

@given('Seleccionar menu de autorizar Consultar/Modificar comprobación')
def step_impl(context):
        context.comision_page.clic_consultar()

@When('Agregar comprobación con gasto con comprobante y agregar impuesto')
def step_impl(context):
        
        context.comision_page = ComprobacionPage(context.driver)
        context.comision_page.clic_comprobar()
        context.comision_page.clic_select()
        PATH_PDF = r"C:/Users/Lenovo/Downloads/Recibo.pdf"
        PATH_XML = r"C:/Users/Lenovo/Downloads/Recibo.xml"
        context.comision_page.cargar_archivos(PATH_PDF,PATH_XML)
        context.comision_page.cargar_formulario_comprobación(concepto,monto,concepto_impuesto,monto_impuesto)

@then('Visualizar el registro creado en el grid de comprobación')
def step_impl(context):
      
        record_data = {
            'column': 'Concepto',
            'registro': 'Alimentos',
        }

        assert context.comision_page.validar_grid(record_data), \
                f"El registro {concepto} con monto {monto} no apareció en el grid"
        
        context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    