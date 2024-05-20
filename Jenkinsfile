@Library('CICD_pipeline-central-python-lib') _

pipeline {
    agent { label getStandardPythonAgent() }

    options {
	  timeout(time:getStandardPythonTimeout(), unit:getStandardPythonTimeoutUnit())
	  disableConcurrentBuilds()
	  buildDiscarder(logRotator(numToKeepStr:getStandardPythonBuildsToKeep()))
	}

     stages {
        stage('Install') {
            steps {
                standardPythonInstall()
            }
        }
        stage('Clean') {
            steps {
                standardPythonClean()
            }
        }

         stage('Check') {
            steps {
                standardPythonCheck()
            }
        }
        stage('Test') {
            steps {
                standardPythonTest()
            }
        }

        stage('Security') {
            steps {
                standardPythonSecurity()
            }
        }

        stage('Assemble') {
            steps {
                standardPythonAssemble()
            }
        }
        stage('Publish') {
            when {
                expression {
                    return env.GIT_BRANCH == 'master'
                }
            }
            steps {
                standardPythonPublish()
            }
        }
       
    }
    post {
        always {
        	standardPythonArchiving()
        }
        failure {
            standardPythonSlackNotification(currentBuild.result)
        }
    }
}
