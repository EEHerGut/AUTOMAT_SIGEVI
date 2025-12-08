@regression @catalogo_estados @administrador @catalogos
Feature: Administración de Estados

    @smoke @login @critical @high
    Scenario: Login exitoso como administrador
        Given Inicio sesion como "ADMINISTRADOR"
        Then El sistema nos permite visualizar el panel principal

    @regression @estado @alta @create @medium
    Scenario: Alta de estado
        Given Seleccionar el menu Configuracion - Catalogos -  "Estado-municipio/ciudad (NAL)" ALTA ESTADO
        When Agregar estado
        Then El estado se agrega correctamente

    @regression @estado @modificar @update @medium
    Scenario: Modificar estado
        Given Seleccionar el menu Configuracion - Catalogos - "Estado-municipio/ciudad (NAL)" EDITAR ESTADO
        When Buscar el estado y editar
        Then El estado se edita correctamente

    @regression @estado @activar @toggle @medium
    Scenario: Activar estado
        Given Seleccionar el menu Configuracion - Catalogos - "Estado-municipio/ciudad (NAL)" ACTIVAR/DESACTIVAR ESTADO
        When Buscar el estado para activar/desactivar
        Then El estado se activa/desactiva correctamente

    @smoke @logout @critical @high
    Scenario: Cerrar sesion
        Given Al terminar la prueba
        When Dar clic en el boton de cerrar sesion
        Then Seleccionar el boton de cerrar sesion y esperar a que el sistema nos muestre la pantalla inicial
        