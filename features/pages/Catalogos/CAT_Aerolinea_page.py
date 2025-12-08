from selenium.webdriver.common.by import By
from ..base_page import BasePage
from features.locators.botones_comunes import BotonesComunes 


class AerolineaPage(BasePage):

    # Locators
    BOTON_NUEVAAEROLINEA = (By.XPATH, "//a[contains(text(), 'Nueva')]")
    INPUT_AEROLINEA = (By.XPATH, "//input[@id='expedienteAutoriza3']")
     
    def __init__(self, driver):
        super().__init__(driver)

    #Alta AEROLINEA
    def click_agregar_aerolinea(self,nombre_aerolinea):
        campos = {self.INPUT_AEROLINEA: nombre_aerolinea}
        return self.click_agregar(self.BOTON_NUEVAAEROLINEA).guardar_registro(campos)
    
    def validar_grid(self,record_data):
         self.validate_record_values_norecord(grid_locator=BotonesComunes.GRID,record_data=record_data)
         return self


    #EDITAR AEROLINEA
    def editar_aerolinea(self,nuevo_nombre):
        campos = {self.INPUT_AEROLINEA: nuevo_nombre + " - EDITADO"}
        return self.editar_registro(campos)
    

     #activar/desactivar aerolinea
    def act_aerolinea(self):
        return self.activar_desactivar_registro()
    

    def validar_vista(self):
        """Método simple para validar visibilidad del botón Nueva"""
        return self.is_button_visible(self.BOTON_NUEVAAEROLINEA,By.XPATH)   