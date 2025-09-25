pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', // ← CAMBIAR AQUÍ
                url: 'https://github.com/EEHerGut/AUTOMAT_SIGEVI.git'
            }
        stage('Ejecutar Behave') {
            steps {
                bat 'behave features/Comision/Operador/solicitud_anticipo.feature'
            }
        }
    }
    }
}