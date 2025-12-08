Feature: Validar depósito 

        Scenario: Login  
            Given Inicio sesion como "OPERADOR_SIGEVI"
            Then El sistema nos permite visualizar el panel principal
 
        Scenario: Subir comprobante y validar depósito - nacional
            Given Seleccionar solicitud que cuenta con el estatus "Comprobación autorizada a cargo del comisionado" validar deposito
            When Cargar comprobante y enviar a validar deposito 
            Then Validar el estatus de la comisión "Comisión con reintegro pendiente de validación" validar depósito

        Scenario: Cerrar sesión
            Given Al terminar la prueba
            When Dar clic en el boton de cerrar sesion
            Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial
            