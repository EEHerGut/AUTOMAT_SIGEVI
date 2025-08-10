Feature: Enviar solicitud a comprobación

    Scenario: Login  
        Given Hemos abierto la página inicial del sistema login
        When Capturas el usuario "mainc044" , contraseña "B@40bR4$1607202$"
        And Seleccionar iniciar sesión
        And Seleccionar el rol "Operador SIGEVI" y dar clic en continuar
        Then El sistema nos permite visualizar el panel principal

    Scenario: Enviar comprobacion
        Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" envío comprobación
        When Seleccionar menu de Envío a comprobación
		And Enviar la comisión y aceptar
        Then Validar el estatus de la comisión "Comisión con comprobación pendiente de autorización"

        