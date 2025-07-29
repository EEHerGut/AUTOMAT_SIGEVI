
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import IMPUESTO
import time


@given('El autorizador ingresa al sistema para agregar un impuesto a un complemento')
def step_impl(context):
  
   
       
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


@when('Seleccionar la comisión conciliada para visualizar el detalle')
def step_impl(context):
    
        
        context.execute_steps('''
            Given Visualizar el grid de comisiones
            When Agregar numero de comisión
            Then Visualizar la comisión y dar clic en detalle
        ''')
   
@when('Seleccionar el menú de complementos')
def step_impl(context):

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Complementos')]"))
    )
    elemento.click()
   
@when('Seleccionar el complemento, dar clic en el botón agregar impuesto')
def step_impl(context):
    time.sleep(2)
    texto = context.driver.find_element(By.XPATH, "//app-encabezado-complemento//div[1]/p[4]").text  
   
    if texto == 'Moneda: MXN':
        id= IMPUESTO['id_complemento']

        xpath = f"//table/tbody/tr[{id}]/td[17]/button[contains(text(),'Agregar Impuesto')]"
        time.sleep(2)
        elemento = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,xpath))
        )
        elemento.click()
    else:
         context.driver.refresh()
         context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')
         time.sleep(2)
         return

    
@then('Seleccionar el concepto y el monto, dar clic en agregar - aceptar y aceptar.')
def step_impl(context):

    
    concepto=IMPUESTO['concepto']
    monto=IMPUESTO['monto']
    
    #dropconcepto
    dropdown = Select(context.driver.find_element(By.XPATH, "//label[contains(text(), 'Concepto')]/following::select[1]"))
    dropdown.select_by_visible_text(concepto)
    #inputmonto

    # Localizar el elemento con espera
    element = WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Monto')]/following::input[1]"))
    )
    element.clear()
    element.send_keys(monto)
    
    boton_agregar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-table-complement-favor-de//button[normalize-space()='Agregar']"))
    )
    boton_agregar.click()


    boton_aceptar = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-modal-confirm-tax//button[contains(text(), 'Aceptar')]"))
    )
    boton_aceptar.click()

    boton_confimacion = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-modal-ok//button[contains(text(), 'Aceptar')]"))
    )
    boton_confimacion.click()
    context.driver.refresh()
    context.driver.execute_script("document.body.style.zoom='80%'")

    time.sleep(2)
    context.driver.refresh()
    context.execute_steps('''
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
        ''')



