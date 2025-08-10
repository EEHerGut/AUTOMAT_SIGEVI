from selenium.webdriver.common.by import By
from .base_page import BasePage 


class EnvioPage(BasePage):
    # Locators for Vuelos section
    MENU_ENVIO = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), ' Envío a autorización ')]")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='sendPay']//button[2]")
    ACEPTAR_BUTTON = (By.XPATH, "//*[@id='sendPay']//button[contains(text(), 'Aceptar')]")
    GRID_TABLE = (By.XPATH, "//table[contains(@class, 'table')]")

    def __init__(self, driver):
       super().__init__(driver)
        
    def seleccionar_menu_envio(self):
      self.wait_and_click(self.MENU_ENVIO, self.DEFAULT_WAIT)
      return self
    
    def confirmar_envío(self):
       self.wait_and_click(self.SUBMIT_BUTTON, self.DEFAULT_WAIT)
       self.wait_and_click(self.ACEPTAR_BUTTON, self.DEFAULT_WAIT)
       return self
    
    def validar_grid(self,record_data):
            
        self.validate_record_values(grid_locator=self.GRID_TABLE,record_data=record_data)
        return self