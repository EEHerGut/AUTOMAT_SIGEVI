import time
from venv import logger
from behave import *
from pages.comision_page import ComisionPage
from pages.all_page import AllPage
from pages.enviar_sol_page import EnvioPage
from config import NUMERO_COMISIÓN

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

    try:
        # Intenta corregir la codificación
        texto_corregido = estatus_comision.encode('latin1').decode('utf-8', errors='replace')
        # Busca el elemento con el texto corregido
        logger.info(f'no Falla: {texto_corregido}')
    except UnicodeError:
        # Fallback: buscar con texto literal si falla la decodificación
        texto_corregido='Solicitud de comisión pendiente de autxorización'
        logger.info(f'Falla: {texto_corregido}')
   
    context.all_page = AllPage(context.driver)
    context.envio_page = EnvioPage(context.driver)
    context.all_page.menu_comision()
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    context.all_page.seleccionar_comision("Solicitud de comisión pendiente de autxorización")
  
@when('Seleccionar menu de autorizar')
def step_impl(context):
  
    context.envio_page.seleccionar_menu_envio()

@when('Autorizar la solicitud y aceptar')
def step_impl(context):

    context.envio_page.click_confirmar()
    context.envio_page.click_aceptar()

@then('Validar el estatus de la comisión "Solicitud de comisión autorizada"')
def step_impl(context):
    context.all_page.buscar_comision(NUMERO_COMISIÓN)
    time.sleep(2)
    texto_esperado="Solicitud de comisión autorizada"
    xpath='//*[@id="body"]/main/app-root/app-commissions/div/app-table-commission/div/div/div[2]/table/tbody/tr[1]/td[6]/button'

    if not context.all_page.validar_texto_boton_por_xpath(xpath,texto_esperado): 
        raise AssertionError(f"No se encontró el botón con texto: {texto_esperado}")
 
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    
 
    