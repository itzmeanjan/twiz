#!/usr/bin/python3

from __future__ import annotations

from typing import List, Dict, Any
from .tweet import Tweet


class Tweets:
    def __init__(self, _all: List[Tweet]):
        self.all = _all

    @staticmethod
    def build(data: List[Dict[str, Any]]) -> Tweets:
        tweets = Tweets([])

        tweets.all = list(filter(lambda e: e, map(
            lambda e: Tweet.build(e.get('tweet', {})), data)))

        return tweets


if __name__ == '__main__':
    print('[!] This is not an executable script')
