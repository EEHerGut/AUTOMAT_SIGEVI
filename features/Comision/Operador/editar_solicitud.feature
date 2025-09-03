
Feature: Editar solicitud sin anticipo a con anticipo


    Scenario: Login  
        Given Inicio sesión como "OPERADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal
    
    Scenario: Alta de solicitud sin anticipo - nacional
        #Given El usuario se encuentra en el grid de comisiones
    Given Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud
        and Deberíamos ver el formulario de solicitud de comisión
		and Completamos los campos obligatorios
        When Guardamos la solicitud
        Then La solicitud se crea exitosamente
        
    @editar_solicitud
    Scenario: Editar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión en registro" editar solicitud
        When Seleccionar menu de solicitud y editar la solicitud y guardar la solicitud
        Then Validar que la solicitud cuente con el estatus "Solicitud de comisión en registro" editar solicitud

    Scenario: Dar de alta ciudad
        Given La solicitud esta con estatus "Solicitud de comisión en registro", selecionar la comisión para agregar ciudad
        When Agregar municipio y/o ciudad
        Then La ciudad se agrega correctamente

    Scenario: Dar de alta vuelo
        Given Visualizar el grid de comisiones vuelo con estatus "Solicitud de comisión en registro"
        When Seleccionar el menu de vuelos
        And Dar clic en el botón Agregar vuelo y seleccionar tipo de vuelo
        And Agregar datos de vuelo, seleccionar agregar y selecionar Aceptar - Aceptar
        Then Validar registro en el grid vuelo 

    Scenario: Enviar solicitud al área de pagos
        Given Visualizar el grid de comisiones enviar al área de pagos con estatus "Solicitud de comisión en registro"
        When Seleccionar el menu de envio a autorización
        And Confirmar el envío
        Then Validar que la solicitud cuente con el estatus "Solicitud de comisión pendiente de autorización"

    Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial



    	


