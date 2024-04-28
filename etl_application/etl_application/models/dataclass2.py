from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass
class class_a:
    pass


class class_b:
    """This class creates instances of the ....t"""

    def __init__(self, data):
        self.data = data
        self.leaderboard = []

    def parse(self):
        for data in self.data:
            self.leaderboard.append(class_a.from_dict(data))
        return self.leaderboard
