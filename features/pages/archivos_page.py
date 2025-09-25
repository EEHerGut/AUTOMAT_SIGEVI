from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select


class ArchivosPage(BasePage):
    # Locators for Vuelos section
    AGREGAR_ARCHIVO_BUTTON = (By.XPATH, "//button[contains(text(), 'Agregar') or contains(text(), 'Ag') or contains(text(), 'Add')]")
    ARCHIVO_DROPDOWN = (By.XPATH, "//select[@formControlName='typeFile']")
    AREA = (By.XPATH, "//textarea[@formControlName='description']")
    AGREGAR_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-primary pull-right')]")
    CONFIRMAR_BUTTON = (By.XPATH,"//button[contains(@class, 'btn-secondary')]")
    FILE_ARCHIVE = (By.XPATH,"//input[@type='file' or @type='text' or @type='email']")
    GRID = (By.XPATH,"//app-add-flights//table")


    def __init__(self, driver):
     super().__init__(driver)
        
    def seleccionar_menu_archivos(self):
        MENU_ARCHIVOS = self.get_locator_botton('Archivos')
        self.wait_and_click(MENU_ARCHIVOS, self.DEFAULT_WAIT)
        return self
        
    def click_agregar_archivo(self,data):
        self.wait_and_click(self.AGREGAR_ARCHIVO_BUTTON, self.DEFAULT_WAIT)
        dropdown = self.wait_for_element(self.ARCHIVO_DROPDOWN, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['tipo_archivo'])
        self.send_keys(self.AREA,data['descripción'])
        self.upload_file(self.FILE_ARCHIVE,data['ruta'])
        self.wait_and_click(self.AGREGAR_BUTTON, self.DEFAULT_WAIT)
        self.wait_and_click(self.CONFIRMAR_BUTTON, self.DEFAULT_WAIT)
        return self
        
    def validar_grid(self,record_data):
            
            self.validate_record_values_norecord(grid_locator=self.GRID,record_data=record_data)
            return self