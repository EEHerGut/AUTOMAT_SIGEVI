Feature: Complementos Nacional

Scenario: Crear complemento a favor del comisionado nacional
        Given Inicio sesion como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
    
@omitir
Scenario: Agregar complemento y un impuesto 
         Given Seleccionar solicitud que cuenta con el estatus "Comisión conciliada" complemento
         And Seleccionar menu de Complementos
         When Seleccionar el botón de alta de complemento
         and Agregar información del formulario, junto con el impuesto
         Then Visualizar el complemento
@omitir   
Scenario: Autorizar Complemento
         Given Selecciónar el complemento con el estatus "Registrado"
         When Seleccionar el botón autorizar complemento
         Then Visualizar el complemento autorizado

@omitir
Scenario: Solicitar reembolso
         Given Selecciónar el complemento con el estatus "Registro" reembolso
         When Seleccionar el botón autorizar complemento reembolso
         Then Visualizar el complemento autorizado reembolso

Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial



Scenario: Baja de complemento 
         Given Seleccionar solicitud que cuenta con el estatus "Comisión conciliada" complemento baja
         And Seleccionar menu de Complementos baja
         When Seleccionar el botón de baja de complemento
         Then No visualizar el complemento
