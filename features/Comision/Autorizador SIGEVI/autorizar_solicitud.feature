Feature: Autorizar Solicitud
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    ##Hola

    Background: Login  
        Given Hemos abierto la página inicial del sistema login
        When Capturas el usuario "mainc044" , contraseña "B@40bR4$1607202$"
        And Seleccionar iniciar sesión
        And Seleccionar el rol "Autorizador SIGEVI" y dar clic en continuar
        Then El sistema nos permite visualizar el panel principal    
        
    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión pendiente de autorización"
        When Seleccionar menu de autorizar
		And Autorizar la solicitud y aceptar
        Then Validar el estatus de la comisión "Solicitud de comisión autorizada" autorizar solicitud
   