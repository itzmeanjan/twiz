#!/usr/bin/python3

from argparse import ArgumentParser
from typing import Tuple
from os.path import exists, abspath, join
from .extract import extract
from .parser import parse
from .model.follower import getFollowers
from .model.following import getFollowings
from .model.manip import getBothFollowersAndFollowings


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


def main():
    try:
        src, sink = _getCMD()
        if not exists(src):
            raise RuntimeError('Source file absent')

        if not extract(src, sink):
            raise RuntimeError('Failed to extract source')

        _parsedFollowers = parse(join(sink, 'data/follower.js'))
        if not _parsedFollowers:
            raise RuntimeError('Failed to parse followers')

        _parsedFollowings = parse(join(sink, 'data/following.js'))
        if not _parsedFollowings:
            raise RuntimeError('Failed to parse followings')

        _followers = getFollowers(_parsedFollowers)
        _followings = getFollowings(_parsedFollowings)
        print(getBothFollowersAndFollowings(_followers, _followings))

    except KeyboardInterrupt:
        print('\n[!]Terminated')
    except Exception as e:
        print('[!]Error: {}'.format(e))


if __name__ == '__main__':
    main()
