# Contributing Guidelines

As a newcomer to python, any suggestions are welcome.

## Installation

### Virtual Environments and pip dev_requirements
I used [https://docs.python.org/3/tutorial/venv.html](venv) when creating this library, so probably best to do the same.

After activating your virtual environment, you can then run `pip install -r dev_requirements.txt`

## Testing and Coverage

To run unit tests:
```
python3 -m unittest discover -s tests/
```

To check unit-test code coverage:
```
coverage run --source=rugby_rankings -m unittest discover -s tests/
coverage report -m
```

## Pylint and code standards

This project uses PEP8 standards.

To run pylint on this project:
```
pylint --rcfile=pylintrc rugby_rankings
```
