from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config import URLS
import pyautogui
import time

class ComisionesPage:
    # Locators for Comisiones section
    GRID = (By.XPATH, "//grid-locator")  # Update with actual locator
    DETALLE_BUTTON = (By.XPATH, "//button[contains(text(), 'Detalle')]")
    
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

class GastosPage:
    # Locators for Vuelos section
    MENU_GASTOS = (By.XPATH, "//app-status-details//tr/td[1]//li[4]/a")
    AGREGAR_GASTO_BUTTON = (By.XPATH, "//app-add-costs//button[contains(text(), 'Agregar') or contains(text(), 'Añadir')]")
    TIPO_GASTO_DROPDOWN = (By.XPATH, "//app-add-costs//select")
    MONTO_FIELD = (By.XPATH, "//app-add-costs//input")
    DESTINO_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[4]//select")
    AEROLINEA_DROPDOWN = (By.XPATH, "//app-add-flights//form//div[5]/div/select")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    ACEPTAR_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-guardar') or contains(text(), 'Aceptar')]")
    CONFIRMAR_BUTTON = (By.XPATH, "//app-add-flights//app-alert-grey//button[contains(@class, 'btn')]")
    
    # Grid validation locators
    AEROLINEA_CELL = (By.XPATH, "//app-add-flights//table//td[5]")
    ORIGEN_CELL = (By.XPATH, "//app-add-flights//table//td[2]")
    
    def __init__(self, driver):
        self.driver = driver
        
    def seleccionar_menu_gastos(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.MENU_GASTOS)
        ).click()
        
    def click_agregar_gasto(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.AGREGAR_GASTO_BUTTON)
        ).click()
        
    def seleccionar_tipo_gasto(self, tipo_gasto):
        trip_dropdown = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.TIPO_GASTO_DROPDOWN)
        )
        Select(trip_dropdown).select_by_visible_text(tipo_gasto)

    def agregar_monto(self, monto):
        campo_monto = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.MONTO_FIELD)
        )
        campo_monto.send_keys(monto)

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
       
    def guardar_gasto(self):
        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        ).click()

        WebDriverWait(self.driver, 15).until(
        EC.element_to_be_clickable((self.ACEPTAR_BUTTON))
        ).click

       
       
        
    def validar_registro_grid(self, origen, aerolinea):
        try:
            # Validate airline
            celda_aerolinea = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.AEROLINEA_CELL)
            )
            assert aerolinea in celda_aerolinea.text, f"Aerolínea '{aerolinea}' no encontrada"
            
            # Validate origin
            celda_origen = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.ORIGEN_CELL)
            )
            assert origen in celda_origen.text, f"Origen '{origen}' no encontrado"
            
            return True
        except Exception as e:
            raise AssertionError(f"Error al validar registro en el grid: {str(e)}")
            
    def refresh_page(self):
        self.driver.refresh()
        self.driver.execute_script("document.body.style.zoom='80%'")

    def navegar_a_comisiones(self):
        """Navega directamente a la página de comisiones"""
        if not self.driver.current_url.startswith(URLS['COMISIONES']):
            self.driver.get(URLS['COMISIONES'])
           