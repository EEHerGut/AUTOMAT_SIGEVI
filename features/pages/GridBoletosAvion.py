from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time

class AviónPage(BasePage):
     BOTON_NUEVOREGISTRO = (By.XPATH, "//app-authorize-tickets//a[contains(text(), 'Nuevo')]")
     TIPO_VUELO = (By.XPATH,"//app-authorize-tickets//select[@id='trip']")
     SALIDA =(By.XPATH,"//input[not(@id) and @formControlName='fechaInicial']")
     REGRESO=(By.XPATH,"//input[not(@id) and @formControlName='fechaFinal']")
     ORIGEN =(By.XPATH,"//app-authorize-tickets//select[@formControlName and @id='rutas']")
     DESTINO=(By.XPATH,"//app-authorize-tickets//select[@formControlName and @id='rutas2']")
     AEROLINEA=(By.XPATH,"//app-authorize-tickets//select[@formControlName='aerolinea']")
     NUMEROBOLETO=(By.XPATH,"//app-authorize-tickets//input[@formControlName='numeroBoleto']")
     CLAVE=(By.XPATH,"//app-authorize-tickets//input[@formControlName='clave']")
     FECHAFACTURA=(By.XPATH,"//input[not(@id) and @formControlName='fechaFactura']")
     FACTURA=(By.XPATH,"//app-authorize-tickets//select[@formControlName and @id='rutas2']")
     AGREGAR_BOLETO=(By.XPATH,"//*[@id='addTicket']//button[1]/following-sibling::button[1]")
     