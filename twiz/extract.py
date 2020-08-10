#!/usr/bin/python3

from os import mkdir
from os.path import exists


def makeDir(target: str) -> bool:
    '''
        Creates non-existing directory & denotes boolean status
    '''
    if exists(target):
        return True

    try:
        mkdir(target)
        return True
    except OSError:
        return False


def extract():
    pass


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
