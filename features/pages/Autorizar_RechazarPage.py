from selenium.webdriver.common.by import By
from .base_page import BasePage



class Autorizar_RechazarPage(BasePage):
    # Locators for Vuelos section
    MENU_AUTORIZAR = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Autorizar')]")
    MENU_RECHAZAR = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), 'Rechazar')]")
    BOTON_ACEPTAR = (By.XPATH, "//app-authorize//button[contains(text(), ' Aceptar ')]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-authorize//button[contains(text(), 'Aceptar')]")
    MOTIVO_AREA=(By.XPATH,"//app-reject-sol//textarea")
    BOTON_RECHAZAR =(By.XPATH,"//app-reject-sol//button[contains(text(), 'Aceptar')]")
    CONFIRMAR_RECHAZAR =(By.XPATH,"//app-reject-sol//button[contains(text(), 'Aceptar')]")

    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_autorizar(self):
        self.wait_and_click(self.MENU_AUTORIZAR, self.DEFAULT_WAIT)
        return self
        
    def confirmar_autorizar(self):
         self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.BOTON_CONFIRMAR, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self
    
    ####################################

    def seleccionar_menu_rechazar(self):
        self.wait_and_click(self.MENU_RECHAZAR, self.DEFAULT_WAIT)
        return self
        
    def confirmar_rechazo(self):
         self.send_keys(self.MOTIVO_AREA, "Motivo de rechazo")
         self.wait_and_click(self.BOTON_RECHAZAR, self.DEFAULT_WAIT)
         self.wait_and_click(self.CONFIRMAR_RECHAZAR, self.DEFAULT_WAIT) 
         return self
    
    def validar_grid(self,record_data):
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self


