#!/usr/bin/python3

from typing import List, Dict, Any


def getFollowers(data: List[Dict[str, Any]]) -> map:
    '''
        Obtains a list of followers, where each of them will be a
        tuple of accountId & corresponding user's account link
    '''
    return map(lambda e: (e['follower']['accountId'],
                          e['follower']['userLink']), data)


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
