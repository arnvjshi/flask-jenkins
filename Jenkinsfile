pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    set -eux
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    set -eux
                    . venv/bin/activate
                    pytest test_app.py -v
                '''
            }
        }

        stage('Build Docker Image (Docker-in-Docker)') {
            steps {
                echo 'Building Docker image...'
                sh 'set -eux; docker build -f Dockerfile.flask -t flask-app:latest .'
            }
        }

        stage('Deploy Flask Container') {
            steps {
                echo 'Deploying container...'
                sh '''
                    set -eux
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app flask-app:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking health endpoint...'
                sh '''
                    set -eux
                    sleep 3
                    # Get Flask container IP and test health endpoint
                    FLASK_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-app)
                    curl http://${FLASK_IP}:5000/api/health
                '''
                echo 'Health check passed!'
            }
        }

        stage('Show App Logs') {
            steps {
                echo 'Showing app logs...'
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
