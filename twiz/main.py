#!/usr/bin/python3

from argparse import ArgumentParser
from typing import Tuple, List
from os.path import exists, abspath, join
from .extract import extract, makeDirectory
from .parser import parse
from .model.follower import getFollowers
from .model.following import getFollowings
from .model.account import getAccountDisplayName
from .plot.util import (
    plotFollowersAndFollowings,
    plotFollowersAndFollowedFollowers
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
    print('\x1b[1;6;36;49m[+]twiz v0.1.0 - Your Twitter Account Data Analysis & Visualization Tool <3\x1b[0m\n\n\t\x1b[3;39;40m$ twiz `path-to-zip-file` `path-to-sink-directory`\x1b[0m\n\n[+]Author: Anjan Roy <anjanroy@yandex.com>\n[+]Source: https://github.com/itzmeanjan/twiz ( CC0-1.0 Licensed )\n')


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

        _followers = getFollowers(_parsedFollowers)
        _followings = getFollowings(_parsedFollowings)
        _accountDisplayName = getAccountDisplayName(_account)
        makeDirectory('plots')

        _success = [
            plotFollowersAndFollowings(_followers,
                                       _followings,
                                       'Twitter Followers And Followings Per Cent for {}'
                                       .format(_accountDisplayName),
                                       'plots/twitterFollowersAndFollowingsPerCentFor{}.png'
                                       .format(_joinName(_accountDisplayName))),
            plotFollowersAndFollowedFollowers(_followers,
                                              _followings,
                                              ['Twitter Followers & Followed back Followers for {}'.format(_accountDisplayName),
                                               'Twitter Followings & Follower Followings for {}'.format(_accountDisplayName)],
                                              'plots/twitterFollowersFollowingsAndIntersectionFor{}.png'
                                              .format(_joinName(_accountDisplayName)))
        ]

        print('[+]Obtained success : {:.2f} %, in {} s'.format(
            _calculateSuccess(_success),
            time() - _start))
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    except Exception as e:
        print('[!]Error: {}'.format(e))


if __name__ == '__main__':
    main()
