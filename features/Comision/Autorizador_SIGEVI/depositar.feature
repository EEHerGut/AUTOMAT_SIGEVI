Feature: Depositar dotación


    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        

    Scenario: Depositar
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" depositar
        When Seleccionar menu de depositar
		And Autorizar la dotación y aceptar
        Then Validar el estatus de la comisión "Depósito en proceso" depositar

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


   