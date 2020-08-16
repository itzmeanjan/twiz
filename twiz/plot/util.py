#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from copy import deepcopy
from ..model.manip import (
    getFollowersAndFollowingsPerCent,
    getFollowedFollowers
)


def plotFollowersAndFollowings(followers: map, followings: map, title: str, sink: str) -> bool:
    '''
        Plotting follower & following data as bar chart
    '''
    try:
        _data = getFollowersAndFollowingsPerCent(deepcopy(followers),
                                                 deepcopy(followings))
        fig = plt.Figure(figsize=(16, 9), dpi=100)

        sns.set_style('darkgrid')

        sns.barplot(x=['Followers', 'Followings'], y=_data, ax=fig.gca())
        fig.gca().set_ylim(0, 100)
        fig.gca().set_title(title, fontsize=22, pad=10)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotFollowersAndFollowedFollowers(followers: map, followings: map, title: str, sink: str) -> bool:
    '''
        Plotting followers & followed followers ( i.e. 
        followers whom you follow back ) data as bar chart
    '''
    try:
        fig = plt.Figure(figsize=(16, 9), dpi=100)

        sns.set_style('darkgrid')

        sns.barplot(x=['Followers',
                       'Followed back Followers'],
                    y=[100,
                       len(getFollowedFollowers(deepcopy(followers),
                                                deepcopy(followings)))],
                    ax=fig.gca())
        fig.gca().set_ylim(0, 100)
        fig.gca().set_title(title, fontsize=22, pad=10)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
