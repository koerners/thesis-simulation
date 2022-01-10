import argparse


class Commandline:
    def __init__(self):
        # Initialize parser
        _parser = argparse.ArgumentParser()

        _parser.add_argument(
            "-m",
            "--Model",
            required=True,
            help="Model to run. \
            Options: baseline, greenbeard, kinselection, group, culture, reputation",
        )

        # Adding optional argument
        _parser.add_argument("-p", "--Processes", help="Number of processes used")

        _parser.add_argument("-i", "--Iterations", help="Number of iterations")

        _parser.add_argument("-s", "--Steps", help="Steps the simulation is run")

        # Read arguments from command line
        _args = _parser.parse_args()

        self._nr_of_processes = int(
            _args.Processes) if _args.Processes else None
        self._iterations = int(_args.Iterations) if _args.Iterations else 1
        self._max_steps = int(_args.Steps) if _args.Steps else 100
        self._model = _args.Model

    @property
    def nr_of_processes(self) -> int:
        return self._nr_of_processes

    @property
    def iterations(self) -> int:
        return self._iterations

    @property
    def max_steps(self) -> int:
        return self._max_steps

    @property
    def model(self) -> str:
        return self._model
