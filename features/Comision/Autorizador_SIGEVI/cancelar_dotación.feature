Feature: Cancelar dotación
  
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        

    Scenario: Cancelar dotación
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" cancelar dotación
        When Seleccionar menu de cancelar dotación
		And Cancelar la dotación y aceptar
        Then Validar el estatus de la comisión "Solicitud de comisión autorizada" cancelar dotación
        #Comisión pendiente de dotación - comisión con dotación
        #Solicitud de comisión autorizada - comisión sin dotación
	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   