#!/usr/bin/python3

from dataclasses import dataclass


@dataclass
class Mention:
    name: str
    screenName: str
    id: str


if __name__ == '__main__':
    print('[!] This is not an executable script')
