class Group:
    # pylint:disable=too-few-public-methods
    def __init__(self, group_id):
        self.group_id = group_id  # A, B, C ...


class CultureGroup(Group):
    def __init__(self, group_id, group_culture):
        self.group_culture = group_culture  # val between 0 and 1
        super().__init__(group_id=f"{group_id}-{group_culture}")  # A, B, C ...

    def agent_acted_altruistic(self):
        self.group_culture = min(self.group_culture + 0.0001, 1)

    def agent_acted_non_altruistic(self):
        self.group_culture = max(0, self.group_culture - 0.0001)
