import time
from behave import *
from config import SOLICITUDES
from pages.comision_page import ComisionPage
from pages.all_page import AllPage
"""
@given('El usuario se encuentra en el grid de comisiones')
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
  
    
@given('Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud')

def step_impl(context):
 
    context.comision_page = ComisionPage(context.driver)
    context.all_page = AllPage(context.driver)
    context.all_page.refresh_page()
    time.sleep(9)
    context.all_page.menu_comision()
    time.sleep(5)
    context.comision_page.click_nueva_solicitud()  

@then('Deberíamos ver el formulario de solicitud de comisión')
def step_impl(context):
    context.comision_page.verificar_formulario_visible()

@when('Completamos los campos obligatorios')
def step_impl(context):
    solicitud = SOLICITUDES["SIN_ANTICIPO"]
    
    # Si hay datos en la tabla del scenario, usarlos para sobrescribir valores
    if hasattr(context, 'table') and context.table is not None:
        for row in context.table:
            campo = row['Campo']
            valor = row['Valor']
            # Convierte el nombre del campo al formato usado en SOLICITUDES
            clave = campo.lower().replace(' ', '_')
            solicitud[clave] = valor
    
    # Asegurarse que comision_page está inicializado
    if not hasattr(context, 'comision_page'):
        context.comision_page = ComisionPage(context.driver)
    
    context.comision_page.completar_campos_obligatorios(solicitud)
    
@when('Guardamos la solicitud')
def step_impl(context):
    context.comision_page.guardar_solicitud()

@then('La solicitud se crea exitosamente')
def step_impl(context):
    context.comision_page.verificar_creacion_exitosa()
    
  