
from typing import Dict
import pandas as pd
from pandas.core.frame import DataFrame
from simulation.utils.directory import create_dir


def get_data_collector_for_step(collector) -> Dict:
    dictionary = collector.model_vars
    for delete in ['datacollector', 'experiment_id']:
        dictionary.pop(delete, None)
    return pd.DataFrame(dictionary)


def pre_edit_run_data(run_data) -> DataFrame:
    run_data.sort_index(axis=1, inplace=True)
    if 'datacollector' in run_data:
        run_data['datacollector'] = run_data['datacollector'].apply(
            get_data_collector_for_step)
    return run_data


def save_to_pickle(dataframe, path):
    full_path = create_dir(path)
    dataframe.to_pickle(full_path)
