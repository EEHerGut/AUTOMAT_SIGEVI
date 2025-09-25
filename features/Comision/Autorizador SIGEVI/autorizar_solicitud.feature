Feature: Autorizar Solicitud

    @login_autorizador
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @autorizar_solicitud
    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión pendiente de autorización"
        When Seleccionar menu de autorizar
		And Autorizar la solicitud y aceptar
        Then Validar el estatus de la comisión "Comisión pendiente de dotación" autorizar solicitud
        #Comisión pendiente de dotación - comisión con dotación
        #Solicitud de comisión autorizada - comisión sin dotación
	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   