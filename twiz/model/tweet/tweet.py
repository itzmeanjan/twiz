#!/usr/bin/python3

from __future__ import annotations

from typing import List, Dict, Any, Tuple
from .mention import Mention
from .url import URL
from datetime import datetime
from dateutil.parser import parse as date_parser


class Tweet:
    def __init__(self):
        self.retweeted: bool = False
        self.retweetCount: int = 0
        self.favorited: bool = False
        self.favoriteCount: int = 0
        self.id: str = ''
        self.possiblySensitive: bool = False
        self.createdAt: datetime = None
        self.language: str = ''
        self.text: str = ''
        self.hashtags: Tuple[str] = tuple()
        self.mentions: Tuple[Mention] = tuple()
        self.urls: Tuple[URL] = tuple()

    @staticmethod
    def build(data: Dict[str, Any]) -> Tweet:
        if not data:
            return None

        tweet = Tweet()

        tweet.retweeted = data.get('retweeted', False)
        tweet.retweetCount = int(data.get('retweet_count', 0))
        tweet.favorited = data.get('favorited', False)
        tweet.favoriteCount = int(data.get('favorite_count', 0))
        tweet.id = data.get('id')
        tweet.possiblySensitive = data.get('possibly_sensitive', False)
        tweet.createdAt = date_parser(data['created_at'])
        tweet.language = data.get('lang')
        tweet.text = data.get('full_text')

        tweet.hashtags = tuple(
            map(lambda e: e.get('text'), data.get('entities', {}).get('hashtags', [])))
        tweet.mentions = tuple(map(lambda e: Mention(e.get('name'), e.get(
            'screen_name'), e.get('id')), data.get('entities', {}).get('user_mentions', [])))
        tweet.urls = tuple(map(lambda e: URL(e.get('url'), e.get(
            'expanded_url')), data.get('entities', {}).get('urls', [])))

        return tweet


if __name__ == '__main__':
    print('[!] This is not an executable script')
