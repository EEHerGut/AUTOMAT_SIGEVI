pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat '''
                    echo "=== INSTALANDO DEPENDENCIAS ==="
                    python -m pip install behave==1.2.6
                    python -m pip install selenium==4.15.0
                    python -m pip install allure-behave==2.9.45
                '''
            }
        }
        
        stage('Generate Config from Template') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'qa-credentials',
                    usernameVariable: 'JENKINS_USER', 
                    passwordVariable: 'JENKINS_PASS'
                )]) {
                    bat '''
                        echo "=== GENERANDO ARCHIVO DE CONFIGURACIÓN ==="
                        python -c "
                        import json
                        import os

                        # Cargar el template
                        with open('roles.template.json', 'r', encoding='utf-8') as f:
                            template = json.load(f)

                        # Reemplazar placeholders con credenciales reales
                        for role_name, role_data in template.items():
                            role_data['usuario'] = os.getenv('JENKINS_USER')
                            role_data['password'] = os.getenv('JENKINS_PASS')

                        # Guardar el archivo final
                        with open('roles.json', 'w', encoding='utf-8') as f:
                            json.dump(template, f, indent=2, ensure_ascii=False)

                        print('✅ roles.json generado exitosamente')
                        "
                        
                        echo "=== CONFIGURACIÓN GENERADA ==="
                        type roles.json
                    '''
                }
            }
        }
        
        stage('Verify Configuration') {
            steps {
                bat '''
                    echo "=== VERIFICANDO CONFIGURACIÓN ==="
                    python -c "
                    import json

                    try:
                        with open('roles.json', 'r') as f:
                            config = json.load(f)
                        
                        print('Roles configurados:')
                        for role, data in config.items():
                            print(f'  {role}: {data[\\\"usuario\\\"]} | Rol: {data[\\\"rol\\\"]}')
                            
                        print('✅ Configuración verificada correctamente')
                    except Exception as e:
                        print(f'❌ Error: {e}')
                        exit(1)
                    "
                '''
            }
        }
        
        stage('Run Behave Tests') {
            steps {
                bat '''
                    echo "=== EJECUTANDO PRUEBAS ==="
                    behave features/Comision/Operador/solicitud_anticipo.feature --format pretty --format allure --out allure-results
                '''
            }
        }
    }
    
    post {
        always {
            // Publicar reporte Allure
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]
            
            // Limpiar archivo temporal (opcional)
            bat '''
                if exist roles.json (
                    echo "=== LIMPIANDO ARCHIVO TEMPORAL ==="
                    del roles.json
                )
            '''
            
            echo "✅ Pipeline completado - Reporte Allure disponible"
        }
    }
}