
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from config import URLS
from .base_page import BasePage 

class LoginPage(BasePage):
        
    LOGGED_IN_INDICATOR = (By.XPATH, "//app-home//button[contains(@class, 'primary') and contains(text(), 'Continuar')]")
    usuario_input = (By.XPATH, "//input[@placeholder='Contraseña' or @placeholder='Ingresa tu usuario']")
    password_input = (By.XPATH, "//input[@placeholder='Contraseña' or @placeholder='Ingresa tu contraseña']")
    login_button = (By.XPATH, "//*[@id='container-fluid']/div/div[2]/form/div[5]/div/button")
    role_dropdown = (By.ID, "roleUser")
    confirm_button = (By.XPATH, "//*[@id='container-fluid']/div/div[2]/div[2]/form/div[2]/div/button")
    breadcrumb = (By.XPATH, "//*[@id='body']/main/app-root/app-home/app-navbar/app-breadcrumb/div/ol/li[2]")
    BOTON_CERRARSESION= (By.XPATH, "//li[contains(@class, 'nav-item')]//a[.//img[contains(@src, 'box-arrow-right')]]")
    CONFIRMAR = (By.XPATH, "//button[normalize-space()='Cerrar Sesión']")     
           
    def __init__(self, driver,context):
        super().__init__(driver)
        self.context = context 
    
    def is_user_logged_in(self):
        """Verifica si el usuario ya tiene sesión activa"""
        try:
            # Busca cualquier elemento que indique sesión activa
             return bool(self.wait.until(
                EC.presence_of_element_located(self.LOGGED_IN_INDICATOR)
            ))
        except:
            return False

    def navigate_to_login_page(self):
        """Navega a la página de login"""
        self.driver.get(URLS["BASE"])
        self.driver.execute_script("document.body.style.zoom='80%'")

    def enter_credentials(self, datos):
        self.wait_for_element(self.usuario_input,self.LONG_WAIT)
        """Ingresa usuario y contraseña"""
        self.driver.find_element(*self.usuario_input).send_keys(datos["usuario"])
        self.driver.find_element(*self.password_input).send_keys(datos["password"])
        self.wait_and_click(self.login_button, self.DEFAULT_WAIT)
        
        dropdown = self.wait_for_element(self.role_dropdown, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(datos["rol"])
        self.wait_and_click(self.confirm_button, self.DEFAULT_WAIT)

##cerrar sesion
    def cerrar_sesion(self):
        
        self.wait_and_click(self.BOTON_CERRARSESION, self.DEFAULT_WAIT)
        self.wait_and_click(self.CONFIRMAR, self.DEFAULT_WAIT)
        return self
          
  

