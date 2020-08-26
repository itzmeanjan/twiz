#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from copy import deepcopy
from ..model.manip import (
    getFollowersAndFollowingsPerCent,
    getFollowedFollowers
)
from ..model.like import (
    topXHashTagsInLikedTweets,
    topXTaggedUsersInLikedTweets,
    topXEmojisInLikedTweets
)
from emoji import demojize
from textwrap import wrap


def plotFollowersAndFollowings(followers: map, followings: map, title: str, sink: str) -> bool:
    '''
        Plotting follower & following data as bar chart
    '''
    try:
        _data = getFollowersAndFollowingsPerCent(deepcopy(followers),
                                                 deepcopy(followings))
        _followerCount = len(list(map(lambda e: e[0],
                                      deepcopy(followers))))
        _followingCount = len(list(map(lambda e: e[0],
                                       deepcopy(followings))))

        fig = plt.Figure(figsize=(16, 9), dpi=100)

        sns.set_style('darkgrid')

        sns.barplot(x=['Followers', 'Followings'], y=_data, ax=fig.gca())

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           ['Count: {} [ {:.2f}% ]'.format(_followerCount, _data[0]),
                            'Count: {} [ {:.2f}% ]'.format(_followingCount, _data[1])][i],
                           ha='center',
                           rotation=0,
                           fontsize=14,
                           color='black')

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

        sns.barplot(x=['Followers',
                       'Followers whom YOU followed back'],
                    y=[100, (_commonCount * 100) / _followerCount],
                    ax=axes[0])

        for i, j in enumerate(axes[0].patches):
            axes[0].text(j.get_x() + j.get_width() * .5,
                         j.get_y() + j.get_height() * .5,
                         [_followerCount, _commonCount][i],
                         ha='center',
                         rotation=0,
                         fontsize=14,
                         color='black')

        sns.barplot(x=['Followings',
                       'Followings who\'re following YOU'],
                    y=[100, (_commonCount * 100) / _followingCount],
                    ax=axes[1])

        for i, j in enumerate(axes[1].patches):
            axes[1].text(j.get_x() + j.get_width() * .5,
                         j.get_y() + j.get_height() * .5,
                         [_followingCount, _commonCount][i],
                         ha='center',
                         rotation=0,
                         fontsize=14,
                         color='black')

        axes[0].set_ylim(0, 100)
        axes[1].set_ylim(0, 100)
        axes[0].set_title(title[0], pad=4)
        axes[1].set_title(title[1], pad=4)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotTopXHashTagsFoundInLikedTweets(likes: map, x: int, title: str, sink: str) -> bool:
    '''
        Plotting top X most found hash tags in tweets liked by YOU as bar plot
    '''
    try:
        _data = topXHashTagsInLikedTweets(deepcopy(likes), x)
        _x, _y = [], []
        for i in _data:
            _x.append(i[0])
            _y.append(i[1])

        fig = plt.Figure(figsize=(16, 9), dpi=100)

        sns.set_style('darkgrid')

        sns.barplot(x=_x, y=_y, ax=fig.gca())

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           _y[i],
                           ha='center',
                           rotation=0,
                           fontsize=15,
                           color='black')

        fig.gca().set_title(title, fontsize=22, pad=10)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotTopXTaggedUsersFoundInLikedTweets(likes: map, x: int, title: str, sink: str) -> bool:
    '''
        Plotting top X most found tagged user names in tweets liked by YOU as bar plot
    '''
    try:
        _data = topXTaggedUsersInLikedTweets(deepcopy(likes), x)
        _x, _y = [], []
        for i in _data:
            _x.append(i[1])
            _y.append(i[0])

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=_x, y=_y, ax=fig.gca(), orient='h')

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           _x[i],
                           ha='center',
                           rotation=0,
                           fontsize=16,
                           color='black')

        fig.gca().set_title(title, fontsize=22, pad=10)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotTopXEmojisFoundInLikedTweets(likes: map, x: int, title: str, sink: str) -> bool:
    '''
        Plotting top X most found emojis ( in demojized form i.e. text 
        based representation ) in tweets liked by YOU as bar plot
    '''
    try:
        _data = topXEmojisInLikedTweets(deepcopy(likes), x)
        _x, _y = [], []
        for i in _data:
            _x.append(i[1])
            _y.append(i[0])

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=_x,
                    y=['\n'.join(wrap(' '.join([j.capitalize() for j in demojize(
                        i).strip(':').split('_')]), width=16)) for i in _y],
                    ax=fig.gca(), orient='h')

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           _x[i],
                           ha='center',
                           rotation=0,
                           fontsize=16,
                           color='black')

        fig.gca().set_title(title, fontsize=22, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.5)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
