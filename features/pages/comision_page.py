from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ComisionPage(BasePage):
    # Element locators
  
    BOTON_NUEVA_SOLICITUD = (By.XPATH, "//app-commissions//button[contains(text(), 'Crear') or contains(text(), ' Nueva solicitud ')]")
    TITULO_FORMULARIO = (By.XPATH, "//h4[contains(text(), 'Solicitud de comisión')]")
    CHECKBOX_ANTICIPO = (By.ID, "check2")
    CAMPO_EXPEDIENTE = (By.ID, "numExp")
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



    def click_nueva_solicitud(self):
        """Hace clic en el botón de nueva solicitud"""
        self.click(self.BOTON_NUEVA_SOLICITUD)
        self.find_element(self.TITULO_FORMULARIO)

    def verificar_formulario_visible(self):
        """Verifica que el formulario de solicitud es visible"""
        titulo = self.get_text(self.TITULO_FORMULARIO)
        assert titulo == "Solicitud de comisión", f"Se esperaba 'Solicitud de comisión' pero se encontró '{titulo}'"

    def completar_campos_obligatorios(self, solicitud):
        """Completa los campos obligatorios del formulario"""
        # Configurar anticipo
        time.sleep(3)
        self.set_checkbox(self.CHECKBOX_ANTICIPO, solicitud["con_anticipo"] == "No")

        # Completar otros campos
        self.send_keys(self.CAMPO_EXPEDIENTE, solicitud["expediente"])
        self.select_by_visible_text(self.DROPDOWN_TIPO_COMISION, solicitud["tipo_comision"])
        self.select_by_visible_text(self.DROPDOWN_MEDIO_TRANSPORTE, solicitud["transporte"])
        self.send_keys(self.CAMPO_FECHA_SALIDA, solicitud["fecha_salida"])
        self.send_keys(self.CAMPO_FECHA_REGRESO, solicitud["fecha_regreso"])
        self.send_keys(self.CAMPO_EDFQA, solicitud["expediente_autoriza"])
        self.select_by_value(self.DROPDOWN_AREA_GASTO, solicitud["area_gasto"])
        self.send_keys(self.CAMPO_OBJETIVO, solicitud["objetivo"])

    def guardar_solicitud(self):
        """Guarda la solicitud y confirma la acción"""
        self.wait_and_click(self.BOTON_GUARDAR, self.DEFAULT_WAIT)
        self.wait_and_click(self.BOTON_CONFIRMAR_GUARDAR, self.DEFAULT_WAIT)
        return self

    def verificar_creacion_exitosa(self):
        """Verifica que la solicitud se creó correctamente"""
        mensaje_exito = self.get_text(self.MODAL_EXITO).lower()
        assert "operación exitosa" in mensaje_exito, f"Se esperaba 'Operación exitosa' pero se encontró: '{mensaje_exito}'"
        self.click(self.BOTON_CERRAR_MODAL)