from behave import *
from pages.GridBoletosAvion import ComisionesBoletosAvionPage
from config import ID_SOLICITUD
from pages.all_page import AllPage
import time


@given('Buscar y seleccionar solicitud Boletos de Avion')
def step_impl(context,estatus):


    context.all_page = AllPage(context.driver)
    context.comisionesBA = ComisionesBoletosAvionPage(context.driver)
    context.comisionesBA.buscar_comisionBoletosAvion(ID_SOLICITUD)
 
@when('Seleccionar Nuevo Registro')


@when('Capturar la información del formulario ')


@then('Validar el boleto genere la factura correctamente')

def step_impl(context,estatus):  
    assert context.reembolsar.validar_grid(), \
                f"El registro estado con registro Solicitud de comisión pendiente de autorización no apareció en el grid"
 