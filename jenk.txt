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
                    echo "=== INSTALANDO DEPENDENCIAS MANUALMENTE ==="
                    python -m pip install behave==1.2.6
                    python -m pip install selenium==4.15.0
                    python -m pip install allure-behave==2.9.45
                '''
            }
        }
        
        stage('Verify Installation') {
            steps {
                bat '''
                    echo "=== VERIFICANDO INSTALACIÓN ==="
                    behave --version
                    pip list | findstr behave
                '''
            }
        }
        
        stage('Run Behave Tests') {
            steps {
                bat '''
                    echo "=== EJECUTANDO PRUEBAS ==="
                    behave features/Comision/Operador/solicitud_anticipo.feature --format pretty
                '''
            }
        }
    }
    
    post {
        always {
            echo "✅ Proceso completado"
        }
    }
}