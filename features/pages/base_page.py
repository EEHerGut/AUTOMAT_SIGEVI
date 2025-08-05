from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIEMPOS_ESPERA
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.DEFAULT_WAIT = TIEMPOS_ESPERA['DEFAULT_WAIT']
        self.LONG_WAIT = TIEMPOS_ESPERA['LONG_WAIT']
        self.SHORT_WAIT = TIEMPOS_ESPERA['SHORT_WAIT']
    
    
    def find_element(self, locator):
        """Encuentra un elemento esperando a que sea visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        """Encuentra múltiples elementos"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Hace click en un elemento después de esperar que sea clickeable"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
   


    def send_keys(self, locator, text):
        """Limpia el campo y escribe el texto"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        return self.find_element(locator).text
    
    def is_visible(self, locator, timeout=None):
        """Verifica si un elemento es visible"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    def take_screenshot(self, filename):
        """Toma un screenshot"""
        self.driver.save_screenshot(filename)

    def select_by_visible_text(self, locator, text):
        """Selecciona una opción por texto visible en un dropdown"""
        Select(self.find_element(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        """Selecciona una opción por valor en un dropdown"""
        Select(self.find_element(locator)).select_by_value(value)
    
    def upload_file(self, file_input_locator, file_path):
        """Sube un archivo a un input de tipo file"""
        file_input = self.find_element(file_input_locator)
        file_input.send_keys(file_path)
    
    def make_file_input_visible(self, file_input_locator):
        """Hace visible un input file (para casos donde está oculto)"""
        self.driver.execute_script(
        "arguments[0].style.display = 'block';", 
        self.find_element(file_input_locator))
     
    def set_checkbox(self, checkbox_locator, state):
         """Establece el estado de un checkbox (True/False)"""
         checkbox = self.find_element(checkbox_locator)  # Primero obtenemos el elemento
         if (checkbox.is_selected() and not state) or (not checkbox.is_selected() and state):
           checkbox.click()

    def is_checkbox_checked(self, checkbox_locator):
          """Verifica si un checkbox está marcado"""
          return self.find_element(checkbox_locator).is_selected()
    
    def is_element_present(self, locator, timeout=10):
        """Verifica si un elemento está presente en el DOM"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
    

    def clear_and_send_keys(self, locator, text):
            """Limpia un campo y escribe texto"""
            element = self.is_element_presentement(locator)
            element.clear()
            element.send_keys(text)

    def is_logged_in(self):
        try:
            return self.is_visible(self.SESSION_MARKER["UI_MARKER"])
        except:
         return False
        
    def wait_for_element(self, locator, timeout=10):
        """Espera a que un elemento sea visible y lo retorna"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
    
    def wait_and_click(self, locator, timeout):
        """Espera a que un elemento sea clickeable y hace click"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        element.click()
        return self
    
            
   