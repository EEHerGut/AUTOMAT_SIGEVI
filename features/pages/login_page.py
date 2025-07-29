
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URLS

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.LOGGED_IN_INDICATOR = (By.XPATH, "//app-home//button[contains(@class, 'primary') and contains(text(), 'Continuar')]")
        self.usuario_input = (By.ID, "usuario")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='container-fluid']/div/div[2]/form/div[5]/div/button")
        self.role_dropdown = (By.ID, "roleUser")
        self.confirm_button = (By.XPATH, "//*[@id='container-fluid']/div/div[2]/div[2]/form/div[2]/div/button")
        self.breadcrumb = (By.XPATH, "//*[@id='body']/main/app-root/app-home/app-navbar/app-breadcrumb/div/ol/li[2]")

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

    def enter_credentials(self, usuario, password):
        """Ingresa usuario y contraseña"""
        self.driver.find_element(*self.usuario_input).send_keys(usuario)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        """Hace click en el botón de login"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def select_role(self, rol):
        """Selecciona el rol del dropdown"""
        dropdown_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.role_dropdown)
        )
        Select(dropdown_element).select_by_visible_text(rol)

    def click_confirm_button(self):
        """Confirma la selección de rol"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_button)
        ).click()

    def verify_successful_login(self):
        """Verifica que el login fue exitoso"""
        textos_esperados = ["Inicio"]
        elemento = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.breadcrumb)
        )
        texto_actual = elemento.text.strip()
        return any(texto in texto_actual for texto in textos_esperados)             

