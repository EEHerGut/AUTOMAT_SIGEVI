Feature: Alta de comprobación 

        Background: Login  
            Given Hemos abierto la página inicial del sistema login
            When Capturas el usuario "mainc044" , contraseña "B@40bR4$1607202$"
            And Seleccionar iniciar sesión
            And Seleccionar el rol "Operador SIGEVI" y dar clic en continuar
            Then El sistema nos permite visualizar el panel principal
            
        Scenario: Alta de comprobación - nacional
            Given Seleccionar solicitud que cuenta con el estatus "Comisión pendiente de comprobación" comprobación
            and Seleccionar menu de autorizar Consultar/Modificar comprobación
            When Agregar comprobación con gasto con comprobante y agregar impuesto
            Then Visualizar el registro creado en el grid de comprobación

        