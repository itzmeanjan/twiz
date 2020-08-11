#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from copy import deepcopy
from ..model.manip import getBothFollowersAndFollowings


def _prepareDataForPlottingFollowersAndFollowings(followers: map, followings: map) -> List[Tuple[str, int]]:
    '''
        Prepare data to be plotted showing followers, followings & followers whom you follow too
    '''
    followerCount = len(list(deepcopy(followers)))
    followingCount = len(list(deepcopy(followings)))
    followedFollowers = len(getBothFollowersAndFollowings(followings,
                                                          followers))

    return [('Followers', followerCount), ('Followings', followingCount), ('Followers followed by YOU', followedFollowers)]


def plotFollowersAndFollowings():
    pass


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
