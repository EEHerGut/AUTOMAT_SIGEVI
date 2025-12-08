from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
import time
import pyautogui


class VuelosPage(BasePage):
    # Locators for Vuelos section
    MENU_VUELOS = (By.XPATH, "//a[contains(text(), 'Aprobar') or contains(text(), 'Vuelos')]")
    AGREGAR_VUELO_BUTTON = (By.XPATH, "//*[@id='body']/main/app-root/app-add-flights/div/div/button")
    TRIP_DROPDOWN = (By.ID, "trip")
    ORIGEN_DROPDOWN = (By.XPATH, "//label[contains(text(),'Origen')]/following::select[1]")
    DESTINO_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[4]//select")
    AEROLINEA_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[5]/div/select")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='addFormModal']//button[@type='submit' or @class='btn-primary']")
    ACEPTAR_BUTTON = (By.XPATH, "//app-alert-grey//button[contains(text(), 'Aceptar')]")
    CONFIRMAR_BUTTON = (By.XPATH, "//app-add-flights//app-alert-grey//button[contains(@class, 'btn')]")
    ETIQUETA = (By.XPATH,"//strong[contains(., 'Solicitud:')]")
    GRID = (By.XPATH,"//app-add-flights//table")
    DATAPICKER = (By.XPATH,"//input[@id='salida' and @formcontrolname='fechaSalida']")


    def __init__(self, driver):
     super().__init__(driver)
        
    def seleccionar_menu_vuelos(self):
        
        self.wait_and_click(self.get_locator_botton('Vuelos'), self.DEFAULT_WAIT)
        return self
        
    def click_agregar_vuelo(self):
        self.wait_for_element(self.AGREGAR_VUELO_BUTTON,self.LONG_WAIT)
        self.wait_and_click(self.AGREGAR_VUELO_BUTTON, self.DEFAULT_WAIT)
        return self
        
    def seleccionar_tipo_vuelo(self, tipo_vuelo):
        self.wait_for_element(self.TRIP_DROPDOWN,self.LONG_WAIT)
        dropdown = self.wait_for_element(self.TRIP_DROPDOWN, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(tipo_vuelo['trip'])
        time.sleep(5)
        return self

    def establecer_fecha_salida(self, fecha):
        """Método robusto para establecer fecha en datepicker nativo"""
        datepicker = self.wait_for_element(self.DATAPICKER, self.LONG_WAIT)
        
        # Intentar con JavaScript primero
        try:
            self.driver.execute_script("""
                arguments[0].value = arguments[1];
                // Disparar eventos para que Angular detecte el cambio
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, datepicker, fecha)
            time.sleep(1)
        except:
            # Fallback: interacción manual
            datepicker.click()
            datepicker.clear()
            for char in fecha:
                datepicker.send_keys(char)
                time.sleep(0.1)
            datepicker.send_keys(Keys.TAB)
        
        # Verificar que la fecha se estableció
        fecha_establecida = datepicker.get_attribute('value')
        if fecha_establecida != fecha:
            print(f"Advertencia: Fecha establecida ({fecha_establecida}) no coincide con la esperada ({fecha})")
        
        return self
        
    

    def ingresar_datos_vuelo(self, data,Tipo_vuelo):
        
        # Select origin
        dropdown = self.wait_for_element(self.TRIP_DROPDOWN, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['trip'])

  
        if Tipo_vuelo == 'INTERNACIONAL':
            dropdown = self.wait_for_element(self.ORIGEN_DROPDOWN, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['origen_int'])
        
            dropdown = self.wait_for_element(self.DESTINO_DROPDOWN, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['arrive_int'])
        
        else:
            dropdown = self.wait_for_element(self.ORIGEN_DROPDOWN, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['origen'])
        
            dropdown = self.wait_for_element(self.DESTINO_DROPDOWN, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['arrive'])
        
        dropdown = self.wait_for_element(self.AEROLINEA_DROPDOWN, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['aeroline'])

         
        return self
      
        
       
    def guardar_vuelo(self):
           time.sleep(2)
           self.wait_and_click(self.SUBMIT_BUTTON,self.DEFAULT_WAIT)
           time.sleep(2)
           self.wait_and_click(self.ACEPTAR_BUTTON,self.DEFAULT_WAIT)
           time.sleep(2)
           self.wait_and_click(self.CONFIRMAR_BUTTON,self.DEFAULT_WAIT)
           time.sleep(10)
           return self 
    
    def validar_grid(self,record_data):
            
            self.validate_record_values_norecord(grid_locator=self.GRID,record_data=record_data)
            return self


