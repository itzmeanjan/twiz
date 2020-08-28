#!/usr/bin/python3

from typing import List


class Tweet:
    def __init__(self, id: str, text: str, urls: List[str], mediaUrls: List[str]):
        self.id = id
        self.text = text
        self.urls = urls
        self.mediaUrls = mediaUrls


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
