from behave import *
from config import GASTO,NUMERO_COMISIÓN
from pages.gasto_page import GastosPage
from pages.all_page import AllPage

@given('Visualizar el grid de comisiones gasto con estatus "{estatus}"')
def step_impl(context,estatus):
     context.gasto_page = GastosPage(context.driver)
     context.all_page = AllPage(context.driver)
     context.all_page.menu_comision()
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(estatus)

@When('Seleccionar el menu de gasto')
def step_impl(context):
    context.gasto_page.seleccionar_menu_gastos()
@When('Dar clic en el botón Agregar gasto, seleccionar tipo de gasto, monto y dar clic en agregar')
def step_impl(context):

    context.gasto_page.click_agregar_gasto()
    context.gasto_page.seleccionar_tipo_gasto(GASTO['concept'])    
    context.gasto_page.agregar_monto(GASTO['amount'])
    context.gasto_page.guardar_gasto()
    
    
    assert context.failed is False

@Then('Validar registro en el grid de gasto')
def step_impl(context):
    context.all_page.refresh_page()
    context.execute_steps('''
			  Given Al terminar la prueba
              When Dar clic en el botón de cerrar sesión
              Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')