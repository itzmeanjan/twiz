#!/usr/bin/python3

from .device import DeviceInfo
from .tweet import Tweet
from .advertiser import Info
from .criteria import MatchedCriteria
from .attributes import EngagementAttributes
from datetime import datetime
from typing import List


class Engagement:
    def __init__(self, device: DeviceInfo, location: str, tweet: Tweet,
                 advertiser: Info, criterias: List[MatchedCriteria],
                 time: str, attrs: List[EngagementAttributes]):
        self.device = device
        self.displayLocation = location
        self.tweet = tweet
        self.advertiser = advertiser
        self.criterias = criterias
        self.time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        self.attrs = attrs


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
