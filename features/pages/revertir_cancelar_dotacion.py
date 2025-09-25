from selenium.webdriver.common.by import By
from .base_page import BasePage



class Revertir_CancelarDotacionPage(BasePage):
    # Locators for Vuelos section
    BOTON_ACEPTAR = (By.XPATH, "//app-reject-dot//div[@class='modal-footer' or contains(@class, 'footer')]//button[2]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-reject-dot//div[contains(@class, 'modal-footer')]/button")
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    BOTON_CANCELAR =(By.XPATH,"//app-cancel-dot//div[contains(@class, 'modal-footer')]/button[2]")
    CONFIRMAR_CANCELAR= (By.XPATH,"//app-cancel-dot/div/div/div/div[3]/button")
    BOTON_ACEPTAR_REV_DEP = (By.XPATH,"//app-revert-deposit/div/div/div/div[3]/button[2]")

    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_revertir(self):
        
        self.wait_and_click(self.get_locator_botton('Revertir dotación'), self.DEFAULT_WAIT)
        return self
        
    def confirmar_reversión(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT) 
         return self
       


############################## Cancelar

    def seleccionar_menu_cancelar(self):
        
        self.wait_and_click(self.get_locator_botton('Cancelar dotación'), self.DEFAULT_WAIT)
        return self
        
    def confirmar_cancelación(self):
         self.wait_and_click(self.BOTON_CANCELAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.CONFIRMAR_CANCELAR, self.DEFAULT_WAIT) 
         return self

################################ Revertir depósito

    def seleccionar_menu_revertir_dep(self):
        
        self.wait_and_click(self.get_locator_botton('Revertir depósito'), self.DEFAULT_WAIT)
        return self
        
    def confirmar_revertir_depósito (self):
         self.wait_and_click(self.BOTON_CANCELAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.CONFIRMAR_CANCELAR, self.DEFAULT_WAIT) 
         return self


################################
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self