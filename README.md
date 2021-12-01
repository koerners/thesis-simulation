# Agent based altruism simulation

[![Lint and Test](https://github.com/koerners/thesis-simulation/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/koerners/thesis-simulation/actions/workflows/pytest.yml)

## Setup

1. Install pip ```python -m ensurepip --upgrade```
2. Install pipenv ```pip install pipenv```
3. Install dependencies ```pipenv install```
4. Run simulation ```pipenv run run``` or get possible arguments with ```--help```
5. Analyze the generated data using ```pipenv run analyze```
6. Clear ```.out/``` with ```pipenv run clear```

## Options

```
usage: run.py [-h] [-p PROCESSES] [-i ITERATIONS] [-s STEPS]

optional arguments:
  -h,            --help                     Show this help message and exit
  -p PROCESSES,  --Processes PROCESSES      Number of processes used
  -i ITERATIONS, --Iterations ITERATIONS    Number of iterations
  -s STEPS,      --Steps STEPS              Max steps
```


## Development

Install the development dependencies with ```pipenv install --dev```.

- Run the formatter with ```pipenv run format```
- Run the linter with ```pipenv run lint```
- Run tests with ```pipenv run test```


## Structure
### Models
![UML-Models](https://github.com/koerners/thesis-simulation/blob/main/uml/classes_Models.png)
### Agents
![UML-Models](https://github.com/koerners/thesis-simulation/blob/main/uml/classes_Agents.png)
