Feature: Revertir depósito
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  

    Scenario: depósito solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" revertir depósito
        When Seleccionar menu de revertir depósito
		And Revertir depósito de la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión pendiente de dotación" revertir depósito de la comisión


	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   