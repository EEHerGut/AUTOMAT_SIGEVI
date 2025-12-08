from selenium.webdriver.common.by import By
from .base_page import BasePage



class ReembolsarPage(BasePage):
    # Locators for Vuelos section
    MENU_REEMBOLSAR = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Solicitar')]")
    BOTON_ACEPTAR = (By.XPATH, "//button[contains(text(), 'Agregar') or contains(text(), 'Reembolsar ') or contains(@title, 'Agregar')]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-request-reimburs//button[contains(text(), 'Aceptar') or contains(text(), 'Add')]")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_reembolsar(self):
        self.wait_and_click(self.get_locator_botton('Solicitar reembolso'), self.DEFAULT_WAIT)
        return self
        
    def confirmar_autorizar(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self

