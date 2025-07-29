		Feature: Login

		  Scenario: Probar Login Exitoso
			  Given Hemos abierto la página inicial del sistema login
			  When Capturas el usuario y contraseña
			  And Seleccionar iniciar sesión
			  When Seleccionar el rol y dar clic en continuar
              Then El sistema nos permite visualizar el panel principal

