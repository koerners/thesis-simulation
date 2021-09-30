import os

import pandas as pd


def get_saved_runs():
    runs = [name for name in os.listdir(
        './out') if os.path.isdir(os.path.join('./out', name))]
    return sorted(runs)


def get_iterations(run_id):
    iterations = [name for name in os.listdir(
        f"./out/{run_id}") if os.path.isdir(os.path.join(f"./out/{run_id}", name))]
    return iterations


def get_run_data(run_id):
    print(f"Loading data for {run_id}")
    try:
        return pd.read_pickle(f"./out/{run_id}/run_data.pkl")
    except IOError as error:
        print(error)
        return None


def get_iteration_networks(run_id, iteration_id, step=None):
    network_files = [f for f in os.listdir(
        f"./out/{run_id}/{iteration_id}") if
        os.path.isfile(os.path.join(f"./out/{run_id}/{iteration_id}", f))]
    if step is not None:
        for file in network_files:
            if file == f"Step_{step}.pkl":
                return file
    return network_files
