Feature: Alta de solicitud Nacional/Internacional
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión

    Background: Login  
        Given Inicio sesión como "OPERADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal
  
    Scenario: Alta de solicitud con anticipo - nacional
        Given Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud
        Then Deberíamos ver el formulario de solicitud de comisión anticipo
		When Completamos los campos obligatorios anticipo
        And Guardamos la solicitud
        Then La solicitud se crea exitosamente
    
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
        
        @gasto
    Scenario: Dar de alta gasto
        Given Visualizar el grid de comisiones gasto con estatus "Solicitud de comisión en registro"
        When Seleccionar el menu de gasto
        And Dar clic en el botón Agregar gasto, seleccionar tipo de gasto, monto y dar clic en agregar
        Then Validar registro en el grid de gasto