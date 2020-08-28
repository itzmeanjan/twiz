#!/usr/bin/python3

from __future__ import annotations
from .engagement import Engagement
from typing import List, Dict, Any, Tuple
from itertools import chain
from collections import Counter


class Engagements:
    def __init__(self, all: List[Engagement]):
        self.all = all

    @staticmethod
    def build(data: Dict[str, Any]) -> Engagements:
        return Engagements(list(
            chain.from_iterable(
                [[Engagement.build(j) for j in i['ad']['adsUserData']
                  ['adEngagements']['engagements']] for i in data])))

    def countByDeviceType(self) -> Counter:
        return Counter(filter(lambda e: e,
                              map(lambda e: e.device.type,
                                  self.all)))


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
