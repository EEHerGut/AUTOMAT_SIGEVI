Feature: Revertir dotación
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @revertir_dotación
    Scenario: Revertir dotación
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" revertir dotación
        When Seleccionar menu de revertir dotación
		And Revertir dotación de la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión pendiente de dotación" revertir dotación de la comisión


	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   