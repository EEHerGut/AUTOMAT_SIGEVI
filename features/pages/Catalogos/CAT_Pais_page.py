from selenium.webdriver.common.by import By
from ..base_page import BasePage
from selenium.common.exceptions import TimeoutException
from features.locators.botones_comunes import BotonesComunes 
import time

class PaisPage(BasePage):

    #LOCATORS
    #Alta de pais
    BOTON_NUEVOPAIS = (By.XPATH, "//a[contains(text(), 'Nuevo')]") 
    INPUT_PAIS = (By.XPATH, "//input[@placeholder='País']")
  
    BOTON_CREARPAIS=  (By.XPATH, "//button[@class='btn btn-primary pull-right']") 
    BOTON_CONFIRMAR = (By.XPATH, "//app-confirm-modal//button[contains(text(), 'Aceptar')]") 
    BOTON_CONF = (By.XPATH, "//app-confirm-modal//button[contains(@class, 'btn btn-primary h5')]") 
    GRID = (By.XPATH, "//table[@class='table table-striped table-hover clsTable']") 

    #editar pais
    BOTON_MODIFICAR = (By.XPATH, "(//a[contains(@class, 'editOption')])[1]")  

    def __init__(self, driver):
        super().__init__(driver)


    def click_agregar_pais(self):
      
        try:
            self.wait_and_click(self.BOTON_NUEVOPAIS, 2)
            return self
        except TimeoutException  :
            self.wait_and_click(self.BOTON_NUEVOPAIS, self.DEFAULT_WAIT)
            return self
        
    def guardar_pais(self,data):
        
        time.sleep(2)
        self.send_keys(self.INPUT_PAIS, data["nombre_pais"])
        time.sleep(1)
        self.click(BotonesComunes.BOTON_CREARPAIS)
        time.sleep(1)
        self.click(BotonesComunes.BOTON_CONFIRMAR)
        time.sleep(1)
        self.click(BotonesComunes.BOTON_CONF)
        return self
    
    def validar_grid(self,record_data):
         self.validate_record_values_norecord(grid_locator=BotonesComunes.GRID,record_data=record_data)
         return self
    
    #EDITAR pais
    def editar_pais(self,data):
        self.wait_and_click(BotonesComunes.BOTON_MODIFICAR,self.DEFAULT_WAIT)
        self.send_keys(self.INPUT_PAIS,data)
        self.wait_and_click(BotonesComunes.BOTON_CREAR,self.DEFAULT_WAIT)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(3)
        self.wait_and_click(BotonesComunes.BOTON_CONF,self.DEFAULT_WAIT)

        return self
    
    #activar/desactivar PAIS
    def act_pais(self):
        self.wait_and_click(BotonesComunes.SWITCH,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONF,self.DEFAULT_WAIT)
        return self
    