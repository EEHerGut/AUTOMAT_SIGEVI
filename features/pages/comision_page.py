from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from utils.logger import global_logger as logger
import time


class ComisionPage(BasePage):
    # Element locators - crear solicitud
    BOTON_NUEVA_SOLICITUD = (By.XPATH, "//app-commissions//button[contains(text(), 'Crear') or contains(text(), ' Nueva solicitud ')]")
    TITULO_FORMULARIO = (By.XPATH, "//h4[contains(text(), 'Solicitud de comisión')]")
    CHECKBOX_ANTICIPO = (By.ID, "check2")
    CHECKBOX_ANTICIPO_1 = (By.ID, "check")
    CAMPO_EXPEDIENTE = (By.XPATH, "//input[@id='numExp']")
    DROPDOWN_TIPO_COMISION = (By.ID, "commissionType")
    DROPDOWN_MEDIO_TRANSPORTE = (By.ID, "transportMeans")
    CAMPO_FECHA_SALIDA = (By.ID, "exitDate")
    CAMPO_FECHA_REGRESO = (By.ID, "returnDate")
    CAMPO_EDFQA = (By.ID, "memberExp")
    DROPDOWN_AREA_GASTO = (By.XPATH, "//select[@formcontrolname='expenditureArea']")
    CAMPO_OBJETIVO = (By.ID, "objective")
    BOTON_GUARDAR = (By.XPATH, "//app-new-commission//button[contains(text(), 'Guardar') or contains(text(), 'Guardar')]")
    BOTON_CONFIRMAR_GUARDAR = (By.XPATH, "//*[@id='confirmModal']/div/div/div[3]/button[2]")
    MODAL_EXITO = (By.XPATH, "//*[@id='resultModal']/div/div/div[1]/h4")
    BOTON_CERRAR_MODAL = (By.XPATH, "//*[@id='resultModal']/div/div/div[3]/button")
    INPUT_DIAS = (By.XPATH,"//input[@type='number' and @formcontrolname='daysAvailable']")
    NUMERO_OFICIO = (By.XPATH,"//input[@formcontrolname='officeNumber']")
    EXPEDIENTE_AUTORIZA=(By.XPATH,"//input[@formcontrolname='authorizerExp']")
    PDF_INPUT =(By.XPATH,"//input[@formcontrolname='officeFile']")
    TIPO_MONEDA =(By.XPATH,"//app-new-commission//li[6]/select")
    # Element locators - editar solicitud
    MENU_SOLICITUD =  (By.XPATH, "//a[contains(text(), 'Solicitud')]")
    BOTON_ACTU_ACTUALIZAR = (By.XPATH, "//button[contains(text(), 'Actualizar') or @aria-label='Hola']")
    BOTON_ACTU_ACEPTAR = (By.XPATH, "//app-edit-commission//button[contains(text(), 'Confirmar') or contains(text(), 'Aceptar')]")
    BOTON_ACTU_CERRAR = (By.XPATH, "//button[normalize-space(text())='Cerrar']") 
    GRID  = (By.XPATH, "//table[contains(@class, 'table-striped') and contains(@class, 'clsTable')]")
    MUNDO =(By.XPATH,"//table//tr[1]/td[3]//img")

    def click_nueva_solicitud(self):
        """Hace clic en el botón de nueva solicitud"""
        self.wait_for_element(self.BOTON_NUEVA_SOLICITUD,self.LONG_WAIT)
        self.click(self.BOTON_NUEVA_SOLICITUD)
        self.find_element(self.TITULO_FORMULARIO)

    def verificar_formulario_visible(self):
        """Verifica que el formulario de solicitud es visible"""
   
        titulo = self.get_text(self.TITULO_FORMULARIO)
        assert titulo == "Solicitud de comisión", f"Se esperaba 'Solicitud de comisión' pero se encontró '{titulo}'"

    def completar_campos_obligatorios(self, solicitud):
        """Completa los campos obligatorios del formulario"""
        # Configurar anticipo
        

        self.set_checkbox(self.CHECKBOX_ANTICIPO, solicitud["anticipo"] == "No")
        # Completar otros campos
        self.send_keys(self.CAMPO_EXPEDIENTE, solicitud["expediente"])
        num_dias=self.get_input_value(self.INPUT_DIAS,self.LONG_WAIT)
        logger.info(f"[SUCCESS] [OK] NÚMERO DIAS DISPONIBLES: {num_dias}")

        if num_dias == "0" :
            PATH_PDF = r"C:/Users/Lenovo/Downloads/Recibo.pdf"
            self.upload_file(self.PDF_INPUT,PATH_PDF)
            time.sleep(2)
            self.send_keys(self.EXPEDIENTE_AUTORIZA, solicitud["ex_autoriza"])
            time.sleep(2)
            self.send_keys(self.NUMERO_OFICIO, solicitud["num_oficio"])
            time.sleep(2)
            logger.info(f"[SUCCESS] [OK] NÚMERO DIAS DISPONIBLES: {num_dias}")
         
    
        tipo_comisión=solicitud["tipo_comision"]
        dropdown = self.wait_for_element(self.DROPDOWN_TIPO_COMISION, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(tipo_comisión)
        time.sleep(1)
        if(tipo_comisión=='INTERNACIONAL'):
             dropdown = self.wait_for_element(self.TIPO_MONEDA, self.LONG_WAIT)
             Select(dropdown).select_by_visible_text(solicitud["tipo_moneda"])
        dropdown = self.wait_for_element(self.DROPDOWN_MEDIO_TRANSPORTE, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(solicitud["transporte"])
        time.sleep(1)
        self.send_keys(self.CAMPO_FECHA_SALIDA, solicitud["fecha_salida"])
        time.sleep(1)
        self.send_keys(self.CAMPO_FECHA_REGRESO, solicitud["fecha_regreso"])
        time.sleep(1)
        self.send_keys(self.CAMPO_EDFQA, solicitud["expediente_autoriza"])
        time.sleep(1)
        self.select_by_value(self.DROPDOWN_AREA_GASTO, solicitud["area_gasto"])
        time.sleep(1)
        self.send_keys(self.CAMPO_OBJETIVO, solicitud["objetivo"])
        time.sleep(1)
            
      

    def guardar_solicitud(self):
        """Guarda la solicitud y confirma la acción"""
        self.wait_and_click(self.BOTON_GUARDAR, self.DEFAULT_WAIT)
        time.sleep(5)
        self.wait_and_click(self.BOTON_CONFIRMAR_GUARDAR, self.DEFAULT_WAIT)
        self.click(self.BOTON_CERRAR_MODAL)
        return self
    
### Editar solicitud
    def seleccionar_menu_solicitud(self):
        self.wait_and_click(self.get_locator_botton('Solicitud'), self.DEFAULT_WAIT)
        return self
       
    def editar_solicitud(self,solicitud):
        time.sleep(3)
        self.set_checkbox(self.CHECKBOX_ANTICIPO_1, solicitud["anticipo"])
        time.sleep(1)

        self.send_keys(self.CAMPO_FECHA_SALIDA, solicitud["data"])
        time.sleep(1)
        self.send_keys(self.CAMPO_FECHA_REGRESO, solicitud["data2"])
        time.sleep(1)
        
        self.wait_and_click(self.BOTON_ACTU_ACTUALIZAR, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_ACTU_ACEPTAR, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_ACTU_CERRAR, self.DEFAULT_WAIT)
        time.sleep(2)
        return self
    
    def validar_grid(self,record_data):
         
         self.validate_record_values(grid_locator=self.GRID,record_data=record_data)
         return self

