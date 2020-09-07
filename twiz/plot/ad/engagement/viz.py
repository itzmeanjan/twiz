#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List, Tuple
from twiz.model.ad.engagement.engagements import Engagements
from functools import reduce
from itertools import chain
from collections import Counter


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


def plotAdsCountGroupedByAdvertiserNames(data: Engagements, x: int, title: str, sink: str) -> bool:
    '''
        We're going to plot how many ads user has engaged in from certain advertiser,
        as a bar plot. Top X advertisers to be plotted, denoted by their name, userid omitted.
    '''
    try:
        _ads = data.topXAdvertiserNames(x)

        _x = [i[1] for i in _ads]
        _y = [i[0] for i in _ads]

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(16, 9), dpi=100)

            sns.barplot(x=_x, y=_y, ax=fig.gca(),
                        palette='PuRd', orient='h')

            fig.gca().set_title(title, fontsize=20, pad=16)
            fig.tight_layout(pad=4)

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


def plotAdsCountGroupedByEngagementTypes(data: Engagements, x: int, title: str, sink: str) -> bool:
    '''
        Plotting ad count by grouping ads by their engagement types i.e.
        depicts how twitter ads were trying to engage you & in which way they happened
        mostly.
    '''
    try:
        _ads = data.topXEngagementTypes(x)

        _x = [i[1] for i in _ads]
        _sum = sum(_x)
        _y = [i[0] for i in _ads]

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(16, 9), dpi=100)

            sns.barplot(x=_x, y=_y, ax=fig.gca(),
                        palette='YlOrRd', orient='h')

            for i, j in enumerate(fig.gca().patches):
                fig.gca().text(j.get_x() + j.get_width() * .5,
                               j.get_y() + j.get_height() * .5,
                               '{:.2f} %'.format((_x[i] / _sum) * 100),
                               ha='center',
                               rotation=0,
                               fontsize=10,
                               color='black')

            fig.gca().set_title(title, fontsize=20, pad=16)
            fig.tight_layout()

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


def _prepareDataForTopXAdvertisersWithRespectiveEngagementTypes(data: Engagements, x: int) -> Tuple[List[str], List[str], List[List[str]]]:
    '''
        Preparing data for plotting heat map showing which of top advertisers used
        what kind of engagement types how many times. 
    '''
    _ads = data.topXAdvertiserNamesWithRespectiveEngagementTypes(x)

    _x = sorted(set(chain.from_iterable(
        [tuple(i.keys()) for i in _ads.values()])))
    _y = sorted(_ads, key=lambda e: sum(_ads[e].values()))

    _counts = [[_ads[i].get(j, 0) for j in _x] for i in _y]

    return _y, _x, _counts


def plotTopXAdvertisersAsHeatMap(data: Engagements, x: int, title: str, sink: str) -> bool:
    '''
        Plotting top X advertisers with their respective engagement type & count
        as heatmap
    '''
    try:
        _y, _x, _data =\
            _prepareDataForTopXAdvertisersWithRespectiveEngagementTypes(
                data, x)

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(18, 10), dpi=200)

            sns.heatmap(_data, lw=.75,
                        cmap='YlGnBu', ax=fig.gca())

            fig.gca().set_xticklabels(_x, rotation=72)
            fig.gca().tick_params(axis='x', which='major', labelsize=10)
            fig.gca().set_yticklabels(_y, rotation=0)
            fig.gca().tick_params(axis='y', which='major', labelsize=12)

            fig.gca().set_title(title, fontsize=20, pad=16)
            fig.tight_layout()

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


def _prepareDataForPlottingTargetCriteriasByAdvertiserName(data: Engagements, advertiser: str) -> map:
    def _prepareDataForTargetType(elem: str) -> Tuple[str, List[str], List[int]]:
        _x = sorted(_data[elem].keys(), key=lambda e: _data[elem][e])
        _y = [_data[elem][i] for i in _x]

        return elem, _x, _y

    _data = data.getGroupedTargetingCriteriasByAdvertiserName(advertiser)
    _keys = list(filter(lambda e: len(_data[e]) > 1, _data.keys()))

    return map(_prepareDataForTargetType, _keys)


def _joinName(name: str) -> str:
    return '_'.join(name.split())


def plotTargetCriteriasForTopXAdvertisers(data: Engagements, x: int, title: str, sink: str) -> bool:
    try:
        def _plot(advertiser: str, type: str, _x: List[str], _y: List[float]):
            with plt.style.context('dark_background'):
                fig = plt.Figure(figsize=(16, 9), dpi=100)

                sns.barplot(x=_y, y=_x, ax=fig.gca(),
                            palette='BuPu', orient='h')

                fig.gca().set_title('{}{} under {} category'.format(title, advertiser, type),
                                    fontsize=20, pad=16)
                fig.tight_layout()

                fig.savefig('{}{}{}.png'.format(sink, _joinName(advertiser), _joinName(type)),
                            pad_inches=.8)
                plt.close(fig)

        for k in data.topXAdvertiserNames(x):
            for v in _prepareDataForPlottingTargetCriteriasByAdvertiserName(data, k[0]):
                _plot(k[0], *v)

        return True
    except Exception:
        return False


def plotTopXTargetCriteriasUsedByTwitterAdvertisers(data: Engagements, x: int, title: str, sink: str) -> bool:
    '''
        Plotting a bar chart depicting which ad target criteria was used mostly for targeting you
    '''
    try:
        _criterias = data.topXAdTargetCriteriasUsed(x)

        _x = [i[1] for i in _criterias]
        _y = [i[0] for i in _criterias]

        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(16, 9), dpi=200)

            sns.barplot(x=_x, y=_y,
                        ax=fig.gca(),
                        palette='RdPu',
                        orient='h')

            fig.gca().set_title(title, fontsize=20, pad=16)
            fig.tight_layout()

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

        return True
    except Exception:
        return False


def _prepareDataForPlottingAdTargetCriteriaUsageGroupedByType(data: Engagements) -> map:
    '''
        Splitting ad target criteria usage count into X -axis data & Y -axis data,
        then creating a map _( lazy evaluation )_, where each element is a
        tuple of ad target criteria type & respective X, Y -axis value to be plotted.
    '''
    def _extractXAndY(v: Counter) -> Tuple[List[str], List[str]]:
        _x = list(v.keys())[:30]
        _y = [v[i] for i in _x]

        return _x, _y

    return map(lambda e: (e[0], *_extractXAndY(e[1])),
               data.adTargetCriteriaUsageCountGroupedByType().items())


def plotBarChartShowingAdTargetCriteriaUsageCountGroupedByType(data: Engagements, name: str):
    '''
        Plotting Twitter Ad target criterias used under each category 
        i.e. {Locations, Age, Follower look-alikes, Platforms, ...}, as bar plot
    '''
    def _plot(title: str, sink: str, _x: List[str], _y: List[str]):
        with plt.style.context('dark_background'):
            fig = plt.Figure(figsize=(24, 12), dpi=240)

            sns.barplot(x=_y, y=_x,
                        ax=fig.gca(),
                        palette='plasma',
                        orient='h')

            fig.gca().set_title(title, fontsize=18, pad=10)
            fig.tight_layout()

            fig.savefig(sink, pad_inches=.8)
            plt.close(fig)

    try:
        for i in _prepareDataForPlottingAdTargetCriteriaUsageGroupedByType(data):
            _plot('Using `{}` as Twitter Ad Target Criteria, for {}'.format(i[0], name),
                  'plots/twitterAdTargetCriteriasUsedIn{}For{}.png'.format(
                      _joinName(i[0]), _joinName(name)),
                  *i[1:])

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
