pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                bat '''
                    python --version
                    pip --version
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Behave Tests') {
            steps {
                bat '''
                    echo "Instalando dependencias de Behave..."
                    pip list | findstr behave
                    pip list | findstr allure
                    
                    echo "Ejecutando pruebas..."
                    behave features/Comision/Operador/solicitud_anticipo.feature --format pretty
                '''
            }
        }
    }
    
    post {
        always {
            echo "Proceso completado - Revisar logs arriba"
        }
    }
}