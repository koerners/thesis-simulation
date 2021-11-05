from mesa import Agent


class BaseAgent(Agent):
    def __init__(self, model, group=None):
        self.unique_id = model.next_id()
        self.group = group
        super().__init__(model=model, unique_id=self.unique_id)
        self.model.schedule.add(self)
        self.model.network.add_node(self)

    def die(self) -> None:
        self.model.network.remove_node(self)
        self.model.schedule.remove(self)

    def step(self) -> None:
        pass
