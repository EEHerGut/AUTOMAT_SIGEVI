Feature: Autorizar Solicitud
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    ##Hola
        
    Scenario: Autorizar solicitud
        Given El usuario se encuentra en el grid de comisiones autorizar
        And seleccionar solicitud que cuenta con el estatus "{Solicitud de comisión pendiente de autorización}"
        When Seleccionar menu de autorizar
		And Autorizar la solicitud y aceptar
        Then Validar el estatus de la comisión "Solicitud de comisión autorizada"
   