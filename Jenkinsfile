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

        stage('Build Docker Image (Docker-in-Docker)') {
            steps {
                sh 'docker build -f Dockerfile.flask -t flask-app:latest .'
            }
        }

        stage('Deploy Flask Container') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app flask-app:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 2 && curl http://localhost:5000/api/health'
            }
        }

        stage('Show App Logs') {
            steps {
                sh 'docker logs --tail 100 flask-app'
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
