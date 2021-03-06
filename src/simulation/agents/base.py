from mesa import Agent


class BaseAgent(Agent):
    def __init__(self, model, group=None, is_altruist=False):
        self.unique_id: int = model.next_id()
        self.group: str = group
        super().__init__(model=model, unique_id=self.unique_id)
        self.model.schedule.add(self)
        self.model.network.add_node(self)
        self.is_altruist = is_altruist

    def die(self):
        self.model.network.remove_node(self)
        self.model.schedule.remove(self)

    def step(self):
        pass
