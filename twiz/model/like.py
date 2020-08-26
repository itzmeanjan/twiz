#!/usr/bin/python3

from typing import List, Tuple, Dict, Any
from re import compile as regCompile, I as regI, Pattern
from itertools import chain
from collections import Counter


def getLikes(data: List[Dict[str, Any]]) -> map:
    '''
        Extract likes & returns stream of tuples, where each of the tuples are
        going to be of form ('id', 'text', 'url')
    '''

    def _helper(obj: Dict[str, Any]) -> Tuple[str, str, str]:
        _like = obj['like']

        return _like['tweetId'], _like['fullText'], _like['expandedUrl']

    return map(_helper, data)


def _getHashTagRegex() -> Pattern:
    '''
        HashTag finder regular expression
    '''
    return regCompile(r'(\#\w+)')


def countOfHashTags(data: map) -> Counter:
    '''
        Returns count of each hashtags found in liked tweets
    '''
    _regex = _getHashTagRegex()

    return Counter(chain.from_iterable(map(lambda e: _regex.findall(e[1]),
                                           data)))


def topXHashTagsInLikedTweets(data: map, x: int) -> List[Tuple[str, int]]:
    '''
        Returns list of top X most used hash tags found in liked tweets
    '''
    return countOfHashTags(data).most_common(x)


def _getTaggedUserRegex() -> Pattern:
    '''
        Regular expression for finding tagged users
    '''
    return regCompile(r'(@\w+)')


def countOfTaggedUsers(data: map) -> Counter:
    '''
        Returns how many times each tagged user name found in liked tweets
    '''
    _regex = _getTaggedUserRegex()

    return Counter(chain.from_iterable(map(lambda e: _regex.findall(e[1]),
                                           data)))


def topXTaggedUsersInLikedTweets(data: map, x: int) -> List[Tuple[str, int]]:
    '''
        Returns list of top X mostly tagged usernames found in liked tweets
    '''
    return countOfTaggedUsers(data).most_common(x)


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
