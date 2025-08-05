from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import URLS
import pyautogui
import time


class AutorizarPage:
    # Locators for Vuelos section
    MENU_ENVIO = (By.XPATH, "//app-details-table-commission//a[contains(@class, '') and contains(text(), ' Envío a autorización ')]")
    AGREGAR_VUELO_BUTTON = (By.XPATH, "//*[@id='body']/main/app-root/app-add-flights/div/div/button")
    TRIP_DROPDOWN = (By.ID, "trip")
    ORIGEN_DROPDOWN = (By.XPATH, "//label[contains(text(),'Origen')]/following::select[1]")
    DESTINO_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[4]//select")
    AEROLINEA_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[5]/div/select")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='sendPay']//button[contains(@class, 'btn btn-primary') and contains(text(), 'Aceptar')]")
    ACEPTAR_BUTTON = (By.XPATH, "//div[@id='sendPay']//button[contains(@class, 'btn-primary') and contains(text(), 'Aceptar')]")
    CONFIRMAR_BUTTON = (By.XPATH, "//app-add-flights//app-alert-grey//button[contains(@class, 'btn')]")
    

    
    def __init__(self, driver):
        self.driver = driver
        
    def seleccionar_menu_envio(self):
        ##//app-details-table-commission//a[contains(@class, 'dropdown-item goUrl') and (@data-action='edit' or contains(text(), ' Autorizar '))]
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.MENU_ENVIO)
        ).click()
        
    def click_confirmar_(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.AGREGAR_VUELO_BUTTON)
        ).click()
        
    def seleccionar_tipo_vuelo(self, tipo_vuelo):
        trip_dropdown = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.TRIP_DROPDOWN)
        )
        Select(trip_dropdown).select_by_visible_text(tipo_vuelo)
        
    def ingresar_datos_vuelo(self, origen, destino, aerolinea):
        
        # Select airline
        time.sleep(5)
        Select(WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.AEROLINEA_DROPDOWN)
        )).select_by_visible_text(aerolinea)
        
        # Set departure date (using pyautogui as in original)
        pyautogui.click(x=830, y=410) 
        pyautogui.press("left")
        # Select origin
        Select(WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ORIGEN_DROPDOWN)
        )).select_by_visible_text(origen)
        
        # Select destination
        Select(WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.DESTINO_DROPDOWN)
        )).select_by_visible_text(destino)
       
    def confirmar_envío(self):
        time.sleep(2)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()
        
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ACEPTAR_BUTTON)
        ).click()
 
    def navegar_a_comisiones(self):
        """Navega directamente a la página de comisiones"""
        if not self.driver.current_url.startswith(URLS['COMISIONES']):
            self.driver.get(URLS['COMISIONES'])
           