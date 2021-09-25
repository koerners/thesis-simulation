from mesa.datacollection import DataCollector


def get_total_agent_count(self) -> int:
    return self.schedule.get_agent_count()


def get_experiment_id(self) -> int:
    return self.experiment_id


def get_data_collector(self) -> DataCollector:
    return self.datacollector


def get_current_network(self):
    return self.network
