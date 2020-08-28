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

        return Engagement(
            DeviceInfo(impressionAttr['deviceInfo'].get('osType'),
                       impressionAttr['deviceInfo'].get('deviceId')),
            impressionAttr.get('displayLocation'),
            Tweet(
                impressionAttr.get('promotedTweetInfo', {}).get('tweetId'),
                impressionAttr.get('promotedTweetInfo', {}).get('tweetText'),
                impressionAttr.get('promotedTweetInfo', {}).get('urls'),
                impressionAttr.get('promotedTweetInfo', {}).get('mediaUrls')
            ),
            Info(
                impressionAttr['advertiserInfo']['advertiserName'],
                impressionAttr['advertiserInfo']['screenName']
            ),
            [MatchedCriteria(i.get('targetingType'), i.get('targetingValue'))
             for i in impressionAttr.get('matchedTargetingCriteria', [])],
            impressionAttr['impressionTime'],
            [EngagementAttributes(i['engagementTime'], i['engagementType'])
             for i in data['engagementAttributes']])


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
