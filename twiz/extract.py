#!/usr/bin/python3

from os import mkdir
from os.path import exists
from zipfile import ZipFile, BadZipFile


def makeDirectory(target: str) -> bool:
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


def extract(src: str, sink: str) -> bool:
    '''
        Extracts compressed twitter account data file into sink directory
    '''
    if not (exists(src) and src.endswith('.zip') and makeDirectory(sink)):
        return False

    try:
        _zf = ZipFile(src)
        _zf.extractall(sink)

        return True
    except BadZipFile:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
