#!/usr/bin/python3

from argparse import ArgumentParser
from typing import Tuple, List
from os.path import exists, abspath, join
from .extract import extract, makeDirectory
from .parser import parse
from .model.follower import getFollowers
from .model.following import getFollowings
from .plot.util import plotFollowersAndFollowings


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


def main():
    try:
        src, sink = _getCMD()
        if not exists(src):
            raise RuntimeError('Source file absent')

        if not extract(src, sink):
            raise RuntimeError('Failed to extract from source')

        print('[+]Working ...')

        _parsedFollowers = parse(join(sink, 'data/follower.js'))
        if not _parsedFollowers:
            raise RuntimeError('Failed to parse followers')

        _parsedFollowings = parse(join(sink, 'data/following.js'))
        if not _parsedFollowings:
            raise RuntimeError('Failed to parse followings')

        _followers = getFollowers(_parsedFollowers)
        _followings = getFollowings(_parsedFollowings)
        makeDirectory('plots')

        _success = [
            plotFollowersAndFollowings(_followers,
                                       _followings,
                                       'Twitter Followers And Followings Per Cent',
                                       'plots/twitterFollowersAndFollowingsPerCent.png')
        ]

        print('[+]Success: {:.2f} %'.format(_calculateSuccess(_success)))
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    except Exception as e:
        print('[!]Error: {}'.format(e))


if __name__ == '__main__':
    main()
