import time
from behave import *
from pages.comision_page import ComisionPage
from pages.all_page import AllPage
from config import NUMERO_COMISIÓN,ESTATUS_COMISIÓN

@given('El usuario se encuentra en el grid de comisiones autorizar')
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
    
    context.comision_page = ComisionPage(context.driver)


@given('seleccionar solicitud que cuenta con el estatus {estatus_comision}')
def step_impl(context,estatus_comision):
    context.all_page = AllPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision(estatus_comision)
  
@when('Seleccionar menu de autorizar')
def step_impl(context):
    envio_page = EnvioPage(context.driver)
    envio_page.confirmar_envío()

@when('Autorizar la solicitud y aceptar')
def step_impl(context):
    envio_page = EnvioPage(context.driver)
    envio_page.confirmar_envío()

@then('Validar el estatus de la comisión "Solicitud de comisión autorizada"')
def step_impl(context):
 time.sleep(3)
 context.all_page = AllPage(context.driver)
 context.all_page.buscar_comision(NUMERO_COMISIÓN)



 texto_esperado="Solicitud de comisión pendiente de autorización"
 xpath='//*[@id="body"]/main/app-root/app-commissions/div/app-table-commission/div/div/div[2]/table/tbody/tr[1]/td[6]/button'

 if not context.all_page.validar_texto_boton_por_xpath(xpath,texto_esperado):
    raise AssertionError(f"No se encontró el botón con texto: {texto_esperado}")
 
 context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    
 
    