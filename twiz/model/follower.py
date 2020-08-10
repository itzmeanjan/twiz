#!/usr/bin/python3

from dataclasses import dataclass


@dataclass
class Follower:
    userId: str
    link: str


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
