pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker_hub_creds_id' // Update with your Docker Hub credentials ID in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git clone https://github.com/DevOps-SRE-Projects-2024/cpu_mem_monitor_app.git
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                     cd /home/ubuntu/cpu_mem_monitor_app/
                     sudo docker build -t cpu_monitor_image .
                     sudo docker run -p 5000:5000 cpu_monitor_image
                    }
                }
            }
        }
/*
        stage('Create EKS Cluster') {
            steps {
                script {
                    // Use withCredentials to securely access AWS credentials
                    withCredentials([[
                        $class: 'AmazonWebServicesCredentialsBinding',
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        credentialsId: 'aws_creds', // Update with your AWS credentials ID in Jenkins
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]]) {
                        // Add steps to create EKS cluster with Fargate profile
                        // Use AWS CLI or AWS SDK for these operations
                    }
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
*/
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
