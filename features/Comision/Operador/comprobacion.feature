Feature: Alta de comprobación 

        Scenario: Login  
            Given Inicio sesión como "OPERADOR_SIGEVI"
            Then El sistema nos permite visualizar el panel principal
       
    #Comisión pendiente de dotación - Comisión con dotación autorizada- Comisión pendiente de comprobación- con anticipo
    #Comisión pendiente de comprobación - sin anticipo
        @alta_comprobación    
        Scenario: Alta de comprobación - nacional
            Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" comprobación
            and Seleccionar menu de autorizar Consultar/Modificar comprobación
            When Agregar comprobación con gasto con comprobante y agregar impuesto
            Then Visualizar el registro creado en el grid de comprobación

        Scenario: Cerrar sesión
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


