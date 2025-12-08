Feature: Enviar solicitud a comprobación

    Scenario: Login  
        Given Inicio sesion como "OPERADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal
    ## Comprobación rechazada
    ## Comisión pendiente de comprobación - comisión sin dotación
    ## Comisión con dotación autorizada - comisión con dotación


    Scenario: Enviar comprobacion
        Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" envío comprobación
        When Seleccionar menu de Envío a comprobación
		And Enviar la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión con comprobación pendiente de autorización"

    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial


