[![Build Status](https://build.sfdcbt.net/bt/buildStatus/icon?job=CICD%2FCICD_invoke-python-sample-lib%2Fmaster)](https://build.sfdcbt.net/bt/job/CICD/job/CICD_invoke-python-sample-lib/job/master/)

# cicd_invoke-python-sample-lib

This is a sample library for python. It has basic structure and other tooling recommended for invoke python library projects. 

## Getting Started





### Installing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install following

```code
brew install python
brew install pdm
```

It is also recommended to have [sonarlint](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode#:~:text=SonarLint%20for%20Visual%20Studio%20Code,as%20you%20create%20your%20code.) plugin installed for IDE. 

### Installing

A step by step series of examples that tell you have to get a development env running

To install the dependencies defined in pyproject.toml run the below command. PDM by default create a venv in the root project and install all the packages there. 


```text
pdm install
```

The above steps would have installed all dependencies. Now if we want to use the virutal environment, use the following command

```text
eval $(pdm venv activate)
```

Once in the virtual env shell we can run various commands as follows: 

Format Code: 
```
black src/
isort . 
```

Linter Check: 
```
flake8
```

Unit tests: 
```
pytest
```

Coverage: 
```
pytest --cov=src --cov-report html --cov-report term
```

Tox: (to run test in multiple environments. It has very good integration with TOX no need to duplicate dependencies.) 
```
tox 
```
Deactivate: To come out of the virtual env
```
deactivate
```

Build: 
```
pdm build
```

Publish: 
There is a publish command as well. Though we need to setup credentials etc. for it to really work. 
End with an example of getting some data out of the system or using it for a little demo


## Deployment

Add additional notes about how to deploy this on a live system

## Acknowledgments

