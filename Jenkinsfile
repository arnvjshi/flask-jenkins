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
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_app.py -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -f Dockerfile.flask -t flask-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-app-test flask-app:latest'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 2 && curl http://localhost:5000/api/health'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker stop flask-app-test && docker rm flask-app-test || true'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
