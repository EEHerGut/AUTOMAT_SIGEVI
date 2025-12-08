from selenium.webdriver.common.by import By
from ..base_page import BasePage
from selenium.common.exceptions import TimeoutException
from features.locators.botones_comunes import BotonesComunes 
import time

class EstadoPage(BasePage):

    #LOCATORS

    BOTON_NUEVOESTADO = (By.XPATH, "//a[contains(text(), 'Nuevo')]") 
    INPUT_ESTADO = (By.XPATH, "//input[@placeholder='Estado']")
    
    def __init__(self, driver):
        super().__init__(driver)


    #ALTA DE ESTADO
    def click_agregar_estado(self,nombre_estado):
        campos = {self.INPUT_ESTADO: nombre_estado}
        return self.click_agregar(self.BOTON_NUEVOESTADO).guardar_registro(campos)
    

    def validar_grid(self,record_data):
         self.validate_record_values_norecord(grid_locator=BotonesComunes.GRID,record_data=record_data)
         return self
    
        #EDITAR estado
    def editar_estado(self,data):
        campos = {self.INPUT_ESTADO: data }
        return self.editar_registro(campos)
    
    #activar/desactivar aerolinea
    def act_estado(self):
        return self.activar_desactivar_registro()
    
    def validar_vista(self):
        """Método simple para validar visibilidad del botón Nueva"""
        return self.is_button_visible(self.BOTON_NUEVOESTADO,By.XPATH)   
    
    