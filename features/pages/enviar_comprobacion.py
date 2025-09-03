from selenium.webdriver.common.by import By
from .base_page import BasePage 

class EnviarcomprobacionPage(BasePage):
        #element colector
        MENU_COMPROBACIÓN = (By.XPATH, "//a[contains(text(), 'Envío a comprobación')]")
        BOTON_ACEPTAR = (By.XPATH, "//*[@id='sendPay']//button[contains(@class, 'btn btn-primary')]")
        BOTON_CONFIRMAR = (By.XPATH, "//*[@id='sendPay']//button[contains(@class, 'btn btn-primary')]")
        GRID_TABLE = (By.XPATH, "//table[contains(@class, 'table')]")


        def __init__(self, driver):
            super().__init__(driver)  

        def seleccionar_menu(self):
            self.wait_and_click(self.MENU_COMPROBACIÓN, self.DEFAULT_WAIT)
            return self
        
        def confirmar_envio(self):
            self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
            self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT)
            return self
        
        def validar_grid(self,record_data):
            
            self.validate_record_values(grid_locator=self.GRID_TABLE,record_data=record_data)
            return self
          

