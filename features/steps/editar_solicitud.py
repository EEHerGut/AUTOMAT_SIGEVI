import time
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import SOLICITUDES


@given('El usuario operador ya inició sesión previamente y entro al panel de comisiones editar')
def step_impl(context):
    if not hasattr(context, 'login_exitoso'):
       
        context.execute_steps('''
            Given Hemos abierto la página inicial del sistema con el usuario y contraseña del usuario y seleccionamos el rol Operador SIGEVI
            When Dar clic en ingresar
            Then El sistema nos permite visualizar el panel principal
        ''')
        context.login_exitoso = True

    
@when('Seleccionar la solicitud para visualizar el detalle')
def step_impl(context):

    context.execute_steps('''
            Given visualizar la pagina principal
            When Seleccionar el menu comision y despues comisiones
            Then Visualizar el detalle de comisiones
        ''')
    
    context.execute_steps('''
            Given Visualizar el grid de comisiones
            When Agregar numero de comisión
            Then Visualizar la comisión y dar clic en detalle
        ''')

  

@when('Seleccionar solicitud')
def step_impl(context):

    elemento =WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Solicitud')]"))
    )
    elemento.click()
    

@Then('Editar la solicitud para pasarla a con anticipo, actualizar y cerrar sesión')
def step_impl(context):
    solicitud = SOLICITUDES["CON_ANTICIPO"] 
  
    time.sleep(5)
    # Usamos la tabla de datos del scenario para llenar los campos
  
    checkbox = WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.ID, "check"))
)

    if not checkbox.is_selected():
     checkbox.click()            
    context.driver.find_element(By.ID, "exitDate").clear()
    context.driver.find_element(By.ID, "exitDate").send_keys(solicitud["fecha_salida"])
    context.driver.find_element(By.ID, "returnDate").clear()
    context.driver.find_element(By.ID, "returnDate").send_keys(solicitud["fecha_regreso"])    
    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Actualizar') or @aria-label='Hola']"))
    )
    elemento.click()

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-edit-commission//button[contains(text(), 'Confirmar') or contains(text(), 'Aceptar')]"))
    )
    elemento.click()

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Cerrar']"))
    )
    elemento.click()
    context.driver.refresh()
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
    
    time.sleep(2)
