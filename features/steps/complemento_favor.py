from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import COMPLEMENTO,ARCHIVOS
import time



@given('El autorizador ingresa al sistema, ingresa al grid de comisiones')
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

@when('Selecionar la comision conciliada para visualizar el detalle')
def step_impl(context):
    
    
    context.execute_steps('''
            Given Visualizar el grid de comisiones
            When Agregar numero de comisión
            Then Visualizar la comisión y dar clic en detalle
        ''')

@then('Seleccionar el menú Complementos, dar clic alta de complementos visualizar el formulario')
def step_impl(context):

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//app-details-table-commission//tr/td[1]//li[position()=8]/a"))
    )
    elemento.click()

    elemento = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, " //app-commission-complement//button[contains(text(), ' Alta de Complemento') or contains(text(), 'Nuevo')]"))
    )
    elemento.click()
   
@then('Dar de alta el formulario y dar clic en alta de complemento')
def step_impl(context):
    

        texto = context.driver.find_element(By.XPATH, "//app-encabezado-complemento//div[1]/p[4]").text  
        concepto_oper=COMPLEMENTO['FAVOR']['concepto_oper']
        importe=COMPLEMENTO['FAVOR']['importe']
        motivo=COMPLEMENTO['FAVOR']['motivo']

        
        
        ruta_archivo = r"C:/Users/Lenovo/Downloads/Recibo.pdf"
        input_file = WebDriverWait(context.driver, 15).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "input#archivoPDF[type='file']")
                    )
                )
        input_file.send_keys(ruta_archivo)
            
            #concepto operativo
        dropdown = Select(context.driver.find_element(By.XPATH, "//app-commission-complement//select[@name='tipoComplemento' or @id='conceptNew']"))
        dropdown.select_by_visible_text(concepto_oper)

            #importe
        context.driver.find_element(By.XPATH, "//app-commission-complement//form//div[5]//input").clear()
        context.driver.find_element(By.XPATH, "//app-commission-complement//form//div[5]//input").send_keys(importe)
            
      

        if texto == 'Moneda: MXN':
            checkbox = context.driver.find_element(By.ID, "taxes")
            checkbox.is_selected()
            #motivo del complento
            context.driver.find_element(By.XPATH, "//app-commission-complement//form//div[7]//textarea").clear()
            context.driver.find_element(By.XPATH, "//app-commission-complement//form//div[7]//textarea").send_keys(motivo)

            context.driver.execute_script("arguments[0].style.display = 'block';", input_file)
            input_file.send_keys(ruta_archivo)
            ruta_xml = r"C:/Users/Lenovo/Downloads/Recibo.pdf"

            data = WebDriverWait(context.driver, 15).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "input#archivoXML[type='file'][accept='application/xml']")
                    )
                )
            data.send_keys(ruta_xml)
        else:
            checkbox = context.driver.find_element(By.ID, "taxes")
            if checkbox.is_selected():  # Verificar si está seleccionado primero
             checkbox.click() 

            context.driver.find_element(By.XPATH, "//app-commission-complement//form//textarea[contains(@class, 'form-control areaInput ng-untouched ng-pristine ng-invalid')]").clear()
            context.driver.find_element(By.XPATH, "//app-commission-complement//form//textarea[contains(@class, 'form-control areaInput ng-untouched ng-pristine ng-invalid')]").send_keys(motivo)
            
        
            #boton altacomplemento
        elemento2 = WebDriverWait(context.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//app-commission-complement//button[contains(text(), 'Alta de complemento') or contains(text(), 'Enviar')]"))
            )
        context.driver.execute_script("arguments[0].scrollIntoView();", elemento2)
        time.sleep(5)
        elemento2.click()

            #boton confirmación
        elemento2 = WebDriverWait(context.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//app-modal-confirm-add//button[contains(@class, 'btn-confirm') or contains(text(), 'Aceptar')]"))
            )
        elemento2.click()
            #botón de alta de registro
        elemento2 = WebDriverWait(context.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//app-modal-add-ok//button[text()='Aceptar']"))
            )
        elemento2.click()
        time.sleep(2)

            
        context.execute_steps('''
                    Given Al terminar la prueba
                    When Dar clic en el botón de cerrar sesión
                    Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial
                ''')