from selenium.webdriver.common.by import By
from .base_page import BasePage


class ConciliarPage(BasePage):
   
    # Locators
    SOLICITAR_DEPTO = (By.XPATH, "//button[contains(text(), 'Solicitar depósito') or contains(text(), 'Confirm')]")
    BOTON_ACEPTAR = (By.XPATH, "//app-reconcile/div/div/div/div[2]//button[2]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-reconcile//button")

    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def seleccionar_menu_conciliar(self):
        self.wait_and_click(self.get_locator_botton('Conciliar comisión'), self.DEFAULT_WAIT)
        return self
    
    def click_confirmar_conciliar(self):
        self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT)
        self.zoom_page()
        return self
            
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self


    
    
