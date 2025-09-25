from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import (NoSuchElementException, 
                                      StaleElementReferenceException,
                                      TimeoutException)
from utils.logger import global_logger as logger
import logging
import time




class AllPage(BasePage):

  def __init__(self, driver):
        super().__init__(driver)

       # Locators
        self.GRID_TITLE = (By.XPATH, "//*[@id='body']/main/app-root/app-commissions/div/div/h1")
        self.SEARCH_FIELD = (By.ID, "table-filtering-search")
        self.BOTON_ESTADO = lambda estado: (By.XPATH, f"//button[contains(text(), '{estado}')]")
        self.BOTON_COMISION= (By.XPATH, "//a[contains(text(), 'Comisión')]")
        self.BOTON_COMISIONES= (By.XPATH, "//a[contains(text(), 'Comisiones')]")
        self.ETIQUETA_COMISION= (By.XPATH, "//h1[contains(text(), 'Comisiones')]")
        self.MUNDO =(By.XPATH,"//table//tr[1]/td[3]//img")
        self.ANTICIPO =(By.XPATH,"//table[contains(@class, 'table')]//tr/td[5]//img")
        self.BOTON_AVION=(By.XPATH,"//table//tr[1]//td[position()=6]//i")


  def menu_comision(self):
    self.zoom_page()
    if self.es_elemento_visible("//h1[contains(text(), 'Comisiones')]"):
          logger.info(f"✅✅✅✅✅Elemento: es visible")
    else:
          logger.error(f"❌❌❌❌❌❌ El elemento NO existe en el DOM")
          self.wait_for_element(self.BOTON_COMISION, self.LONG_WAIT)
          self.wait_and_click(self.BOTON_COMISION, self.DEFAULT_WAIT)
          self.wait_and_click(self.BOTON_COMISIONES, self.DEFAULT_WAIT)

     
        
    """   elemento = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.ETIQUETA_COMISION)
            )
        

        logger.info(f"🚀🚀🚀🚀🚀🚀🚀🚀 Elemento: {elemento.text}")
        logger.info(f"🚀🚀🚀🚀🚀🚀🚀🚀 Elemento: {elemento.is_displayed}")
        
        if elemento.is_displayed():
            self.wait_for_element(self.BOTON_COMISION, self.LONG_WAIT)
        else:
            self.wait_for_element(self.BOTON_COMISION, self.LONG_WAIT)
            self.wait_and_click(self.BOTON_COMISION, self.DEFAULT_WAIT)
            self.wait_and_click(self.BOTON_COMISIONES, self.DEFAULT_WAIT)

        return self"""
  
  def buscar_comision(self, numero_comision):
        """Busca una comisión por su número"""
        logger.info(f"✅✅✅✅✅Busca una comisión por su número")
        try:
            self.wait_for_element(self.SEARCH_FIELD, self.LONG_WAIT)
            self.send_keys(self.SEARCH_FIELD,numero_comision)
            time.sleep(0.5)
            logging.info(f"Búsqueda realizada para comisión: {numero_comision}")
            return True
        except Exception as e:
            logging.error(f"Error al buscar comisión: {str(e)}")
            self.driver.save_screenshot("error_busqueda_comision.png")
            return False
     
  def seleccionar_comision(self, estado_esperado):
        self.wait_for_element(self.BOTON_ESTADO(estado_esperado),self.LONG_WAIT)
        self.wait_and_click(self.BOTON_ESTADO(estado_esperado), self.DEFAULT_WAIT)

  def seleccionar_boleto(self):
        self.wait_and_click(self.BOTON_AVION)


  def validar_registro_tabla(self, datos_esperados, locator_tabla, timeout=15):
        """
        Valida que un registro exista en una tabla con los valores esperados
        
        Args:
            datos_esperados (dict): Diccionario con {columna: valor} a validar
            locator_tabla (str): XPath de la tabla (opcional)
            timeout (int): Tiempo máximo de espera
            
        Returns:
            bool: True si se encuentra el registro, False si no
        """
        try:
            # Esperar a que la tabla esté visible
            tabla = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator_tabla))
            )
            
            # Construir XPath para buscar el registro
            xpath_busqueda = self._construir_xpath_busqueda(datos_esperados)
            
            # Buscar el registro
            registro = WebDriverWait(tabla, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath_busqueda))
            )
            
            logging.info(f"Registro encontrado: {registro.text}")
            return True
            
        except TimeoutException:
            logging.error(f"No se encontró el registro con datos: {datos_esperados}")
            self.driver.save_screenshot("error_validacion_tabla.png")
            return False
        
  def _construir_xpath_busqueda(self, datos_esperados):
        """Construye XPath dinámico basado en los datos esperados"""
        condiciones = []
        for columna, valor in datos_esperados.items():
            # XPath para celda que contiene el texto de la columna
            condiciones.append(f".//td[contains(., '{valor}')]")
        
        # Unir todas las condiciones con AND lógico
        return " | ".join(condiciones) if len(condiciones) > 1 else condiciones[0]
                
  def refresh_page(self):
        self.driver.refresh()
        self.driver.execute_script("document.body.style.zoom='80%'")
   
  def validar_tipo_comisión(self):
        try:
            self.wait_and_click(self.MUNDO, 2)
            variable ="INTERNACIONAL"
            return variable
        except TimeoutException  :
            variable="MACIONAL"
            return variable

  def validar_anticipo(self):
         try:
            self.wait_and_click(self.ANTICIPO, 2)
            variable ="CON ANTICIPO"
            return variable
         except TimeoutException  :
            variable="SIN ANTICIPO"
            return variable
         



    