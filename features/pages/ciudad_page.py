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
    MENSAJE_EXITO_XPATH = (By.XPATH, "//p[contains(text(), 'Municipio agregado correctamente')]")
    BOTON_CERRAR_MENSAJE_XPATH = (By.XPATH, "//p[contains(text(), 'Municipio agregado correctamente')]/following::button[1]")
    MODAL_EXITO=  (By.XPATH, "//app-add-city//p[contains(@class, 'description') or contains(text(), 'Municipio agregado correctamente.')]")

    def __init__(self, driver):
        super().__init__(driver)
    
    def seleccionar_menu_ciudades(self):
        self.click(self.MENU_CIUDADES_XPATH)
        return self
    
    def click_agregar_ciudad(self):
        self.click(self.BOTON_AGREGAR_CIUDAD_XPATH)
        return self
    
    def seleccionar_estado(self, estado):
        time.sleep(3)
        estado_dropdown = self.find_element(self.ESTADO_DROPDOWN_ID)
        time.sleep(3)
        estado_dropdown = self.find_element(self.ESTADO_DROPDOWN_ID)
        Select(estado_dropdown).select_by_visible_text(estado)
        return self
    
    def seleccionar_municipio(self, municipio):
        municipio_dropdown = self.find_element(self.MUNICIPIO_DROPDOWN_ID)
        Select(municipio_dropdown).select_by_visible_text(municipio)
        return self
    
    def guardar_ciudad(self):
        self.click(self.BOTON_GUARDAR_XPATH)
        return self
    
    def cerrar_mensaje_exito(self):
        self.click(self.BOTON_CERRAR_MENSAJE_XPATH)
        return self
    
    def verificar_mensaje_exito(self):
        return self.is_visible(self.MENSAJE_EXITO_XPATH)
    
    def verificar_creacion_exitosa(self):
        """Verifica que la solicitud se creó correctamente"""
        mensaje_exito = self.get_text(self.MODAL_EXITO).lower()
        assert "municipio agregado correctamente." in mensaje_exito, f"Se esperaba 'Municipio agregado correctamente.' pero se encontró: '{mensaje_exito}'"

    def refresh_page(self):
        self.driver.refresh()
        self.driver.execute_script("document.body.style.zoom='80%'")
    