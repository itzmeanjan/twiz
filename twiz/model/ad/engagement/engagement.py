#!/usr/bin/python3

from __future__ import annotations
from .device import DeviceInfo
from .tweet import Tweet
from .advertiser import Info
from .criteria import MatchedCriteria
from .attributes import EngagementAttributes
from datetime import datetime
from typing import List, Dict, Any


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

    @staticmethod
    def build(data: Dict[str, Any]) -> Engagement:
        impressionAttr = data['impressionAttributes']
        engagementAttr = data['engagementAttributes']

        return Engagement(
            DeviceInfo(impressionAttr['deviceInfo']['osType'],
                       impressionAttr['deviceInfo']['deviceId']),
            impressionAttr['displayLocation'],
            Tweet(
                impressionAttr['promotedTweetInfo']['tweetId'],
                impressionAttr['promotedTweetInfo']['tweetText'],
                impressionAttr['promotedTweetInfo']['urls'],
                impressionAttr['promotedTweetInfo']['mediaUrls']
            ),
            Info(
                impressionAttr['advertiserInfo']['advertiserName'],
                impressionAttr['advertiserInfo']['screenName']
            ),
            [MatchedCriteria(i['targetingType'], i['targetingValue'])
             for i in impressionAttr['matchedTargetingCriteria']],
            impressionAttr['impressionTime'],
            [EngagementAttributes(i['engagementTime'], i['engagementType'])
             for i in engagementAttr]
        )


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
