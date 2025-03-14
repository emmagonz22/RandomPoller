# Random Poller 🎲 

### This project was originally homework from the Google Tech Exchange Software Development Studio 2023; below are the requirements for the HW. Additionally, from these requirements, I created a webapp to add more interactivity to the Console application.

# Homework 1

Refer to the directions [here](https://site.sds-techx.in/hw1-unit-testing/#0) for how to complete this assignment.

Below is an abbreviated enumeration of the requirements:

| Requirement                                                 | Points
| ----------------------------------------------------------- | -------
| Add functionality to commit the changes                     | 5
| Modules, classes and methods commented                      | 5
| Participant class passing unit test                         | 5
| At least partially correct Poller class                     | 5
| Working attempted/correct/excused/missing/stop/total method | 12
| Working __enter__/__exit__ (open/save) methods              | 8
| Working __next__ method                                     | 20
| Working mock_open                                           | 10
| Working test for iterator                                   | 10
| Working tests for all other behaviors                       | 20
| Working test_random                                         | Bonus!!!

# Dependencies to run the Flask/Jinja Application

```
Flask==1.1.2
pytest==6.2.3
pytest-cov==2.11.1
Jinja2==2.11.3
jsonpickle
```

# Dependencies for the command line application

```
Flask==1.1.2
pytest==6.2.3
pytest-cov==2.11.1
Jinja2==2.11.3
```

# To run the Flask application
```
cd html 
flask run --port 8080
```

# To run do:
```
cd hw1
pytest
```

#To run the command-line tool do:
```
python randopoll.py ./data/participants.csv
```
#To commit the changes in the execution do
```
python randopoll.py ./data/participants.csv -c "Commit message"
```
#To commit the changes and push in the execution do
```
python randopoll.py ./data/participants.csv  -c "Commit message" -p
```