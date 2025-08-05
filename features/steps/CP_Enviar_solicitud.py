from behave import *
from pages.enviar_sol_page import EnvioPage
from config import NUMERO_COMISIÓN,ESTATUS_COMISIÓN
from pages.all_page import AllPage
import time
""" if not hasattr(context, 'login_exitoso'):
            context.execute_steps('''
                Given Hemos abierto la página inicial del sistema login
                When Capturas el usuario y contraseña
                And Seleccionar iniciar sesión
                When Seleccionar el rol y dar clic en continuar
                Then El sistema nos permite visualizar el panel principal
            ''')
        context.login_exitoso = True
        
        context.comision_page = ComisionPage(context.driver)"""

@given('Visualizar el grid de comisiones enviar al área de pagos')
def step_impl(context):
     
     context.all_page = AllPage(context.driver)
     context.envio_page = EnvioPage(context.driver)
     context.all_page.menu_comision()
     context.all_page.buscar_comision(NUMERO_COMISIÓN)
     context.all_page.seleccionar_comision(ESTATUS_COMISIÓN)
  
@when('Seleccionar el menu de envio a autorización')
def step_impl(context):
    
    context.envio_page.seleccionar_menu_envio()

@when('Confirmar el envío')
def step_impl(context):
  
    context.envio_page.confirmar_envío()

@then('Validar que la solicitud cuente con el estatus "Solicitud de comisión pendiente de autorización"')
def step_impl(context):

    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(2)
    texto_esperado="Solicitud de comisión pendiente de autorización"
    xpath='//*[@id="body"]/main/app-root/app-commissions/div/app-table-commission/div/div/div[2]/table/tbody/tr[1]/td[6]/button'

    if not context.all_page.validar_texto_boton_por_xpath(xpath,texto_esperado):
        raise AssertionError(f"No se encontró el botón con texto: {texto_esperado}")
 
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    
 
    