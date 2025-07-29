Feature: Alta de solicitud Nacional/Internacional
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
        
    Scenario: Alta de solicitud con anticipo - nacional
        Given El usuario se encuentra en el grid de comisiones
        When Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud
        Then Deberíamos ver el formulario de solicitud de comisión
		When Completamos los campos obligatorios
        And Guardamos la solicitud
        Then La solicitud se crea exitosamente
    
    Scenario: Dar de alta ciudad
        Given El usuario se encuentra en el grid de comisiones ciudad
        And la solicitud esta con estatus "Solicitud de comisión en registro" ciudad y selecionar la comisión para agregar ciudad
        When Seleccionar menu de ciudades
        And Dar clic en el boton Agregar municipio 
        And Agregar municipio
        Then La ciudad se agrega correctamente
    
        Scenario: Dar de alta vuelo
        Given Visualizar el grid de comisiones vuelo
        When Seleccionar el menu de vuelos
        And Dar clic en el botón Agregar vuelo y seleccionar tipo de vuelo
        And Agregar datos de vuelo, seleccionar agregar y selecionar Aceptar - Aceptar
        Then Validar registro en el grid vuelo

        Scenario: Dar de alta gasto
        Given Visualizar el grid de comisiones gasto
        When Seleccionar el menu de gasto
        And Dar clic en el botón Agregar gasto, seleccionar tipo de gasto, monto y dar clic en agregar
        Then Validar registro en el grid de gasto