pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/ardiyanto1234/efiasi_web.git' // Ganti dengan repo Anda
        BRANCH = 'master'  // Ganti dengan branch yang sesuai
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone repositori dari GitHub
                git branch: "${BRANCH}", url: "${GIT_REPO}"
            }
        }
        
        stage('Build') {
            steps {
                // Menjalankan build project, misalnya untuk Node.js
                sh 'npm install'
            }
        }
        
        stage('Test') {
            steps {
                // Menjalankan test (misalnya unit test)
                sh 'npm test'
            }
        }
    }
    
    post {
        always {
            // Menampilkan laporan setelah selesai
            echo 'Pipeline selesai!'
        }
        success {
            // Jika pipeline berhasil
            echo 'Build dan testing berhasil!'
        }
        failure {
            // Jika pipeline gagal
            echo 'Build atau testing gagal!'
        }
    }
}