Feature: Solicitar reembolso

    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    
    Scenario: Solicitar reembolso
        Given Seleccionar solicitud que cuenta con el estatus "Comprobación autorizada a favor del comisionado" reembolso
        When Seleccionar menu de reembolso
		And Rembolsar la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión con reembolso en proceso" reembolsar comisión

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


   