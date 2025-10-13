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
     BOTON_AGREGARFAC= (By.XPATH, "//*[@id='body']/main/app-root/app-authorize-tickets/div/div[1]/div/a")
     SELECT_TIPO_VUELO = (By.XPATH, "//app-authorize-tickets//app-contents-data//select[@id='trip']")


     def menuBoletosavion(self):
          self.click(self.BOTON_COMISION)
          time.sleep(1)
          self.click(self.SELECT_MENUSOL)


     def buscar_comisionBoletosAvion(self, ID_SOL):
          self.send_keys(self.BUSCAR_SOL, ID_SOL)   
          self.click(self.SELECT_AVION)
          

     def AgregarNuevaFactura(self,data):
          self.click(self.BOTON_AGREGARFAC)
          dropdown = self.wait_for_element(self.SELECT_TIPO_VUELO, self.LONG_WAIT)
          Select(dropdown).select_by_visible_text(data["tipo_vuelo"])
          
          
          
          time.sleep(30)