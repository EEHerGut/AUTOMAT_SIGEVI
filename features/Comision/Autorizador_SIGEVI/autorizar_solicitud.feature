Feature: Autorizar Solicitud

 
    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        

    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión pendiente de autorización"
        When Seleccionar menu de autorizar
		And Autorizar la solicitud y aceptar "Comisión pendiente de dotación"
        Then Validar el estatus de la comisión "Comisión con dotación autorizada" autorizar solicitud
        #Comisión pendiente de dotación - comisión con dotación
        #Solicitud de comisión autorizada - comisión sin dotación
	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial

   