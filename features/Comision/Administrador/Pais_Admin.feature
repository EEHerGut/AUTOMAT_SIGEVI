
Feature: Alta de país
  
    Scenario: Login  
        Given Inicio sesion como "ADMINISTRADOR"
        Then El sistema nos permite visualizar el panel principal

    Scenario: Alta de país
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos -  "País-ciudad(INT)" país
        When Agregar país
        Then El país se agrega correctamente


    Scenario: Modificar país
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "País-ciudad(INT)" EDITAR PAÍS
        When Buscar el país y editar
        Then El país se edita correctamente

    Scenario: Activar moneda
        #Given El usuario se encuentra en el grid de comisiones
        Given Seleccionar el menu Configuración - Catálogos - "MonPaís-ciudad(INT)eda" ACTIVAR/DESACTIVAR país
        When Buscar el país para activar/desactivar
        Then El país se activa/desactiva correctamente

	Scenario: Cerrar sesión
		Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestrela pantalla inicial

