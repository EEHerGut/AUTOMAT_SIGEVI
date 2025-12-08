
Feature: Alta de Moneda
  
    Scenario: Login  
        Given Inicio sesion como "ADMINISTRADOR"
        Then El sistema nos permite visualizar el panel principal

    
    Scenario: Alta de Moneda
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos -  "Moneda" ALTA moneda
        When Agregar Moneda
        Then La Moneda se agrega correctamente


    Scenario: Modificar de moneda
        Given Seleccionar el menu Configuración - Catálogos - "Moneda" EDITAR moneda
        When Buscar la moneda y editar
        Then La moneda se edita correctamente


    Scenario: Activar moneda
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "Moneda" ACTIVAR/DESACTIVAR moneda
        When Buscar la moneda para activar/desactivar
        Then La moneda se activa/desactiva correctamente
        

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial

