from selenium.webdriver.common.by import By
from .base_page import BasePage


class DepositarPage(BasePage):
   
    # Locators
    MENU_DEPOSITAR = (By.XPATH, "//a[contains(@class, 'dropdown-item goUrl') and contains(text(), ' Depositar ')]")
    SOLICITAR_DEPTO = (By.XPATH, "//button[contains(text(), 'Solicitar depósito') or contains(text(), 'Confirm')]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-deposit-advance//button[1]")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def seleccionar_menu_depositar(self):
        self.wait_and_click(self.get_locator_botton('Depositar'), self.DEFAULT_WAIT)
        return self
    
    def click_confirmar_depósito(self):

        self.wait_and_click(self.SOLICITAR_DEPTO, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT)
        self.zoom_page()
        return self
            
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self


    
    

