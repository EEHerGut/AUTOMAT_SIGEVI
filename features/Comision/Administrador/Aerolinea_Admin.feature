Feature: Alta de aerolínea
    ##Rol:Operador 
    ##Quiero: Dar de alta una solicitud nacional/internacional sin anticipo 
    ##Para: Atender una comisión
    
    Scenario: Login  
        Given Inicio sesion como "ADMINISTRADOR"
        Then El sistema nos permite visualizar el panel principal

    Scenario: Alta de aerolinea
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "Aerolínea"
        When Agregar aerolinea
        Then La Aerolinea se agrega correctamente

    Scenario: Modificar aerolinea
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "Aerolínea" EDITAR AEROLINEA
        When Buscar la aerolinea y editar
        Then La aerolinea se edita correctamente

    Scenario: Activar aerolinea
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "Aerolínea" activar/desactivar aerolinea
        When Buscar la aerolinea activar/desactivar
        Then La aerolinea activa/desactiva correctamente


	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestrela pantalla inicial

