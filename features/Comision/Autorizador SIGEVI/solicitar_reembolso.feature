Feature: Solicitar reembolso

    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @solicitar_reembolso
    Scenario: Solicitar reembolso
        Given Seleccionar solicitud que cuenta con el estatus "Comprobación autorizada a favor del comisionado" reembolso
        When Seleccionar menu de reembolso
		And Rembolsar la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión con reembolso en proceso" reembolsar comisión

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   