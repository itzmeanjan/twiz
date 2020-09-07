#!/usr/bin/python3

from argparse import ArgumentParser
from typing import Tuple, List
from os.path import exists, abspath, join
from .extract import extract, makeDirectory
from .parser import parse
from .model.follower import getFollowers
from .model.following import getFollowings
from .model.account import getAccountDisplayName
from .model.like import getLikes
from .model.ad.engagement.engagements import Engagements
from .plot.util import (
    plotFollowersAndFollowings,
    plotFollowersAndFollowedFollowers,
    plotTopXHashTagsFoundInLikedTweets,
    plotTopXTaggedUsersFoundInLikedTweets,
    plotTopXEmojisFoundInLikedTweets
)
from .plot.ad.engagement.viz import (
    plotAdTargetDeviceTypes,
    plotPercentageOfShownAdsByLocationOfDisplay,
    plotShownAdsGroupedByDeviceTypeAndDisplayLocation,
    plotAdsCountGroupedByAdvertiserNames,
    plotAdsCountGroupedByEngagementTypes,
    plotTopXAdvertisersAsHeatMap,
    plotTargetCriteriasForTopXAdvertisers,
    plotTopXTargetCriteriasUsedByTwitterAdvertisers,
    plotBarChartShowingAdTargetCriteriaUsageCountGroupedByType
)
from time import time


def _getCMD() -> Tuple[str, str]:
    parser = ArgumentParser(
        prog='twiz',
        description='twiz - Your Twitter Account Data Analysis & Visualization Tool <3')
    parser.add_argument('src', type=str, nargs=1,
                        help='Compressed File with Twitter Account Data')
    parser.add_argument('sink', type=str, nargs=1,
                        help='Zip extraction directory')
    args = parser.parse_args()

    return (abspath(args.src[0]), abspath(args.sink[0]))


def _calculateSuccess(_data: List[bool]) -> float:
    return (len(list(filter(lambda e: e, _data))) / len(_data)) * 100


def _banner():
    print('\x1b[1;6;36;49m[+]twiz v0.2.7 - Your Twitter Account Data Analysis & Visualization Tool <3\x1b[0m\n\n\t\x1b[3;39;40m$ twiz `path-to-zip-file` `path-to-sink-directory`\x1b[0m\n\n[+]Author: Anjan Roy <anjanroy@yandex.com>\n[+]Source: https://github.com/itzmeanjan/twiz ( CC0-1.0 Licensed )\n')


def _joinName(name: str) -> str:
    return '_'.join(name.split())


