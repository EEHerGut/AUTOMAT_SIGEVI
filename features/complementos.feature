Feature: Complementos Nacional

    Scenario: Crear complemento a favor del comisionado nacional
        Given El autorizador ingresa al sistema, ingresa al grid de comisiones
        When Selecionar la comision conciliada para visualizar el detalle
        Then Seleccionar el menú Complementos, dar clic alta de complementos visualizar el formulario
        And Dar de alta el formulario y dar clic en alta de complemento

    Scenario: Agregar impuesto a un complemento
         Given El autorizador ingresa al sistema para agregar un impuesto a un complemento
         When Seleccionar la comisión conciliada para visualizar el detalle 
         and Seleccionar el menú de complementos
         and Seleccionar el complemento, dar clic en el botón agregar impuesto
         Then Seleccionar el concepto y el monto, dar clic en agregar - aceptar y aceptar.

    Scenario: Autorizar complemento
         Given El autorizador ingresa al sistema para autorizar un complemento
         When Seleccionar la comisión conciliada para visualizar el detalle autorizar
         and Seleccionar el menú complementos para autorizar complemento
         and Seleccionar el botón registrado del complemento a autorizar,visualizar el detalle
         Then Seleccionar el botón autorizar complemento, confirmar, aceptar.

    Scenario: Reembolsar al comisionado
         Given El autorizador ingresa al sistema para reembolsar al comisionado
         When Seleccionar la comisión conciliada para visualizar el detalle reembolsar
         And Seleccionar el menú complementos para reembolsar complemento
         And Seleccionar el botón autorizado del complemento a reembolsar,visualizar el detalle
         Then Seleccionar el botón reembolso al comisionado, Solicitar reembolso, aceptar.
         And Validar estatus


