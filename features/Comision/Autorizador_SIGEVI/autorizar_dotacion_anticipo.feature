Feature: Autorizar Dotación

    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal
    
    #Comisión pendiente de dotación - con anticipo
    

    Scenario: Autorizar dotación
        Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de dotación" autorizar dotación con anticipo
        When Seleccionar menu de autorizar dotación con anticipo
		And Autorizar la solicitud y aceptar autorizar dotación con anticipo
        Then Validar el estatus de la comisión "Comisión con dotación autorizada" autorizar dotación con anticipo
        #Comisión con dotación autorizada - con anticipo - Comprobación autorizada a favor del comisionado

  	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial

   