#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from twiz.model.ad.engagement.engagements import Engagements
from functools import reduce
from itertools import chain


def plotAdTargetDeviceTypes(data: Engagements, title: str, sink: str) -> bool:
    try:
        _tmp = data.countByDeviceType()
        x = list(_tmp.keys())
        y = [_tmp[i] for i in x]

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=x, y=y, ax=fig.gca())

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           y[i],
                           ha='center',
                           rotation=0,
                           fontsize=14,
                           color='black')

        fig.gca().set_title(title, fontsize=20, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.8)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotPercentageOfShownAdsByLocationOfDisplay(data: Engagements, title: str, sink: str) -> bool:
    try:
        _tmp = data.percentageOfAdsByDisplayLocation()
        x = [i[0] for i in _tmp]
        y = [i[1] for i in _tmp]

        _counts = data.countByDisplayLocation()
        _counts = [_counts[i] for i in x]

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(16, 9), dpi=100)

            sns.barplot(x=x, y=y, ax=fig.gca(), palette='BuGn_r')

            for i, j in enumerate(fig.gca().patches):
                fig.gca().text(j.get_x() + j.get_width() * .5,
                               j.get_y() + j.get_height() * .5,
                               _counts[i],
                               ha='center',
                               rotation=0,
                               fontsize=16,
                               color='white')

            fig.gca().set_ylim(0, 100)
            fig.gca().set_title(title, fontsize=20, pad=14)
            fig.tight_layout(pad=4)

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


def _prepareDataForTwitterAdsGroupedByDeviceTypeAndDisplayLocation(data: Engagements) -> Tuple[List[str], List[int], List[str]]:
    '''
        Preparing data for plotting group bar chart, depicting how many twitter ads
        were shown on which device & how many in each of them were shown on which portion
        of display
    '''
    _tmp = data.groupAdCountByDeviceTypeAndDisplayLocation()
    _displayLocations = list(set(reduce(
        lambda acc, cur: acc + list(cur),
        map(lambda e: e.keys(), _tmp.values()), [])))

    _x = list(chain.from_iterable(
        [[i] * len(_displayLocations) for i in _tmp.keys()]))
    _y = [_tmp[j].get(_displayLocations[i % len(_displayLocations)], 0)
          for i, j in enumerate(_x)]
    _hue = list(chain.from_iterable(
        [_displayLocations * (len(_x) // len(_displayLocations))]))

    return _x, _y, _hue


def plotShownAdsGroupedByDeviceTypeAndDisplayLocation(data: Engagements, title: str, sink: str) -> bool:
    '''
        Plotting grouped bar chart, showing how many twitter ads
        were shown on which device & how many in each of them 
        were shown on which portion of display
    '''
    try:
        _x, _y, _hue = _prepareDataForTwitterAdsGroupedByDeviceTypeAndDisplayLocation(
            data)

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(16, 9), dpi=100)

            sns.barplot(x=_x, y=_y, hue=_hue,
                        ax=fig.gca(), palette='PuRd')

            fig.gca().set_title(title, fontsize=20, pad=14)
            fig.tight_layout(pad=4)

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
