from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

import pyautogui
import time

class ComprobacionPage(BasePage):
       # Element locators
       MENU_CONSULTAR = (By.XPATH, "//a[contains(text(), 'Consultar')]")
       BOTON_ADDCOMPRO= (By.XPATH, "//button[contains(text(), 'Agregar comprobación')]")
       CHECKBOX_ANTICIPO = (By.XPATH, "//*[@id='check']")
       BOTON_CONTINUAR = (By.XPATH, "//*[@id='addFormModal']//button[contains(text(), 'Continuar')]")
       PDF = (By.XPATH, "//input[@type='file' and contains(@id, 'invoicePDF')]")
       XML = (By.XPATH, "//input[@type='file' and contains(@id, 'invoiceXML')]")
       BOTON_SIGUIENTE = (By.XPATH, "//*[@id='addFormModal']//button[contains(text(), 'Siguiente')]")
       CONCEPTO_GASTO = (By.XPATH, "//*[@id='conceptNew']")
       IMPORTE = (By.XPATH, "//*[@id='import']")
       BOTON_AGREGAR = (By.XPATH, "//*[@id='addFormModal']//button[contains(text(), 'Agregar')]")
       CONFIRMAR = (By.XPATH, "//*[@id='addFormModal']//button[contains(text(), 'Aceptar')]")
       BOTON_IMPUESTO = (By.XPATH, "//button[@title='' or contains(@class, 'btn btn-sm btn-primary')]")
       DROP_IMPUESTO = (By.XPATH, "//app-verification-table//form//select")
       MONTO_IMPUESTO = (By.XPATH, "//*[@id='amount']")
       BOTON_AC_IMPUESTO = (By.XPATH, "//app-verification-table//form//button[contains(text(), 'Agregar')]")
       BOTON_CONF_IMPUESTO = (By.XPATH, "//app-verification-table//button[contains(text(), 'Aceptar')]") 
       GRID_COMPROBACIONES = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")

       def __init__(self, driver):
            super().__init__(driver)
           
       def clic_consultar(self):
            self.wait_and_click(self.get_locator_botton('Consultar'), self.DEFAULT_WAIT)
            return self
       
       def clic_comprobar(self):
            self.wait_and_click(self.BOTON_ADDCOMPRO, self.DEFAULT_WAIT)
            return self
       
       def clic_select(self):
             self.set_checkbox(self.CHECKBOX_ANTICIPO,self.DEFAULT_WAIT)
             self.wait_and_click(self.BOTON_CONTINUAR, self.DEFAULT_WAIT)
             return self
       
       def cargar_archivos(self,PATH_PDF,PATH_XML):
             self.upload_file(self.PDF,PATH_PDF)
             self.upload_file(self.XML,PATH_XML)
             self.wait_and_click(self.BOTON_SIGUIENTE, self.DEFAULT_WAIT)
             return self
       
       def cargar_formulario_comprobación(self,data):
             ##concepto,importe,concepto_impuesto,monto
             time.sleep(2)
             pyautogui.click(x=768, y=350) 
             time.sleep(1)
             pyautogui.press("left")
             time.sleep(1)
             pyautogui.click(x=768, y=390) 
             time.sleep(1)
             pyautogui.press("right")
        
             dropdown = self.wait_for_element(self.CONCEPTO_GASTO, self.LONG_WAIT)
             Select(dropdown).select_by_visible_text(data['concepto'])
             self.send_keys(self.IMPORTE,data['monto'])
             self.wait_and_click(self.BOTON_AGREGAR, self.DEFAULT_WAIT)
             self.wait_and_click(self.CONFIRMAR, self.DEFAULT_WAIT)
             self.wait_and_click(self.BOTON_IMPUESTO, self.DEFAULT_WAIT)
             self.select_by_value(self.DROP_IMPUESTO,data['concepto_impuesto'])
             self.send_keys(self.MONTO_IMPUESTO,data['monto_impuesto'])
             self.wait_and_click(self.BOTON_AC_IMPUESTO, self.DEFAULT_WAIT)
             self.wait_and_click(self.BOTON_CONF_IMPUESTO, self.DEFAULT_WAIT)

             return self
       
       def validar_grid(self,record_data):
            
            self.validate_record_values_norecord(grid_locator=self.GRID_COMPROBACIONES,record_data=record_data)
            return self

             
             



"""file_input = (By.CSS_SELECTOR, "input[accept='.pdf,.jpg']")
file_path = "/ruta/completa/imagen.jpg"
verification = (By.XPATH, "//div[contains(text(),'Archivo cargado')]")
assert self.upload_file_with_verification(file_input, file_path, verification)

# En tus steps o page objects
file_input = (By.XPATH, "//input[@type='file']")
file_path = "/ruta/completa/archivo.pdf"
self.upload_file(file_input, file_path)
"""
