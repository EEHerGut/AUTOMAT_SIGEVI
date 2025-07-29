from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import URLS
from pages.all_page import AllPage
import pyautogui
import time

class ComisionesPage:
    # Locators for Comisiones section
    def __init__(self, driver):
        self.driver = driver
        
    def visualizar_grid(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.GRID)
        )
        
    def agregar_numero_comision(self, numero):
        # Implementation for adding commission number
        pass
        
    def click_detalle(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.DETALLE_BUTTON)
        ).click()

class VuelosPage:
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
    
    # Grid validation locators
    AEROLINEA_CELL = (By.XPATH, "//app-add-flights//table//td[5]")
    ORIGEN_CELL = (By.XPATH, "//app-add-flights//table//td[2]")
    
    def __init__(self, driver):
        self.driver = driver
        
    def seleccionar_menu_vuelos(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.MENU_VUELOS)
        ).click()
        
    def click_agregar_vuelo(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.AGREGAR_VUELO_BUTTON)
        ).click()
        
    def seleccionar_tipo_vuelo(self, tipo_vuelo):
        trip_dropdown = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.TRIP_DROPDOWN)
        )
        Select(trip_dropdown).select_by_visible_text(tipo_vuelo)
        
    def ingresar_datos_vuelo(self, origen, destino, aerolinea):
        
        """  all_Page = AllPage(self.driver)
        all_Page.seleccionar_dropdown_con_reintentos(
            locator=self.AEROLINEA_DROPDOWN,
            valor=aerolinea,
            max_reintentos=3
        )"""

        
        # Set departure date (using pyautogui as in original)
        
        # Select origin
        Select(WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ORIGEN_DROPDOWN)
        )).select_by_visible_text(origen)
        
        # Select destination
        Select(WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.DESTINO_DROPDOWN)
        )).select_by_visible_text(destino)

        time.sleep(5)
        pyautogui.click(x=830, y=410) 
        pyautogui.press("left")
        
        time.sleep(5)
        Select(WebDriverWait(self.driver, 20).until(
              EC.element_to_be_clickable(self.AEROLINEA_DROPDOWN)
          )).select_by_visible_text(aerolinea)
        
       
    def guardar_vuelo(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()
        
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ACEPTAR_BUTTON)
        ).click()
        
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.CONFIRMAR_BUTTON)
        ).click()
        time.sleep(2)
        
            
    def refresh_page(self):
        time.sleep(2)
        self.driver.refresh()
        self.driver.execute_script("document.body.style.zoom='80%'")

    def navegar_a_comisiones(self):
        """Navega directamente a la página de comisiones"""
        if not self.driver.current_url.startswith(URLS['COMISIONES']):
            self.driver.get(URLS['COMISIONES'])
           