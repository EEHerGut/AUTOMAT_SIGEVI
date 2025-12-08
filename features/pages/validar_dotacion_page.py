from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class ValidardotacionPage(BasePage):
    # Locators for Vuelos section
    MENU_AUTORIZAR = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Autorizar dotación')]")
    
    BOTON_ACEPTAR = (By.XPATH, "//app-validate-deposit//button[contains(text(), 'Aceptar')]")
    BOTON_ACEPTAR_1 = (By.XPATH, "//app-validate-deposit//button")
    BOTON_CONFIRMAR_SIN = (By.XPATH, "//app-authorize//button[contains(text(), 'Aceptar')]")
    BOTON_CONFIRMAR_CON = (By.XPATH, "//app-auth-dot//button")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    



    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_validardep(self):
        
        self.wait_and_click(self.get_locator_botton('Enviar a validar depósito'), self.DEFAULT_WAIT)
        time.sleep(1)
        self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_ACEPTAR_1, self.DEFAULT_WAIT)
        time.sleep(2)        
        return self
        
    def confirmar_autorizar_sin(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR_SIN, self.DEFAULT_WAIT) 
         return self
    
    def confirmar_autorizar_con(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR_CON, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self

