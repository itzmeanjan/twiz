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
        _followerCount = len(list(map(lambda e: e[0], deepcopy(followers))))
        _followingCount = len(list(map(lambda e: e[0], deepcopy(followings))))
        _commonCount = len(getFollowedFollowers(deepcopy(followers),
                                                deepcopy(followings)))

        fig, axes = plt.subplots(1, 2,
                                 sharey=True,
                                 figsize=(16, 9),
                                 dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=['Followers : {}'.format(_followerCount),
                       'Followers whom YOU followed back : {}'.format(_commonCount)],
                    y=[100, (_commonCount * 100) / _followerCount],
                    ax=axes[0])
        sns.barplot(x=['Followings : {}'.format(_followingCount),
                       'Followings who\'re following YOU : {}'.format(_commonCount)],
                    y=[100, (_commonCount * 100) / _followingCount],
                    ax=axes[1])
        axes[0].set_ylim(0, 100)
        axes[1].set_ylim(0, 100)
        axes[0].set_title(title[0], pad=4)
        axes[1].set_title(title[1], pad=4)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
