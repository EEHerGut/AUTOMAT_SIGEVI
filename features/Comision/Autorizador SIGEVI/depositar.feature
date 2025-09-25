Feature: Depositar dotación

    @login_autorizador
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @depositar
    Scenario: Depositar
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" depositar
        When Seleccionar menu de depositar
		And Autorizar la dotación y aceptar
        Then Validar el estatus de la comisión "Depósito en proceso" autorizar solicitud depositar

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   