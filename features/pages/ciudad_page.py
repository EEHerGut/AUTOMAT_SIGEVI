from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
import time

class CiudadPage(BasePage):
   
    # Locators
    MENU_CIUDADES_XPATH = (By.XPATH, "//a[contains(@class, 'dropdown-item goUrl') and contains(text(), ' Ciudades ')]")
    BOTON_AGREGAR_CIUDAD_XPATH = (By.XPATH, "//app-add-city//button[normalize-space()='Agregar municipio']")
    ESTADO_DROPDOWN_ID = (By.ID, "state")
    MUNICIPIO_DROPDOWN_ID = (By.ID, "town")
    BOTON_GUARDAR_XPATH = (By.XPATH, "//*[@id='addFormModal']/div/div/div/div[3]/form/button")
    BOTON_CERRAR_MENSAJE_XPATH = (By.XPATH, "//p[contains(text(), 'Municipio agregado correctamente')]/following::button[1]")
    MODAL_EXITO=  (By.XPATH, "//app-add-city//p[contains(@class, 'description') or contains(text(), 'Municipio agregado correctamente.')]")

    def __init__(self, driver):
        super().__init__(driver)
    
    def seleccionar_menu_ciudades(self):
        self.wait_and_click(self.MENU_CIUDADES_XPATH, self.DEFAULT_WAIT)
        return self
    
    def click_agregar_ciudad(self):
        self.wait_and_click(self.BOTON_AGREGAR_CIUDAD_XPATH, self.DEFAULT_WAIT)
        return self
    
    def seleccionar_estado(self, estado):

        dropdown = self.wait_for_element(self.ESTADO_DROPDOWN_ID, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(estado)
        return self
         
    def guardar_ciudad(self,data):
        
        time.sleep(2)
        dropdown = self.wait_for_element(self.ESTADO_DROPDOWN_ID, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['state'])
        dropdown = self.wait_for_element(self.MUNICIPIO_DROPDOWN_ID, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['town'])
        self.wait_and_click(self.BOTON_GUARDAR_XPATH, self.DEFAULT_WAIT)
        return self
    
    
    def cerrar_mensaje_exito(self):
        self.wait_and_click(self.BOTON_CERRAR_MENSAJE_XPATH, self.DEFAULT_WAIT)
        return self

    def verificar_creacion_exitosa(self):
        """Verifica que la solicitud se creó correctamente"""
        mensaje_exito = self.get_text(self.MODAL_EXITO).lower()
        assert "municipio agregado correctamente." in mensaje_exito, f"Se esperaba 'Municipio agregado correctamente.' pero se encontró: '{mensaje_exito}'"

