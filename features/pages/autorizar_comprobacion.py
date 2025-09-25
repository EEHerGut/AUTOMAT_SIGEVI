from selenium.webdriver.common.by import By
from .base_page import BasePage



class AutorizarComprobacionPage(BasePage):
    # Locators for Vuelos section
    MENU_APROBAR = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Aprobar')]")
    BOTON_ACEPTAR = (By.XPATH, "//*[@id='modalApprove']//button[contains(text(), ' Aceptar ')]")
    BOTON_CONFIRMAR = (By.XPATH, "//*[@id='closeModal'][contains(text(), 'Aceptar')]")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_autorizar(self):
        self.wait_and_click(self.get_locator_botton('Aprobar'), self.DEFAULT_WAIT)
        return self
        
    def confirmar_autorizar(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self
