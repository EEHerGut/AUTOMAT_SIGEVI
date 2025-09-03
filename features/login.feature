		Feature: Login
		 
		  Scenario: Probar Login Exitoso
        		Given Hemos abierto la página inicial del sistema login
        		When Capturas el usuario "uedga193" , contraseña "B@40bR4$1607202$"
       			And Seleccionar iniciar sesión
       			And Seleccionar el rol "Operador SIGEVI" y dar clic en continuar
        		Then El sistema nos permite visualizar el panel principal    

