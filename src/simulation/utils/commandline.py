import argparse


class Commandline:
    def __init__(self):
        # Initialize parser
        _parser = argparse.ArgumentParser()

        # Adding optional argument
        _parser.add_argument("-p", "--Processes",
                             help="Number of processes used")

        _parser.add_argument("-i", "--Iterations",
                             help="Number of iterations")

        _parser.add_argument("-s", "--Steps",
                             help="Max steps")

        # Read arguments from command line
        _args = _parser.parse_args()

        self._nr_of_processes = int(_args.Processes) if _args.Processes else 1
        self._iterations = int(_args.Iterations) if _args.Iterations else 1
        self._max_steps = int(_args.Steps) if _args.Steps else 100

    @property
    def nr_of_processes(self):
        return self._nr_of_processes

    @property
    def iterations(self):
        return self._iterations

    @property
    def max_steps(self):
        return self._max_steps
