Feature: Conciliar

    Scenario: Login  
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
    #Comisión con comprobación pendiente de autorización
    #Comisión conciliada
  
    Scenario: Autorizar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Comisión con reintegro pendiente de validación" conciliar comproabación
        When Seleccionar menu de Conciliar comisión
		And La comisión se concilia correctamente
       
    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


   
