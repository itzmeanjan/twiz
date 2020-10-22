#!/usr/bin/python3

from __future__ import annotations

from typing import List, Dict, Any
from .tweet import Tweet

from itertools import chain
from collections import Counter
from datetime import timedelta, datetime


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

    def dateToTweetCount(self) -> Dict[datetime, int]:
        '''
            Mapping all tweets to their respective date of occurance,
            giving us daily tweet count
        '''
        dates = dict(Counter(map(lambda e: e.createdAt.date(), self.all)))
        _min = min(dates)
        _max = max(dates)

        buffer = dict()

        while _min <= _max:
            buffer[_min] = dates.get(_min, 0)

            _min += timedelta(days=1)

        return buffer

    def getAllHashTags(self) -> str:
        '''
            Retrieves all hashtags by concatenating them with `\n`, to be used
            for creating word cloud of hashtags mostly used by this user
        '''
        return '\n'.join(map(lambda e: f'#{e}', chain.from_iterable(map(lambda e: e.hashtags, self.all))))

    def getAllTaggedUsers(self) -> str:
        '''
            Generating a concatenation of @user mentions, found in tweets by user,
            user names are seperated by `\n`
        '''
        return '\n'.join(chain.from_iterable(map(lambda e: map(lambda e: f'@{e.screenName}', e.mentions), self.all)))


if __name__ == '__main__':
    print('[!] This is not an executable script')