def main():
    _banner()

    try:
        src, sink = _getCMD()
        if not exists(src):
            raise RuntimeError('Source file absent')

        if not extract(src, sink):
            raise RuntimeError('Failed to extract from source')

        print('[+]Working ...')
        _start = time()

        _parsedFollowers = parse(join(sink, 'data/follower.js'))
        if not _parsedFollowers:
            raise RuntimeError('Failed to parse followers')

        _parsedFollowings = parse(join(sink, 'data/following.js'))
        if not _parsedFollowings:
            raise RuntimeError('Failed to parse followings')

        _account = parse(join(sink, 'data/account.js'))
        if not _account:
            raise RuntimeError('Failed to parse account')

        _parsedLikes = parse(join(sink, 'data/like.js'))
        if not _parsedLikes:
            raise RuntimeError('Failed to parse likes')

        _parsedAdEngagement = parse(join(sink, 'data/ad-engagements.js'))
        if not _parsedFollowers:
            raise RuntimeError('Failed to parse advertisement engagements')

        _followers = getFollowers(_parsedFollowers)
        _followings = getFollowings(_parsedFollowings)
        _accountDisplayName = getAccountDisplayName(_account)
        _likes = getLikes(_parsedLikes)
        _engagements = Engagements.build(_parsedAdEngagement)
        makeDirectory('plots')

        _success = [
            plotFollowersAndFollowings(_followers,
                                       _followings,
                                       'Twitter Followers And Followings for {}'
                                       .format(_accountDisplayName),
                                       'plots/twitterFollowersAndFollowingsFor{}.png'
                                       .format(_joinName(_accountDisplayName))),
            plotFollowersAndFollowedFollowers(_followers,
                                              _followings,
                                              ['Twitter Followers & Followed back Followers for {}'.format(_accountDisplayName),
                                               'Twitter Followings & Follower Followings for {}'.format(_accountDisplayName)],
                                              'plots/twitterFollowersFollowingsAndIntersectionFor{}.png'
                                              .format(_joinName(_accountDisplayName))),
            plotTopXHashTagsFoundInLikedTweets(
                _likes, 10,
                'Top 10 Twitter #HASHTAGS found in tweets liked by {}'.format(
                    _accountDisplayName),
                'plots/top10TwitterHashTagsFoundInTweetsLikedBy{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotTopXTaggedUsersFoundInLikedTweets(
                _likes, 10,
                'Top 10 @TaggedTwitterUsers found in tweets liked by {}'.format(
                    _accountDisplayName),
                'plots/top10TaggedTwitterUsersFoundInTweetsLikedBy{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotTopXEmojisFoundInLikedTweets(
                _likes, 10,
                'Top 10 Emojis found in tweets liked by {}'.format(
                    _accountDisplayName),
                'plots/top10EmojisFoundInTweetsLikedBy{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotAdTargetDeviceTypes(
                _engagements,
                'Twitter Ads for {}, by target device type'.format(
                    _accountDisplayName),
                'plots/twitterAdsTargeting{}OnDevices.png'.format(
                    _joinName(_accountDisplayName))),
            plotPercentageOfShownAdsByLocationOfDisplay(
                _engagements,
                'Twitter Ads for {}, by on-screen display location'.format(
                    _accountDisplayName),
                'plots/twitterAdCountByDisplayLocationFor{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotShownAdsGroupedByDeviceTypeAndDisplayLocation(
                _engagements,
                'Twitter Ads for {}, grouped by Device Type & on-screen Display Location'.format(
                    _accountDisplayName),
                'plots/twitterAdsGroupedByDeviceTypeAndDisplayLocationFor{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotAdsCountGroupedByAdvertiserNames(
                _engagements,
                15,
                f'Top 15 Twitter Advertisers {_accountDisplayName} interacted with',
                'plots/twitterAdsCountGroupedByAdvertiserNamesFor{}.png'.format(
                    _joinName(_accountDisplayName))),
            plotAdsCountGroupedByEngagementTypes(
                _engagements,
                15,
                f'Top 15 Ad Engagement Types Twitter used for {_accountDisplayName}',
                f'plots/twitterAdsCountGroupedByEngagementTypesFor{_joinName(_accountDisplayName)}.png'),
            plotTopXAdvertisersAsHeatMap(
                _engagements,
                15,
                f'Top 15 Twitter Advertisers with respective Engagement Types for {_accountDisplayName}',
                f'plots/twitterAdsCountGroupedByAdvertiserNamesAndEngagementTypesFor{_joinName(_accountDisplayName)}.png'),
            plotTargetCriteriasForTopXAdvertisers(
                _engagements,
                5,
                f'Twitter Ad Targeting Criterias used for {_accountDisplayName} by ',
                f'plots/twitterAdTargetingCriteriasUsedFor{_joinName(_accountDisplayName)}By'),
            plotTopXTargetCriteriasUsedByTwitterAdvertisers(
                _engagements,
                20,
                f'Top 20 Ad Target Criterias used for {_accountDisplayName} on Twitter',
                f'plots/top20AdTargetCriteriasUsedFor{_joinName(_accountDisplayName)}OnTwitter.png'),
            plotBarChartShowingAdTargetCriteriaUsageCountGroupedByType(
                _engagements,
                _accountDisplayName)
        ]

        print('[+]Obtained success : {:.2f} %, in {:.2f} s'.format(
            _calculateSuccess(_success),
            time() - _start))
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    except Exception as e:
        print('[!]Error: {}'.format(e))


if __name__ == '__main__':
    main()
