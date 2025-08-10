from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
import pyautogui


class VuelosPage(BasePage):
    # Locators for Vuelos section
    MENU_VUELOS = (By.XPATH, "//a[contains(text(), 'Aprobar') or contains(text(), 'Vuelos')]")
    AGREGAR_VUELO_BUTTON = (By.XPATH, "//*[@id='body']/main/app-root/app-add-flights/div/div/button")
    TRIP_DROPDOWN = (By.ID, "trip")
    ORIGEN_DROPDOWN = (By.XPATH, "//label[contains(text(),'Origen')]/following::select[1]")
    DESTINO_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[4]//select")
    AEROLINEA_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[5]/div/select")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='addFormModal']//button[@type='submit' or @class='btn-primary']")
    ACEPTAR_BUTTON = (By.XPATH, "//app-alert-grey//button[contains(text(), 'Aceptar')]")
    CONFIRMAR_BUTTON = (By.XPATH, "//app-add-flights//app-alert-grey//button[contains(@class, 'btn')]")

    def __init__(self, driver):
     super().__init__(driver)
        
    def seleccionar_menu_vuelos(self):
        self.wait_and_click(self.MENU_VUELOS, self.DEFAULT_WAIT)
        return self
        
    def click_agregar_vuelo(self):
        self.wait_and_click(self.AGREGAR_VUELO_BUTTON, self.DEFAULT_WAIT)
        return self
        
    def seleccionar_tipo_vuelo(self, tipo_vuelo):
   
        self.select_by_visible_text(self.TRIP_DROPDOWN,tipo_vuelo)
        return self

        
    def ingresar_datos_vuelo(self, origen, destino, aerolinea):
        
        # Select origin
        self.select_by_visible_text(self.ORIGEN_DROPDOWN,origen)
        # Select destination
        self.select_by_visible_text(self.DESTINO_DROPDOWN,destino)  
        pyautogui.click(x=830, y=410) 
        pyautogui.press("left")
        self.select_by_visible_text(self.AEROLINEA_DROPDOWN,aerolinea)
      
        
       
    def guardar_vuelo(self):
           self.wait_and_click(self.SUBMIT_BUTTON,self.DEFAULT_WAIT)
           self.wait_and_click(self.ACEPTAR_BUTTON,self.DEFAULT_WAIT)
           self.wait_and_click(self.CONFIRMAR_BUTTON,self.DEFAULT_WAIT)
           time.sleep(2)
           return self 
        


