Feature: Admin boletos de avión
    ##Rol:Administrador Boletos Avión
    ##Quiero: Poder gestionar los boletos de avión de una comisión nacional/internacional
    ##Para: Tener el control de las facturas

    @login_AutorizadorBoletosAvion
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_AVIÓN"
        Then El sistema nos permite visualizar el panel principal

    @AltaBoletoAvión
     Scenario: Alta de boleto de avión
        #Given El usuario se encuentra en la pantalla de grid de comisiones Boletos de Avión
        Given Buscar y seleccionar solicitud Boletos de Avion
        And Seleccionar Nuevo Registro
        And Capturar la información del formulario
        Then Validar el boleto genere la factura correctamente