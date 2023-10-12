pipeline {
	agent any

	parameters {
		string(name: 'X', defaultValue: '300', description: 'Value of X')
		string(name: 'Y', defaultValue: '4', description: 'Value of Y')
	}

	stages {
		stage('Checkout') {
			steps {
				checkout scmGit(branches: name: '*/master', extensions: [], userRemoteConfigs: url: 'https://github.com/ashikha2023/python-calculator.git')
			}
		}
		stage('Build run') {
			steps {
				script {
					def x = params.X
					def y = params.Y

					sh "python3 math_operations.py ${x} ${y}"
				}
			}
		}
    }
}