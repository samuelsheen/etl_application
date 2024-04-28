from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass
class class1:
    column1: int
    column2: int


@dataclass_json()
@dataclass
class class2:
    column1: str
    column2: str
    column3: Optional[str]
    column4: Optional[str]
    column5: str


class class3:
    """This class parses dicts to instances of the class2 class"""

    def __init__(self, data):
        self.data = data

    def parse(self):
        return class2.from_dict(self.data)
