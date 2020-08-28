#!/usr/bin/python3

from dataclasses import dataclass
from datetime import datetime


@dataclass
class EngagementAttributes:
    _time: str
    type: str

    def time(self) -> datetime:
        return datetime.strptime(self._time, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
