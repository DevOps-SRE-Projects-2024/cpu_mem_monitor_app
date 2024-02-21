pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker_hub_creds_id' // Update with your Docker Hub credentials ID in Jenkins
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id') // Update with your AWS access key ID credential ID in Jenkins
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key') // Update with your AWS secret access key credential ID in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
                        def customImage = docker.build('your_username/your_repository:latest', '.')
                        customImage.push()
                    }
                }
            }
        }

        stage('Create EKS Cluster') {
            steps {
                script {
                    // Add steps to create EKS cluster with Fargate profile
                    // Use AWS CLI or AWS SDK for these operations
                }
            }
        }

        stage('Update Deployment YAML') {
            steps {
                script {
                    // Add steps to update deployment.yaml with the new Docker image
                    sh 'sed -i "s#image: your_username/your_repository:.*#image: your_username/your_repository:latest#" deployment.yaml'
                }
            }
        }

        stage('Deploy to EKS Cluster') {
            steps {
                script {
                    // Add steps to deploy the application to EKS cluster
                    // Use kubectl or eksctl for deployment
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

