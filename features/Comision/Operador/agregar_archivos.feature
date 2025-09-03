Feature: Alta de comprobación 

        Scenario: Login  
            Given Inicio sesión como "OPERADOR_SIGEVI"
            Then El sistema nos permite visualizar el panel principal
       
    #Comisión pendiente de dotación - con anticipo
    #Comisión pendiente de comprobación - sin anticipo
        @alta_archivo
        Scenario: Alta de archivo - nacional
            Given Seleccionar solicitud que cuenta con el estatus "Comisión con dotación autorizada" alta de archivo
            When Seleccionar menu de archivos
            and Agregar archivos a la comisión
            Then Validar registro en el grid archivos

        Scenario: Cerrar sesión
            Given Al terminar la prueba
            When Dar clic en el botón de cerrar sesión
            Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial

