from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time

class CiudadPage(BasePage):
   
    # Locators
    MENU_CIUDADES_XPATH = (By.XPATH, "//a[contains(@class, 'dropdown-item goUrl') and contains(text(), ' Ciudades ')]")
    BOTON_AGREGAR_MUNICIPIO_XPATH = (By.XPATH, "//app-add-city//button[normalize-space()='Agregar municipio']")
    BOTON_AGREGAR_CIUDAD_XPATH = (By.XPATH, "//button[contains(text(), ' Agregar ciudad ')]")
    SELECT_PAIS =(By.XPATH,"//app-add-city-international//select")
    SELECT_CIUDAD =(By.XPATH,"//app-add-city-international//form/div[2]//select")
    ESTADO_DROPDOWN_ID = (By.XPATH, "//app-add-city//form//select")
    MUNICIPIO_DROPDOWN_ID = (By.ID, "town")
    BOTON_GUARDAR_XPATH = (By.XPATH, "//*[@id='addFormModal']/div/div/div/div[3]/form/button")
    BOTON_CERRAR_MENSAJE_XPATH = (By.XPATH, "//p[contains(text(), 'Municipio agregado correctamente')]/following::button[1]")
    BOTON_CERRAR_PAIS_XPATH = (By.XPATH, "//p[contains(text(), 'Ciudad agregada correctamente')]/following::button[1]")
    MODAL_EXITO=  (By.XPATH, "//app-add-city//p[contains(@class, 'description') or contains(text(), 'Municipio agregado correctamente.')]")

    def __init__(self, driver):
        super().__init__(driver)
    
    def seleccionar_menu_ciudades(self):
              
        self.wait_and_click(self.get_locator_botton('Ciudades'), self.DEFAULT_WAIT)
        return self
    
    def click_agregar_ciudad(self):

         try:
            self.wait_and_click(self.BOTON_AGREGAR_MUNICIPIO_XPATH, 2)
            return self
         except TimeoutException  :
            self.wait_and_click(self.BOTON_AGREGAR_CIUDAD_XPATH, self.DEFAULT_WAIT)
            return self
         
    def guardar_ciudad(self,data):
        
       
        try:
            dropdown = self.wait_for_element(self.ESTADO_DROPDOWN_ID, 2)
            Select(dropdown).select_by_visible_text(data['state'])
            time.sleep(2)
            dropdown = self.wait_for_element(self.MUNICIPIO_DROPDOWN_ID, 2)
            Select(dropdown).select_by_visible_text(data['town'])
            self.wait_and_click(self.BOTON_GUARDAR_XPATH, self.DEFAULT_WAIT)
            return "nacional"
        except TimeoutException:
            time.sleep(2)
            dropdown = self.wait_for_element(self.SELECT_PAIS, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['country'])
            time.sleep(2)
            dropdown = self.wait_for_element(self.SELECT_CIUDAD, self.LONG_WAIT)
            Select(dropdown).select_by_visible_text(data['capital'])
            time.sleep(2)
            self.wait_and_click(self.BOTON_GUARDAR_XPATH, self.DEFAULT_WAIT)
            return "internacional"

    
    def verificar_creacion_exitosa(self,tipo):
      
      if tipo=="nacional":
        self.wait_and_click(self.BOTON_CERRAR_MENSAJE_XPATH, 2)
        return self
      else:
        self.wait_and_click(self.BOTON_CERRAR_PAIS_XPATH, self.DEFAULT_WAIT)
        return self

    def cerrar_mensaje_exito(self):
        assert True