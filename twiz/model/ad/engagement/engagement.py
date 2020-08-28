#!/usr/bin/python3

from .device import DeviceInfo
from .tweet import Tweet
from .advertiser import Info
from .criterias import MatchedCriterias
from .attributes import EngagementAttributes


class Engagement:
    def __init__(self, device: DeviceInfo, tweet: Tweet, advertiser: Info, criterias: MatchedCriterias, attr: EngagementAttributes):
        self.device = device
        self.tweet = tweet
        self.advertiser = advertiser
        self.criterias = criterias
        self.attr = attr


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
