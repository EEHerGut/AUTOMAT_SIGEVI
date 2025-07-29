
from behave import *
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from config import IMPUESTO


@given('El autorizador ingresa al sistema para reembolsar al comisionado')
def step_impl(context):
   if not hasattr(context, 'login_exitoso'):
       
        context.execute_steps('''
            Given Hemos abierto la página inicial del sistema con el usuario y contraseña del usuario y seleccionamos el rol Operador SIGEVI
            When Dar clic en ingresar
            Then El sistema nos permite visualizar el panel principal
        ''')
        context.login_exitoso = True

        context.execute_steps('''
            Given visualizar la pagina principal
            When Seleccionar el menu comision y despues comisiones
            Then Visualizar el detalle de comisiones
        ''')

@when('Seleccionar la comisión conciliada para visualizar el detalle reembolsar')
def step_impl(context):
    
           
        context.execute_steps('''
            Given Visualizar el grid de comisiones
            When Agregar numero de comisión
            Then Visualizar la comisión y dar clic en detalle
        ''')
   
@when('Seleccionar el menú complementos para reembolsar complemento')
def step_impl(context):   

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-details-table-commission//tr/td[1]//li[position()=8]/a"))
    )
    elemento.click()


@when('Seleccionar el botón autorizado del complemento a reembolsar,visualizar el detalle')
def step_impl(context):
     
    id= IMPUESTO['id_complemento']
    ## QA xpath = f"//table/tbody/tr[{id}]/td[17]/button[contains(text(), 'Registrado')]"
    ##//app-table-complement-favor-de//tbody/tr[position()>=3]/td[17]/button
    ##"//app-table-complement-favor-de//tbody/tr[{id}]/td[5]/button"

    xpath = f'//app-table-complement-favor-de//tr[{id}]/td[5]/button'
    time.sleep(2)
    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,xpath))
    )
    elemento.click()
    

@then('Seleccionar el botón reembolso al comisionado, Solicitar reembolso, aceptar.')
def step_impl(context):
    time.sleep(2)

    boton_autorizar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//app-table-favor-detalle//a[contains(text(), "Reembolso al comisionado")]'))
    )
    boton_autorizar.click()
    boton_autorizar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//app-table-favor-detalle//a[contains(text(), "Reembolso al comisionado")]'))
    )
    boton_autorizar.click()
    
    boton_confirmar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//app-table-favor-detalle//button[contains(text(), "Solicitar Reembolso")]'))
    )
    boton_confirmar.click()
    time.sleep(15)
   
    """
    boton_aceptar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH,'//app-modal-ok-cargo//button[contains(@class, "btn-primary") or contains(text(), "Aceptar")]'))
    )
    boton_aceptar.click()
    """
    time.sleep(2)


@then('Validar estatus')
def step_impl(context):
    context.driver.refresh()
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')