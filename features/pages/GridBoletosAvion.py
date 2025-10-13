from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time

class ComisionesBoletosAvionPage(BasePage):
     BOTON_COMISION= (By.XPATH, "//a[contains(text(), 'Comisión')]")
     SELECT_MENUSOL = (By.XPATH, "//*[@id='subenlaces']/app-menu/ul/li[2]/ul")
     BUSCAR_SOL = (By.XPATH, "//input[@id='table-filtering-search']")
     SELECT_AVION = (By.XPATH, "//app-planes-tickets//app-table-data//table//button/img")
     BOTON_AGREGARFAC= (By.XPATH, "//a[contains(text(), 'Comisión')]")
     SELECT_TIPO_VUELO = ()


     def menuBoletosavion(self):
          self.click(self.BOTON_COMISION)
          time.sleep(1)
          self.click(self.SELECT_MENUSOL)


     def buscar_comisionBoletosAvion(self, ID_SOL):
          self.send_keys(self.BUSCAR_SOL, ID_SOL)   
          self.click(self.SELECT_AVION)
          time.sleep(30)

     def AgregarNuevaFactura(self):
          self.click(self.BOTON_AGREGARFAC)
          