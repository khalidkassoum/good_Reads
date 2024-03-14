pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'python ./API_tests.py'
                bat "python -m pip install --upgrade pip"


            }
        }

    }
}