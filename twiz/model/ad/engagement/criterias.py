#!/usr/bin/python3

from typing import List
from .criteria import MatchedCriteria


class MatchedCriterias:
    def __init__(self, all: List[MatchedCriteria]):
        self._all = all

    def all(self) -> List[MatchedCriteria]:
        return self._all


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
