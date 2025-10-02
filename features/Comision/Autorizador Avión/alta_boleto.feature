Feature: Alta de boleto de avión
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    @login_operador
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_AVIÓN"
        Then El sistema nos permite visualizar el panel principal
    
     Scenario: Alta de boleto de avión
        Given Seleccionar solicitud para dar de alta boleto de avión
        When Seleccionar nuevo 2 registro 
		And dar de alta boleto de avión
        Then Validar el boleto se haya generado correctamente
        