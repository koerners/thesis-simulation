from mesa import Agent

class BaseAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.model = model
        self.model.network.add_node(self)

    def die(self):
        self.model.network.remove_node(self)
        self.model.schedule.remove(self)
