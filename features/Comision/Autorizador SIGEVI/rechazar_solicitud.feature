Feature: Rechazar Solicitud
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    ##Hola
    
    Scenario: Login  
        Given Inicio sesión como "AUTORIZADOR_SIGEVI"
        Then El sistema nos permite visualizar el panel principal  
        
    @rechazar_solicitud
    Scenario: Rechazar solicitud
        Given Seleccionar solicitud que cuenta con el estatus "Solicitud de comisión pendiente de autorización" rechazar solicitud
        When Seleccionar menu de rechazar
		And Rechazar la solicitud y aceptar
        Then Validar el estatus de la comisión "Solicitud de comisión rechazada" rechazar solicitud
        #Comisión pendiente de dotación - comisión con dotación
        #Solicitud de comisión autorizada - comisión sin dotación
	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el botón de cerrar sesión
        Then Seleccionar el boton de cerrar sesión y esperar a que el sistema nos muestrela pantalla inicial


   