pipeline {
    agent any

    stages {
        
        stage('Setup parameters') {
      steps {
        script {
          properties([
            parameters([
              string(
                name: 'GCP_PROJECT_ID',
                trim: true
              ),
              string(

                name: 'GCR_IMAGE_NAME',
                trim: true
              ),
              string(

                name: 'GCR_IMAGE_TAG',
                trim: true
              )
            ])
          ])
        }
      }
    }
        
        stage('Clone Repository') {
            steps {
                script {
                    sh 'pwd'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                      sh "docker build -t gcr.io/${params.GCP_PROJECT_ID}/${params.GCR_IMAGE_NAME}:${params.GCR_IMAGE_TAG} ."
                     // sh 'docker run -p 5000:5000 cpu_monitor_image'
                     // Check if a container with the given image is already running
               def existingContainerId = sh(script: 'docker ps | grep "python3 app.py" | awk \'{print $1}\'', returnStdout: true).trim()

                if (existingContainerId) {
                    echo "Stopping and removing existing container with ID: ${existingContainerId}"
                    sh "docker stop ${existingContainerId}"
                    sh "docker rm ${existingContainerId} -f"
                }

                // Run Docker container in the background and redirect logs to a file
                sh 'docker run -p 5000:5000 cpu_monitor_image > docker_logs.txt 2>&1 &'
                
                
            
                    }
                }
            }

         stage("Pushing ECR Image to GCR") {
      steps {

          script {
                    // Authenticate Docker with Google Container Registry
                    withCredentials([file(credentialsId: 'jenkins_gcp', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                sh "gcloud auth activate-service-account --key-file=\$GOOGLE_APPLICATION_CREDENTIALS"
                sh "gcloud auth configure-docker"
            }
                    
                    // Push the Docker image to Google Container Registry
                   sh "docker push us-docker.pkg.dev/${params.GCP_PROJECT_ID}/${params.GCR_IMAGE_NAME}:${params.GCR_IMAGE_TAG}"
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
