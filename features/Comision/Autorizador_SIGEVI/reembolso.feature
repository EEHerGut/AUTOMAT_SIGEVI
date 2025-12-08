Feature: Reembolso

    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión con comprobación pendiente de autorización
    #Comisión conciliada
  
    Scenario: Solicitar reembolso
        Given Seleccionar solicitud que cuenta con el estatus "Comprobación autorizada a favor del comisionado" solicitar reembolso
        When Seleccionar menu de Solicitar reembolso 
        And Autorizar la solicitud y aceptar el reembolso
        Then Validar el estatus de la comisión "Comisión de rembolso en proceso" rembolso

       
    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


   
