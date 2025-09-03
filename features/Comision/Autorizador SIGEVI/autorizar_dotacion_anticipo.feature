Feature: Autorizar Dotación
    ##Rol:Operador 
    ##Quiero: Autorizar una dotación
    ##Para: Atender una comisión
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión pendiente de dotación - con anticipo
    
    @autorizar_dotación_anticipo
    Scenario: Autorizar dotación
        Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de dotación" autorizar dotación con anticipo
        When Seleccionar menu de autorizar dotación con anticipo
		And Autorizar la solicitud y aceptar autorizar dotación con anticipo
        Then Validar el estatus de la comisión "Comisión con dotación autorizada" autorizar dotación con anticipo
        #Comisión con dotación autorizada - con anticipo - Comprobación autorizada a favor del comisionado

  	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial

   