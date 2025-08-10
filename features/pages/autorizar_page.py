from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import URLS
from .base_page import BasePage
import pyautogui
import time


class AutorizarPage(BasePage):
    # Locators for Vuelos section
    MENU_ENVIO = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Autorizar')]")
    BOTON_ACEPTAR = (By.XPATH, "//app-authorize//button[contains(text(), ' Aceptar ')]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-authorize//button[contains(text(), 'Aceptar')]")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_envio(self):
        self.wait_and_click(self.MENU_ENVIO, self.DEFAULT_WAIT)
        return self
        
    def confirmar_envio(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self

