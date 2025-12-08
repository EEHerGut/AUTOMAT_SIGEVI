Feature: Alta de comprobación 

        Scenario: Login  
            Given Inicio sesion como "OPERADOR_SIGEVI"
            Then El sistema nos permite visualizar el panel principal
       
    #Comisión pendiente de dotación - Comisión con dotación autorizada- Comisión pendiente de comprobación- con anticipo
    #Comisión pendiente de comprobación - sin anticipo
 
        Scenario: Alta de comprobación - nacional
            Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" comprobación
            and Seleccionar menu de autorizar Consultar/Modificar comprobación
            When Agregar comprobación con gasto con comprobante y agregar impuesto, pasar al estatus "Comisión pendiente de comprobación"
            Then Validar el estatus de la comisión "Comisión con comprobación pendiente de autorización" comprobación

        Scenario: Cerrar sesión
            Given Al terminar la prueba
            When Dar clic en el boton de cerrar sesion
            Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial
            