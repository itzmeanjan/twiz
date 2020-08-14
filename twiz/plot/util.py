#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from copy import deepcopy
from ..model.manip import getFollowedFollowers


def _prepareDataForPlottingFollowersAndFollowings(followers: map, followings: map) -> List[Tuple[str, int]]:
    '''
        Prepare data to be plotted showing followers, followings & followers whom you follow too
    '''
    followerCount = len(list(deepcopy(followers)))
    followingCount = len(list(deepcopy(followings)))
    followedFollowers = len(getFollowedFollowers(followers,
                                                 followings))

    return [('Followers', followerCount), ('Followings', followingCount), ('Followers followed by YOU', followedFollowers)]


def plotFollowersAndFollowings(followers: map, followings: map, title: str, sink: str) -> bool:
    '''
        Plotting follower & following data as bar chart
    '''
    try:
        _data = _prepareDataForPlottingFollowersAndFollowings(followers,
                                                              followings)

        _x = [i[0] for i in _data]
        _y = [i[1] for i in _data]

        fig = plt.Figure(figsize=(16, 9), dpi=100)

        sns.set_style('darkgrid')

        sns.barplot(x=_x, y=_y, ax=fig.gca())
        fig.gca().set_ylabel('Count')
        fig.gca().set_title(title, fontsize=22)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
