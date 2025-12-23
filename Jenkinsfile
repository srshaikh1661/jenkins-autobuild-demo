pipeline {
    agent any
    
    tools {
        // For Java project
        maven 'Maven' 
        // For Python project (if needed)
        // python 'Python3'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/yourusername/jenkins-autobuild-demo.git'
            }
        }
        
        stage('Build') {
            steps {
                // For Java Maven project
                sh 'mvn clean compile'
                
                // For Python project (uncomment below)
                // sh 'python -m py_compile src/main.py'
            }
        }
        
        stage('Test') {
            steps {
                // For Java Maven project
                sh 'mvn test'
                
                // For Python project (uncomment below)
                // sh 'python -m pytest tests/ -v'
            }
        }
        
        stage('Package') {
            steps {
                // For Java Maven project
                sh 'mvn package -DskipTests'
                
                // For Python project (uncomment below)
                // sh 'tar -czf application.tar.gz src/'
            }
            
            post {
                success {
                    archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
                    // For Python: 'application.tar.gz'
                }
            }
        }
    }
    
    post {
        always {
            junit 'target/surefire-reports/*.xml'  // Java test reports
            // For Python pytest reports (if configured)
            // junit 'test-reports/*.xml'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
