Feature: Autorizar Dotación
    ##Rol:Operador 
    ##Quiero: Autorizar una dotación
    ##Para: Atender una comisión
    
    Background: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión pendiente de comprobación - sin anticipo
    #Comprobación autorizada a favor del comisionado - con anticipo
    
        
    @autorizar_dotación   
    Scenario: Autorizar dotación
        Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" autorizar dotación
        When Seleccionar menu de autorizar dotación
		And Autorizar la solicitud y aceptar autorizar dotación
        Then Validar el estatus de la comisión "Comprobación autorizada a favor del comisionado" autorizar dotación

  	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial

   