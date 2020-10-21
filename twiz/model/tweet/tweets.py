#!/usr/bin/python3

from __future__ import annotations

from typing import List, Dict, Any
from .tweet import Tweet

from itertools import chain
from collections import Counter


class Tweets:
    def __init__(self, _all: List[Tweet]):
        self.all = _all

    @staticmethod
    def build(data: List[Dict[str, Any]]) -> Tweets:
        tweets = Tweets([])

        tweets.all = list(filter(lambda e: e, map(
            lambda e: Tweet.build(e.get('tweet', {})), data)))

        return tweets

    def hashTagToCount(self) -> Counter:
        '''
            Returns all hash tags and their respective occurance count
        '''
        return Counter(chain.from_iterable(map(lambda e: e.hashtags, self.all)))

    def topXHashTagsWithCount(self, x: int) -> List[Tuple[str, int]]:
        return self.hashTagToCount().most_common(x)

    def userMentionToCount(self) -> Counter:
        '''
            Returns which Twitter user has been mentioned how many times
            in tweets by USER
        '''
        return Counter(chain.from_iterable(map(lambda e: map(lambda e: f'{e.name} ( @{e.screenName} )', e.mentions), self.all)))

    def topXUserMentionsWithCount(self, x: int) -> List[Tuple[str, int]]:
        return self.userMentionToCount().most_common(x)


if __name__ == '__main__':
    print('[!] This is not an executable script')
