pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'npm install'  // Replace sh with bat for Windows
            }
        }
        stage('Build Project') {
            steps {
                bat 'npm run build'  // Again, using bat instead of sh
            }
        }
    }
}
