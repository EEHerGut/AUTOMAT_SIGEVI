
Feature: Alta de solicitud Nacional/Internacional
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    @login
    Scenario: Login  
        Given Hemos abierto la página inicial del sistema login
        When Capturas el usuario "mainc044" , contraseña "B@40bR4$1607202$"
        And Seleccionar iniciar sesión
        And Seleccionar el rol "Operador SIGEVI" y dar clic en continuar
        Then El sistema nos permite visualizar el panel principal

    @comision
    Scenario: Alta de solicitud sin anticipo - nacional
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud
        Then Deberíamos ver el formulario de solicitud de comisión
		When Completamos los campos obligatorios
        And Guardamos la solicitud
        Then La solicitud se crea exitosamente
        
    @ciudad
    Scenario: Dar de alta ciudad
        #Given El usuario se encuentra en el grid de comisiones ciudad
        Given La solicitud esta con estatus "Solicitud de comisión en registro" ciudad y selecionar la comisión para agregar ciudad
        When Seleccionar menu de ciudades
        And Dar clic en el boton Agregar municipio 
        And Agregar municipio
        Then La ciudad se agrega correctamente

    @vuelo
    Scenario: Dar de alta vuelo
        Given Visualizar el grid de comisiones vuelo con estatus "Solicitud de comisión en registro"
        When Seleccionar el menu de vuelos
        And Dar clic en el botón Agregar vuelo y seleccionar tipo de vuelo
        And Agregar datos de vuelo, seleccionar agregar y selecionar Aceptar - Aceptar
        Then Validar registro en el grid vuelo

    @enviar
    Scenario: Enviar solicitud al área de pagos
        Given Visualizar el grid de comisiones enviar al área de pagos con estatus "Solicitud de comisión en registro"
        When Seleccionar el menu de envio a autorización
        And Confirmar el envío
        Then Validar que la solicitud cuente con el estatus "Solicitud de comisión pendiente de autorización"
        