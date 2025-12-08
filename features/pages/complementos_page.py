from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select
import time
import pyautogui


class ComplementosPage(BasePage):
    # Locators for Vuelos section
    BOTON_ALTA_COMPLEMENTO = (By.XPATH, "//app-commission-complement//button[contains(text(), 'Alta de Complemento')]")
    BOTON_ALTA = (By.XPATH, "//app-commission-complement//button[contains(text(), 'Alta de complemento')]")
    BOTON_CONFIRMAR = (By.XPATH, "//app-modal-confirm-add//button[2]")
    BOTON_CONFIRMAR_2 = (By.XPATH, "//app-modal-add-ok//div[@class='modal-footer']//button")
    BOTON_CONFIRMAR_123 = (By.XPATH, "//app-modal-confirm-add//div[@class='modal-footer']//button[2]")
    BOTON_AGREGAR_IMP = (By.XPATH, "//app-table-complement-favor-de//button[contains(text(), 'Agregar')]")
    BOTON_ACEPTAR_IMPUESTO = (By.XPATH, "//app-table-complement-favor-de//form//button")
    BOTON_MODAL_IMPUESTO =(By.XPATH, "//app-modal-confirm-tax//div[@class='modal-footer']//button[2]")
    BOTON_CONFIRMAR_IMPUESTO=(By.XPATH, "//app-modal-ok//div[@class='modal-footer']//button")
    FACTURA= (By.XPATH, "//app-commission-complement//input[@id='archivoPDF']")
    XML= (By.XPATH, "//app-commission-complement//input[@id='archivoXML']")
    CONCEPTO = (By.XPATH, "//app-commission-complement//select[@id='conceptNew']")
    CONCEPTO_IMPUESTO = (By.XPATH, "//app-table-complement-favor-de//select[@id='concept']")
    IMPORTE_IMPUESTO=(By.XPATH, "//app-table-complement-favor-de//input[@id='amount']") 
    IMPORTE=(By.XPATH, "//app-commission-complement//input[@placeholder]") 
    TEXT_AREA=(By.XPATH, "//app-commission-complement//textarea[@id='detalle']") 
    ##Autorizar Complemento
    BOTON_REGISTRADO=(By.XPATH, "//app-table-complement-favor-de//button[contains(text(), 'Registrado')]")
    BOTON_AUTORIZAR_COMPLEMENTO =(By.XPATH, "//app-table-favor-detalle//a[contains(text(), 'Autorizar complemento')]")
    BOTON_CONFIRMAR_COMPLEMENTO=(By.XPATH, "//app-table-favor-detalle//button[contains(text(), 'Confirmar')]")
   

    ##Reembolso al comisionado
    BOTON_REEMBOLSO=(By.XPATH, "//app-table-favor-detalle//a[contains(text(), 'Reem')]")
    BOTON_SOLICITAR_REEMBOLSO=(By.XPATH, "//app-table-favor-detalle//button[contains(text(), 'Solicitar')]")
    
    
    ##MODALACEPTAR
    BOTON_ACEPTAR=(By.XPATH, "//app-modal-ok-cargo//button[contains(text(), 'Aceptar')]")

    ##BAJA COMPLEMENTO
    BOTON_TRASH=(By.XPATH, "//app-table-complement-favor-de//ul/li/a") 
    BOTON_TRASH_ACEPTAR =(By.XPATH, "//app-modal-confirm-delete//div[@class='modal-footer']//button[2]") 

   

    def __init__(self, driver):
     super().__init__(driver)
        
    def seleccionar_menu_complementos(self):
        
        self.wait_and_click(self.get_locator_botton('Complementos'), self.DEFAULT_WAIT)
        return self
     
    def alta_complemento(self):
        
        self.wait_and_click(self.BOTON_ALTA_COMPLEMENTO, self.DEFAULT_WAIT)
        return self
    
    def baja_complemento(self):
        
        self.wait_and_click(self.BOTON_TRASH, self.DEFAULT_WAIT)
        time.sleep(.8)
        self.wait_and_click(self.BOTON_TRASH_ACEPTAR, self.DEFAULT_WAIT)
        time.sleep(.8)
        self.wait_and_click(self.BOTON_ACEPTAR, self.DEFAULT_WAIT)
        return self
        
    def agregar_formulario(self,data,data1,paths):


        self.upload_file(self.FACTURA,paths['PATH_PDF'])
        self.upload_file(self.XML,paths['PATH_XML'])
        self.wait_for_element(self.CONCEPTO,self.LONG_WAIT)
        dropdown = self.wait_for_element(self.CONCEPTO, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data['concepto'])
        self.send_keys(self.IMPORTE,data['importe'])
        self.send_keys(self.TEXT_AREA,data['motivo'])
      
        time.sleep(1)
        self.wait_and_click(self.BOTON_ALTA,self.DEFAULT_WAIT)
        time.sleep(.9)
        self.wait_and_click(self.BOTON_CONFIRMAR,self.DEFAULT_WAIT)
        time.sleep(.9)
        self.wait_and_click(self.BOTON_CONFIRMAR_2,self.DEFAULT_WAIT)

        time.sleep(1)
        self.wait_and_click(self.BOTON_AGREGAR_IMP,self.DEFAULT_WAIT)
        
        self.wait_for_element(self.CONCEPTO_IMPUESTO,self.LONG_WAIT)
        dropdown = self.wait_for_element(self.CONCEPTO_IMPUESTO, self.LONG_WAIT)
        Select(dropdown).select_by_visible_text(data1['concepto'])
        self.send_keys(self.IMPORTE_IMPUESTO,data1['monto_impuesto'])
        self.wait_and_click(self.BOTON_ACEPTAR_IMPUESTO,self.DEFAULT_WAIT)
        time.sleep(1)
        self.wait_and_click(self.BOTON_MODAL_IMPUESTO,self.DEFAULT_WAIT)
        time.sleep(1)
        self.wait_and_click(self.BOTON_CONFIRMAR_IMPUESTO,self.DEFAULT_WAIT)
    
        return self


    def validar_grid(self,record_data):
            
            self.validate_record_values_norecord(grid_locator=self.GRID,record_data=record_data)
            return self

        
##-------------------------------Autorizar complemento-----------------------##


    def seleccionar_complemento(self):
            time.sleep(2)
            self.wait_and_click(self.BOTON_REGISTRADO,self.DEFAULT_WAIT)
            return self
    
    def autorizar_complemento(self):
            time.sleep(1)
            self.wait_and_click(self.BOTON_AUTORIZAR_COMPLEMENTO,self.DEFAULT_WAIT)
            time.sleep(1)
            self.wait_and_click(self.BOTON_CONFIRMAR_COMPLEMENTO,self.DEFAULT_WAIT)
            time.sleep(1)
            self.wait_and_click(self.BOTON_ACEPTAR,self.DEFAULT_WAIT) 
            return self
    
##-------------------------------Reembolso al comisionado-----------------------##