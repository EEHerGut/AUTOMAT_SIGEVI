from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import pyautogui
import time

class ComisionesBoletosAvionPage(BasePage):
     BOTON_COMISION= (By.XPATH, "//a[contains(text(), 'Comisión')]")
     SELECT_MENUSOL = (By.XPATH, "//*[@id='subenlaces']/app-menu/ul/li[2]/ul")
     BUSCAR_SOL = (By.XPATH, "//input[@id='table-filtering-search']")
     SELECT_AVION = (By.XPATH, "//app-planes-tickets//app-table-data//table//button/img")
     BOTON_AGREGARFAC= (By.XPATH, "//*[@id='body']/main/app-root/app-authorize-tickets/div/div[1]/div/a")
     SELECT_TIPO_VUELO = (By.XPATH, "//app-authorize-tickets//app-contents-data//select[@id='trip']")
     SELECT_ORIGEN = (By.XPATH,"//app-authorize-tickets//app-contents-data//select[@id='rutas']")
     SELECT_DESTINO = (By.XPATH,"//app-authorize-tickets//app-contents-data//select[@id='rutas2']")
     SELECT_AEROLINEA = (By.XPATH,"(//app-authorize-tickets//select[contains(@class, 'form-control')])[4]")
     NUMERO_BOLETO = (By.XPATH,"(//app-authorize-tickets//input[@type='text'])[1]")
     CLAVE = (By.XPATH,"(//app-authorize-tickets//input[@type='text'])[2]")
     FACTURA = (By.XPATH,"(//app-authorize-tickets//input[@type='text'])[3]")
     BOTON_AGREGAR_AVION = (By.XPATH,"(//app-authorize-tickets//app-contents-data//button[contains(text (),'Agregar')])[2]")

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
          pyautogui.click(x=1435, y=485)
          time.sleep(1)
          pyautogui.press("left")
          pyautogui.click(x=1435, y=1000)
          time.sleep(1)
          dropdown = self.wait_for_element(self.SELECT_ORIGEN,self.LONG_WAIT)
          Select(dropdown).select_by_visible_text(data["origen"])
          time.sleep(1)
          dropdown = self.wait_for_element(self.SELECT_DESTINO,self.LONG_WAIT)
          Select(dropdown).select_by_visible_text(data["destino"])
          time.sleep(1)
          dropdown = self.wait_for_element(self.SELECT_AEROLINEA,self.LONG_WAIT)
          Select(dropdown).select_by_visible_text(data["aerolinea"])
          time.sleep(1)
          self.send_keys(self.NUMERO_BOLETO,data["num_boleto"])
          time.sleep(1)
          self.send_keys(self.CLAVE,data["clave"])
          time.sleep(1)
          pyautogui.click(x=1435, y=850)
          pyautogui.press("left")
          time.sleep(1)
          self.send_keys(self.FACTURA,data["factura"])  
          time.sleep(1)
          self.click(self.BOTON_AGREGAR_AVION)
          time.sleep(30)