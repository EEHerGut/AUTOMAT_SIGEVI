Feature: Autorizar Comprobacion

    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión con comprobación pendiente de autorización
    #Comisión conciliada
  
    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con comprobación pendiente de autorización" autorizar comproabación
        When Seleccionar menu de autorizar comprobación
		And Autorizar la solicitud y aceptar autorizar comprobación
        Then Validar el estatus de la comisión "Comprobación autorizada a cargo del comisionado" autorizar comprobación

    ##- Comprobación autorizada a cargo del comisionado
    ##- Comprobación autorizada a favor del comisionado
    ##- Comprobación autorizada 

    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


   
