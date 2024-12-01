pipeline {
    agent any
    environment {
        AWS_DEFAULT_REGION = 'eu-north-1'
        ECR_REGISTRY = '925860042597.dkr.ecr.eu-north-1.amazonaws.com'
        ECR_REPOSITORY = 'flask-dockere-ecr'
        IMAGE_TAG = "${env.BUILD_ID}"
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY') 
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_KEY')
    }
    stages {
        stage('Checkout Source') {
      steps {
        git url:'https://github.com/malamcsc/flask_project.git', branch:'main', credentialsId: 'gitlab-password-c'
         }
      }
        stage('Login to ECR') {
            steps {
                script {
                    withAWS(role: 'docker-ecr-service-role', roleAccount: '925860042597', credentialsId: 'docker-k8s-user-cred') {
                        sh 'aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $ECR_REPOSITORY:$IMAGE_TAG .'
            }
        }
        stage('Push Docker Image to ECR') {
            steps {
                sh 'docker tag $ECR_REPOSITORY:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG'
                sh 'docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
