#!/usr/bin/python3

from typing import Set, List


def getFollowedFollowers(followers: map, followings: map) -> Set[str]:
    '''
        Computes list of those followings who follow you back or in other terms
        followers whom you follow back
    '''
    return set(map(lambda e: e[0], followers)).intersection(
        set(map(lambda e: e[0], followings)))


def getFollowersAndFollowingsPerCent(followers: map, followings: map) -> List[float]:
    '''
        Scaling down number of followers & followings to 100 i.e. per cent of each of these categories
    '''
    _tmp = list(map(lambda e: len(list(e)), [followers, followings]))

    return [(i / sum(_tmp)) * 100 for i in _tmp]


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
