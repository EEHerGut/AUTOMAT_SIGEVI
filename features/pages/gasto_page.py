from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage 
import time

class GastosPage(BasePage):
    # Locators for Vuelos section
    MENU_GASTOS = (By.XPATH, "//app-status-details//tr/td[1]//li[4]/a")
    AGREGAR_GASTO_BUTTON = (By.XPATH, "//app-add-costs//button[contains(text(), 'Agregar') or contains(text(), 'Añadir')]")
    TIPO_GASTO_DROPDOWN = (By.XPATH, "//app-add-costs//select")
    MONTO_FIELD = (By.XPATH, "//app-add-costs//input")
    DESTINO_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[4]//select")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    ACEPTAR_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-guardar') or contains(text(), 'Aceptar')]")
    # Grid validation locators
    AEROLINEA_CELL = (By.XPATH, "//app-add-flights//table//td[5]")
    ORIGEN_CELL = (By.XPATH, "//app-add-flights//table//td[2]")
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def seleccionar_menu_gastos(self):
        self.wait_and_click(self.MENU_GASTOS, self.DEFAULT_WAIT)
        return self
        
    def click_agregar_gasto(self):
        self.wait_and_click(self.AGREGAR_GASTO_BUTTON, self.DEFAULT_WAIT)
        return self
        
    def seleccionar_tipo_gasto(self, tipo_gasto):
        dropdown = self.wait_for_element(self.TIPO_GASTO_DROPDOWN, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(tipo_gasto)
        return self
    
    def agregar_monto(self, monto):
        campo = self.wait_for_element(self.MONTO_FIELD, self.DEFAULT_WAIT)
        campo.clear()
        campo.send_keys(monto)
        return self
    
    def guardar_gasto(self):
        time.sleep(2)
        self.wait_and_click(self.SUBMIT_BUTTON, self.DEFAULT_WAIT)
        self.wait_and_click(self.ACEPTAR_BUTTON, self.DEFAULT_WAIT)