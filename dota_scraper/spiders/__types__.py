
from typing import List
from traitlets.traitlets import default
from abc import ABC

class CountersQueryParams(ABC):
    values: List[str] = [
        'week',
        'month',
        '3month',
        '6month',
        'year']

    def get_last_index(self):
        return len(self.values)
