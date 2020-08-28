#!/usr/bin/python3

from dataclasses import dataclass


@dataclass
class Info:
    fullName: str
    screenName: str


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
