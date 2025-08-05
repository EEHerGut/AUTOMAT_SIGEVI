from asyncio import timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import (NoSuchElementException, 
                                      StaleElementReferenceException,
                                      TimeoutException)
import time
import logging




class AllPage(BasePage):

  def __init__(self, driver):
        super().__init__(driver)

       # Locators
        self.GRID_TITLE = (By.XPATH, "//*[@id='body']/main/app-root/app-commissions/div/div/h1")
        self.SEARCH_FIELD = (By.ID, "table-filtering-search")
        self.BOTON_ESTADO = lambda estado: (By.XPATH, f"//button[contains(text(), '{estado}')]")


  def menu_comision(self):
         
         locator = (By.XPATH, "//a[contains(text(), 'Comisión')]")
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
            ).click()
    
         locator = (By.XPATH, "//a[contains(text(), 'Comisiones')]")
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
         
  def buscar_comision(self, numero_comision):
        """Busca una comisión por su número"""
        try:
            search_field = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.SEARCH_FIELD)
            )
            search_field.clear()
            search_field.send_keys(numero_comision)
            logging.info(f"Búsqueda realizada para comisión: {numero_comision}")
            return True
        except Exception as e:
            logging.error(f"Error al buscar comisión: {str(e)}")
            self.driver.save_screenshot("error_busqueda_comision.png")
            return False
     
  def seleccionar_comision(self, estado_esperado):
    
        boton = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(self.BOTON_ESTADO(estado_esperado))
            )
        boton.click()

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
  
  def validar_texto_boton(self, locator, texto_esperado, timeout=15, exact_match=True):
        """
        Valida el texto de un botón contra el texto esperado
        
        Args:
            locator (tuple): Locator del botón (By, selector)
            texto_esperado (str): Texto que se espera encontrar
            timeout (int): Tiempo máximo de espera en segundos
            exact_match (bool): True para coincidencia exacta, False para parcial
            
        Returns:
            bool: True si el texto coincide, False si no
        """
        try:
            # Esperar a que el botón esté presente y visible
            boton = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            
            # Obtener texto del botón
            texto_actual = boton.text.strip()
            
            # Realizar comparación
            if exact_match:
                coincide = texto_actual == texto_esperado
            else:
                coincide = texto_esperado.lower() in texto_actual.lower()
            
            if not coincide:
                logging.warning(f"Texto no coincide. Esperado: '{texto_esperado}', Actual: '{texto_actual}'")
                return False
                
            logging.info(f"Texto del botón validado correctamente: '{texto_actual}'")
            return True
            
        except TimeoutException:
            logging.error(f"Botón no encontrado con locator: {locator}")
            self.driver.save_screenshot("error_boton_no_encontrado.png")
            return False
        except Exception as e:
            logging.error(f"Error inesperado validando botón: {str(e)}")
            return False
        
  def validar_texto_boton_por_xpath(self, xpath, texto_esperado, **kwargs):
        """Valida texto de botón localizado por XPath"""
        return self.validar_texto_boton((By.XPATH, xpath), texto_esperado, **kwargs)
    
  def validar_texto_boton_por_id(self, id, texto_esperado, **kwargs):
        """Valida texto de botón localizado por ID"""
        return self.validar_texto_boton((By.ID, id), texto_esperado, **kwargs)
    
  def validar_texto_boton_por_texto(self, texto, exact_match=True, **kwargs):
        """
        Valida botón que contiene cierto texto
        Ejemplo: <button>Guardar</button>
        """
        operador = "=" if exact_match else "contains"
        xpath = f"//button[{operador}(text(), '{texto}')]"
        return self.validar_texto_boton((By.XPATH, xpath), texto, **kwargs)

  def seleccionar_dropdown_con_reintentos(self, locator, valor, max_reintentos=3, delay=2):
        """
        Método robusto para seleccionar opciones en dropdowns con reintentos
        
        Args:
            locator: Tupla (By, selector) del elemento dropdown
            valor: Texto de la opción a seleccionar
            max_reintentos: Número máximo de intentos
            delay: Tiempo de espera entre intentos (segundos)
        """
        for intento in range(1, max_reintentos + 1):
            try:
                dropdown = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                select = Select(dropdown)
                
                if len(select.options) > 1:
                    select.select_by_visible_text(valor)
                    logging.info(f"Opción '{valor}' seleccionada en dropdown {locator}")
                    return True
                
                logging.warning(f"Intento {intento}: Dropdown vacío. Recargando...")
                dropdown.click()
                time.sleep(delay)
                
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
                logging.warning(f"Intento {intento} fallido: {str(e)}")
                if intento == max_reintentos:
                    self._tomar_screenshot("dropdown_fallido")
                    raise Exception(f"No se pudo cargar el dropdown {locator} después de {max_reintentos} intentos")
                time.sleep(delay)
                
  def refresh_page(self):
        self.driver.refresh()
        self.driver.execute_script("document.body.style.zoom='80%'")
    