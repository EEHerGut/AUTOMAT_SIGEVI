Feature: Autorizar Comprobacion

    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión con comprobación pendiente de autorización
    @autorizar_solicitud_comprobacion    
    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con comprobación pendiente de autorización" autorizar comproabación
        When Seleccionar menu de autorizar comprobación
		And Autorizar la solicitud y aceptar autorizar comprobación
        Then Validar el estatus de la comisión "Comprobación autorizada a favor del comisionado" autorizar comprobación

    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   
