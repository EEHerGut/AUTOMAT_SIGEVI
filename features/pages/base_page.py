from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import global_logger as logger
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from config import TIEMPOS_ESPERA
from selenium.webdriver.support.ui import Select
from behave import *
from utils.logger import global_logger as logger
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from features.locators.botones_comunes import BotonesComunes
import time


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.DEFAULT_WAIT = TIEMPOS_ESPERA['DEFAULT_WAIT']
        self.LONG_WAIT = TIEMPOS_ESPERA['LONG_WAIT']
        self.SHORT_WAIT = TIEMPOS_ESPERA['SHORT_WAIT']
        self.PAGE_MARKER = None  # Sobreescribir en páginas hijas

    
    def is_loaded(self):
        """
        Verifica si la página está completamente cargada.
        DEBE ser sobrescrito por cada página hija.
        """
        if self.PAGE_MARKER is None:
            raise NotImplementedError("Cada página debe definir PAGE_MARKER o sobrescribir is_loaded()")
            
        try:
            return self.is_visible(self.PAGE_MARKER, timeout=self.SHORT_WAIT)
        except TimeoutException:
            return False
        
    def load(self):
        """
        Carga la página y verifica que esté lista.
        """
        if not self.is_loaded():
            self._navigate()
            self.wait.until(lambda _: self.is_loaded(),
                          message=f"La página no se cargó correctamente. Markers: {self.PAGE_MARKER}")
        
    
    def find_element(self, locator):
        """Encuentra un elemento esperando a que sea visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        """Encuentra múltiples elementos"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Hace click en un elemento después de esperar que sea clickeable"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
   


    def send_keys(self, locator, text):
        """Limpia el campo y escribe el texto"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        return self.find_element(locator).text
    
    def is_visible(self, locator, timeout=None):
        """Verifica si un elemento es visible"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    def take_screenshot(self, filename):
        """Toma un screenshot"""
        self.driver.save_screenshot(filename)

    def seleccionar_tipo_vueloselect_by_visible_text(self, locator, text):
        """Selecciona una opción por texto visible en un dropdown"""
        Select(self.find_element(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        """Selecciona una opción por valor en un dropdown"""
        Select(self.find_element(locator)).select_by_value(value)
    
    def upload_file(self, file_input_locator, file_path):
        """Sube un archivo a un input de tipo file"""
        file_input = self.find_element(file_input_locator)
        file_input.send_keys(file_path)
    
    def make_file_input_visible(self, file_input_locator):
        """Hace visible un input file (para casos donde está oculto)"""
        self.driver.execute_script(
        "arguments[0].style.display = 'block';", 
        self.find_element(file_input_locator))
     
    def set_checkbox(self, checkbox_locator, state):
         """Establece el estado de un checkbox (True/False)"""
         checkbox = self.find_element(checkbox_locator)  # Primero obtenemos el elemento
         if (checkbox.is_selected() and not state) or (not checkbox.is_selected() and state):
           checkbox.click()

    def is_checkbox_checked(self, checkbox_locator):
          """Verifica si un checkbox está marcado"""
          return self.find_element(checkbox_locator).is_selected()
    
    def is_element_present(self, locator, timeout=10):
        """Verifica si un elemento está presente en el DOM"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
    

    def clear_and_send_keys(self, locator, text):
            """Limpia un campo y escribe texto"""
            element = self.is_element_presentement(locator)
            element.clear()
            element.send_keys(text)

    def is_logged_in(self):
        try:
            return self.is_visible(self.SESSION_MARKER["UI_MARKER"])
        except:
         return False
        
    def wait_for_element(self, locator, timeout=10):
        """Espera a que un elemento sea visible y lo retorna"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
    
    def wait(self, locator, timeout):
        """Espera a que un elemento sea clickeable"""
        element = self.find_element(locator)
        return element
    
    def es_elemento_visible(self,xpath):
        try:
            elemento = self.driver.find_element(By.XPATH, xpath)
            return elemento.is_displayed()
        except:
            return False
    
    def wait_and_click(self, locator, timeout):
        """Espera a que un elemento sea clickeable y hace click"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        element.click()
        return self
    
    def upload_file_with_verification(self, file_input_locator, file_path, verification_locator=None, timeout=None):
        """Sube un archivo y verifica que se haya cargado correctamente
    Args:
        file_input_locator: Tupla (By, locator) para el input file
        file_path: Ruta absoluta del archivo
        verification_locator: (Opcional) Locator para verificar la carga
        timeout: (Opcional) Tiempo máximo de espera
    Returns:
        bool: True si la carga fue exitosa
        """
        self.upload_file(file_input_locator, file_path)
    
        if verification_locator:
            try:
                wait = WebDriverWait(self.driver, timeout or self.timeout)
                return wait.until(EC.visibility_of_element_located(verification_locator)).is_displayed()
            except:
                return False
        return True
    
    def upload_file(self, file_input_locator, file_path):
        """Sube un archivo a un input de tipo file
    Args:
        file_input_locator: Tupla (By, locator) para el input file
        file_path: Ruta absoluta del archivo a subir
        """
        file_input = self.wait.until(EC.presence_of_element_located(file_input_locator))
        file_input.send_keys(file_path)

    def guardar_registro_comision(self,numero_comision, estado,nac_inter,anticipo,archivo_nombre):
        try:
            directorio = "resultados_1"
            
            # CORRECCIÓN: Crear directorio solo si NO existe
            if not os.path.exists(directorio):
                os.makedirs(directorio)
                print(f"📂 Carpeta creada: {os.path.abspath(directorio)}")
            
            # Verificar permisos (opcional)
            permisos = os.stat(directorio).st_mode
            print(f"🔓 Permisos de la carpeta: {oct(permisos)}")
            
            ruta_archivo = os.path.join(directorio, archivo_nombre)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            lineas = []
            encontrado = False
            
            # Leer archivo si existe
            if os.path.exists(ruta_archivo):
                print(f"📄 Archivo existente encontrado: {ruta_archivo}")
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    lineas = file.readlines()
                
                # Buscar y actualizar línea
                for i, linea in enumerate(lineas):
                    if linea.strip() and not linea.startswith('Timestamp'):
                        partes = linea.strip().split(',')
                        if len(partes) >= 2 and partes[1] == str(numero_comision):
                                lineas[i] = f"{timestamp},{numero_comision},{estado},{nac_inter},{anticipo}\n"
                                encontrado = True
                                print(f"🔄 Registro actualizado: {numero_comision}")
                                break
            
            # Si no se encontró, agregar nueva línea
            if not encontrado:
                print(f"🆕 Nuevo registro: {numero_comision}")
                if not lineas or not lineas[0].startswith('Timestamp'):
                    lineas.insert(0, "Timestamp,Número_Comisión,Estado,Anticipo\n")
                lineas.append(f"{timestamp},{numero_comision},{estado},{nac_inter},{anticipo}\n")
            
            # Escribir todo de vuelta al archivo
            with open(ruta_archivo, 'w', encoding='utf-8') as file:
                file.writelines(lineas)
            
            print(f"✅ Registro {'actualizado' if encontrado else 'creado'}: {numero_comision} - {estado}")
            print(f"📁 Archivo: {ruta_archivo}")
            print(f"📍 Ruta absoluta: {os.path.abspath(ruta_archivo)}")
            
            # Verificar que realmente se creó
            if os.path.exists(ruta_archivo):
                print("🎯 ¡Archivo creado exitosamente!")
            else:
                print("❌ ¡Error: El archivo no se creó!")
                
        except Exception as e:
            print(f"💥 Error crítico: {str(e)}")
            import traceback
            traceback.print_exc()
        
    def validate_record_values(self, grid_locator, record_data, timeout=10):
        """
        Valida múltiples valores de un registro en el grid
        Args:
            record_data: Diccionario con {nombre_columna: valor_esperado}
        Returns:set_checkbox
            bool: True si todos los valores coinciden
        """
        logger.info(f"-------- Recorddata: {record_data}")
        try:
            xpath_parts = []
            for column, value in record_data.items():
                xpath_parts.append(f"td[@data-column='{column}' and contains(., '{value}')]")
            
            full_xpath = f"{grid_locator}//tr[{' and '.join(xpath_parts)}]"
            resultado = self.is_visible((By.XPATH, full_xpath), timeout)
            
            numero_comision = record_data.get('num', 'N/A')
            estado = record_data.get('registro', 'N/A')
            nac_inter=record_data.get('nac/inter', 'N/A')
            anticipo=record_data.get('anticipo', 'N/A')
            resultado="registro_comisiones.txt"
            self.guardar_registro_comision(numero_comision, estado,nac_inter,anticipo,resultado)
            
            return resultado       
        except Exception  as e:
            numero_comision = record_data.get('num', 'N/A')
            estado = 'error'
            resultado="registro_comisiones.txt"
            self.guardar_registro_comision(numero_comision, estado, False)
            return False 
        
    def validate_record_values_norecord(self, grid_locator, record_data, timeout=10):
        """
        Valida que un registro aparezca en el grid
        Args:
            record_data: Puede ser diccionario {columna: valor} o string para buscar en cualquier columna
        """
        if isinstance(record_data, str):
            # Si es string, buscar en cualquier columna
            full_xpath = f"{grid_locator}//tr[td[contains(., '{record_data}')]]"
        else:
            # Si es diccionario, buscar por columnas específicas
            xpath_parts = []
            for column, value in record_data.items():
                xpath_parts.append(f"td[@data-column='{column}' and contains(., '{value}')]")
            full_xpath = f"{grid_locator}//tr[{' and '.join(xpath_parts)}]"
        
        resultado = self.is_visible((By.XPATH, full_xpath), timeout)
        return resultado
        
    def get_input_value(self, locator, timeout=None):
        """
        Obtiene el valor de un input field mediante su locator
        
        Args:
            locator: Tupla (By, locator) del elemento
            timeout: Tiempo opcional de espera (usa el default si es None)
        
        Returns:
            str: Valor del input o cadena vacía si no se encuentra
        """
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            element = wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.get_attribute('value') or ''
        
        except TimeoutException:
            logger.warning(f"[TIMEOUT] Timeout al buscar elemento: {locator}")
            return ''
        except Exception as e:
            logger.error(f"❌ Error al obtener valor del input {locator}: {str(e)}")
            return ''

    def get_locator_botton(self,accion):
         return (By.XPATH, f"//app-details-table-commission//a[contains(@class, '') and contains(text(), '{accion}')]")

    def zoom_page(self):
        self.driver.execute_script("document.body.style.zoom='80%'")


    def is_button_visible(self, locator, by=By.CSS_SELECTOR, timeout=10):
        """
        Verifica si un botón está visible en el DOM
        
        Args:
            locator: Puede ser string o tupla (by, locator)
            by: Tipo de selector (solo si locator es string)
            timeout: Tiempo máximo de espera
        """
        try:
            # Si locator es una tupla, desempaquetar
            if isinstance(locator, tuple) and len(locator) == 2:
                by, locator_value = locator
            else:
                locator_value = locator
                
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator_value))
            )
            # Verificación adicional para asegurar que no es None
            if element is None:
                return False
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
        except Exception as e:
            print(f"Error inesperado en is_button_visible: {e}")
            return False
        
        # === MÉTODOS CRUD GENÉRICOS ===
    
    def click_agregar(self, boton_nuevo_locator):
        """Método genérico para agregar nuevo registro"""
        try:
             self.wait_and_click(boton_nuevo_locator, 2)
        except TimeoutException:
             self.wait_and_click(boton_nuevo_locator,self.DEFAULT_WAIT)
        return self
    
    def guardar_registro(self, campos_data, tiempo_espera=2):
        """Método genérico para guardar cualquier registro"""
        time.sleep(tiempo_espera)
        
        # Llenar campos dinámicamente
        for locator, valor in campos_data.items():
             self.send_keys(locator, valor)
             time.sleep(1)
        
        # Flujo común de guardado
        try:
         self.click(BotonesComunes.BOTON_CREAR)
        except:
            self.click(BotonesComunes.BOTON_CREAR_ESTADO)
            
        time.sleep(1)
        self.click(BotonesComunes.BOTON_CONFIRMAR)
        time.sleep(1)
        self.click(BotonesComunes.BOTON_CONF)
        return self
    
    def validar_grid(self, record_data):
        """Validar registro en grid"""
        self.validate_record_values_norecord(
            grid_locator=BotonesComunes.GRID, 
            record_data=record_data
        )
        return self
    
    def editar_registro(self, campos_data, tiempo_espera=2):
        """Método genérico para editar registro"""
        self.wait_and_click(BotonesComunes.BOTON_MODIFICAR,self.DEFAULT_WAIT)
        time.sleep(tiempo_espera)
        
        # Llenar campos dinámicamente
        for locator, valor in campos_data.items():
             self.send_keys(locator, valor)
        
        try:
         self.click(BotonesComunes.BOTON_CREAR)
        except:
            self.click(BotonesComunes.BOTON_CREAR_ESTADO)
            
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(3)
        self.wait_and_click(BotonesComunes.BOTON_CONF,self.DEFAULT_WAIT)
        return self
    
    def activar_desactivar_registro(self):
        """Método genérico para activar/desactivar"""
        self.wait_and_click(BotonesComunes.SWITCH,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(2)
        self.wait_and_click(BotonesComunes.BOTON_CONF,self.DEFAULT_WAIT)
        return self
    
    
