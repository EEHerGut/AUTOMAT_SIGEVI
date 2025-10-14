from behave import *
from pages.GridBoletosAvion import ComisionesBoletosAvionPage
from config import ID_SOLICITUD
from config import ID_FACTURA
from pages.all_page import AllPage
import time


@given('Buscar y seleccionar solicitud Boletos de Avion')
def step_impl(context):
    context.all_page = AllPage(context.driver)
    context.comisionesBA = ComisionesBoletosAvionPage(context.driver)
    context.comisionesBA.menuBoletosavion()
    context.comisionesBA.buscar_comisionBoletosAvion(ID_SOLICITUD)

 
@given('Seleccionar y Capturar Nuevo Boleto de Avión')
def step_impl(context):
    data = context.data["formularios"]['ALTA_BOLETO_AVION']
    context.comisionesBA.AgregarNuevaFactura(data)
    

@then('Validar el boleto genere la factura correctamente')

def step_impl(context,estatus):  
    assert context.reembolsar.validar_grid(), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 
