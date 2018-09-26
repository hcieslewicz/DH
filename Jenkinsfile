

pipeline {
    agent any
    environment {
        PYTHONPATH="${workspace}"
    }
    stages {
        stage('Build') {
           agent {
            label 'master'
           }
           steps {
               echo 'Cleaning directory'

               echo 'Checkout scm'
               checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                //withPythonEnv('python') {
                // Uses the default system installation of Python
                // Equivalent to withPythonEnv('/usr/bin/python')
                //pysh 'python --version'
                sh 'pip install nose selenium pytest'
                sh 'pytest tests/'

            }
        }
    }
}
