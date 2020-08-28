#!/usr/bin/python3

from typing import List
from re import compile as regCompile, I as regI, Pattern


class Tweet:
    def __init__(self, id: str, text: str, urls: List[str], mediaUrls: List[str]):
        self.id = id
        self.text = text
        self.urls = urls
        self.mediaUrls = mediaUrls

    def _tagRegex(self) -> Pattern:
        return regCompile(r'(@\w+)')

    def extractTags(self) -> List[str]:
        return self._tagRegex().findall(self.text)

    def _hashTagRegex(self) -> Pattern:
        return regCompile(r'(\#\w+)')

    def extractHashTags(self) -> List[str]:
        return self._hashTagRegex().findall(self.text)


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
