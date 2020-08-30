#!/usr/bin/python3

from __future__ import annotations
from .engagement import Engagement
from typing import List, Dict, Any, Tuple
from itertools import chain
from collections import Counter
from functools import reduce


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

    def countByDisplayLocation(self) -> Counter:
        '''
            Counts how many twitter ads were displayed on which location
            of your profile while you were browsing twitter
        '''
        return Counter(map(lambda e: e.displayLocation, self.all))

    def percentageOfAdsByDisplayLocation(self) -> List[Tuple[str, float]]:
        '''
            Percentage distribution of total ads shown on twitter to YOU,
            in terms of location of ad display
        '''
        _buffer = self.countByDisplayLocation()
        _total = sum(_buffer.values())

        return [(i, (_buffer[i] / _total) * 100) for i in sorted(_buffer,
                                                                 key=lambda e: _buffer[e],
                                                                 reverse=True)]

    def groupAdCountByDeviceTypeAndDisplayLocation(self) -> Dict[str, Counter]:
        '''
            Distribution of shown twitter ads by device type & respective location
            of display on device
        '''
        def _groupByDeviceType(acc: Dict[str, List[str]], cur: Tuple[str, str]) -> Dict[str, List[str]]:
            if cur[0] in acc:
                acc[cur[0]].append(cur[1])
            else:
                acc[cur[0]] = [cur[1]]

            return acc

        return dict(map(lambda e: (e[0], Counter(e[1])),
                        reduce(_groupByDeviceType,
                               map(lambda e: (e.device.type, e.displayLocation),
                                   self.all),
                               {}).items()))


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
