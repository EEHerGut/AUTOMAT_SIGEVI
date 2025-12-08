from selenium.webdriver.common.by import By
from ..base_page import BasePage
from selenium.common.exceptions import TimeoutException
from features.locators.botones_comunes import BotonesComunes 
import time

class MonedaPage(BasePage):

    #LOCATORS
    #Alta de moneda
    BOTON_NUEVAMONEDA = (By.XPATH, "//a[contains(text(), 'Nueva')]")
    INPUT_MONEDA = (By.XPATH, "//input[@placeholder='Moneda']")
    INPUT_CAMBIO = (By.XPATH, "//input[@placeholder='Tipo cambio']")
 

    def __init__(self, driver):
        super().__init__(driver)


    def click_agregar_moneda(self):
      
        try:
            self.wait_and_click(self.BOTON_NUEVAMONEDA, 2)
            return self
        except TimeoutException  :
            self.wait_and_click(self.BOTON_NUEVAMONEDA, self.DEFAULT_WAIT)
            return self
        
    def guardar_moneda(self,data):
        
        time.sleep(2)
        self.send_keys(self.INPUT_MONEDA, data["nombre_moneda"])
        time.sleep(1)
        self.send_keys(self.INPUT_CAMBIO, data["tipo_cambio"])
        time.sleep(1)
        self.wait_and_click(BotonesComunes.BOTON_CREAR, self.DEFAULT_WAIT)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR, self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONF, self.DEFAULT_WAIT)
        return self
    
    def validar_grid(self,record_data):
         self.validate_record_values_norecord(grid_locator=BotonesComunes.GRID,record_data=record_data)
         return self
    
    
        #EDITAR Moneda
    def editar_moneda(self,data):
        self.wait_and_click(BotonesComunes.BOTON_MODIFICAR,self.DEFAULT_WAIT)
        self.send_keys(self.INPUT_MONEDA,data["nombre_moneda_m"])
        self.send_keys(self.INPUT_CAMBIO,data["tipo_cambio_m"])
        self.wait_and_click(BotonesComunes.BOTON_CREAR,self.DEFAULT_WAIT)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(3)
        self.wait_and_click(self.BOTON_CONF,self.DEFAULT_WAIT)

        return self
    
    #activar/desactivar moneda
    def act_moneda(self):
        self.wait_and_click(BotonesComunes.SWITCH,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONF,self.DEFAULT_WAIT)
        return self
    