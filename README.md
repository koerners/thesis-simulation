# Cross-Generational Agent-Based Altruism Simulation

[![Lint and Test](https://github.com/koerners/thesis-simulation/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/koerners/thesis-simulation/actions/workflows/pytest.yml)

## Purpose
The most popular theories regarding the evolution of altruistic traits in humans are put to the test in a series of cross-generational agent-based simulations that mimic natural selection according to Darwin's three principles of inheritance, variation, and selection. The focus is put on the environmental circumstances that may have led to the evolution of altruism according to each of these theories.

## Setup

1. Install pip ```python -m ensurepip --upgrade```
2. Install pipenv ```pip install pipenv```
3. Install dependencies ```pipenv install```
4. Run simulation ```pipenv run start``` or get possible arguments with ```--help```
5. Analyze the generated data using ```pipenv run analyze```
6. Clear ```.out/``` with ```pipenv run clear```

## Options

```
usage: pipenv run start [-h] -m MODEL [-p PROCESSES] [-i ITERATIONS] [-s STEPS]

arguments:
  -h, --help                              show this help message and exit
  -m MODEL, --Model MODEL                 Model to run. Options: baseline, greenbeard, kinselection, group, culture, reputation
  -p PROCESSES, --Processes PROCESSES     Number of processes used
  -i ITERATIONS, --Iterations ITERATIONS  Number of iterations
  -s STEPS, --Steps STEPS                 Steps the simulation is run
```

## Development

Install the development dependencies with ```pipenv install --dev```.

- Run the formatter with ```pipenv run format```
- Run the linter with ```pipenv run lint```
- Run tests with ```pipenv run test```

## Structure
These diagrams are updated automatically by the pipeline when a new commit is pushed to the main branch.
### Models

![UML-Models](https://github.com/koerners/thesis-simulation/blob/main/uml/classes_Models.png)

### Agents

![UML-Models](https://github.com/koerners/thesis-simulation/blob/main/uml/classes_Agents.png)
