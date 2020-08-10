#!/usr/bin/python3

from typing import List, Dict, Any


def getFollowings(data: List[Dict[str, Any]]) -> map:
    '''
        Obtains a list of followings, where each of them will be a
        tuple of accountId & corresponding user's account link
    '''
    return map(lambda e: (e['following']['accountId'],
                          e['following']['userLink']), data)


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
