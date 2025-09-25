Feature: Cancelar solicitud
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @cancelar_solicitud
    Scenario: Cancelar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión pendiente de autorización" cancelar solicitud
        When Seleccionar menu de cancelar solicitud
		And Cancelar la solicitud y aceptar
        Then Validar el estatus de la comisión "Solicitud de comisión rechazada" cancelar solicitud
        #Comisión pendiente de dotación - comisión con dotación
        #Solicitud de comisión autorizada - comisión sin dotación
	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   