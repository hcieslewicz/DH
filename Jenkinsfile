
pipeline {
    agent any
    environment {
        PYTHONPATH = "${PYTHONPATH};${pwd()}"
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
            parallel {
                stage('Test On Windows with Firefox') {
                    agent {
                        label "windows"
                    }
                    steps {
                        bat 'pytest --driver firefox tests --alluredir=allure-results'
                    }
                }
                stage('Test On Windows with Chrome') {
                    agent {
                        label "windows"
                    }
                    steps {
                        bat 'pytest --driver chrome tests --alluredir=allure-results'
                    }
                }
                stage('Test On Windows with IE') {
                    agent {
                        label "windows"
                    }
                    steps {
                        bat 'pytest --driver ie tests --alluredir=allure-results'
                    }
                }
                stage('Test On Linux with Firefox') {
                    agent {
                        label "linux"
                    }
                    steps {
                        sh 'pytest --driver firefox tests --alluredir=allure-results'
                    }
                }
                stage('Test On Linux with Chrome') {
                    agent {
                        label "linux"
                    }
                    steps {
                        sh 'pytest --driver chrome tests --alluredir=allure-results'
                    }
                }
            }
        }
    }
}
