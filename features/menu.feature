Feature: Navegacion en el menu de Comisiones

    Scenario: Menu comision
     Given visualizar la pagina principal
     When Seleccionar el menu comision y despues comisiones
     Then Visualizar el detalle de comisiones
    
    Scenario: Busqueda de comision
        Given Visualizar el grid de comisiones
        When Agregar numero de comisión
        Then Visualizar la comisión y dar clic en detalle