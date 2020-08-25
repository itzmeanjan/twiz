#!/usr/bin/python3

from typing import List, Tuple, Dict, Any
from re import compile as regCompile, I as regI, Pattern


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
        HashTag finded regular expression
    '''
    return regCompile(r'(\#\S+)')


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
