import time
from behave import *
from pages.all_page import AllPage
from pages.autorizar_page import AutorizarPage
from config import NUMERO_COMISIÓN

"""@given('El usuario se encuentra en el grid de comisiones autorizar')
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
@given('Seleccionar solicitud que cuenta con el estatus "{estatus}"')
def step_impl(context,estatus):

    time.sleep(2)
    context.all_page = AllPage(context.driver)
    context.autorizar_page = AutorizarPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(2)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus)
  
@when('Seleccionar menu de autorizar')
def step_impl(context):
  
    context.autorizar_page.seleccionar_menu_envio()

@when('Autorizar la solicitud y aceptar')
def step_impl(context):

    context.autorizar_page.confirmar_envio()

@then('Validar el estatus de la comisión "{estatus}" autorizar solicitud')
def step_impl(context,estatus):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(1)
    record_data = {
            'column': 'Estado ',
            'registro': estatus,
        }

    assert context.autorizar_page.validar_grid(record_data), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
    
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    

    