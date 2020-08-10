#!/usr/bin/python3

from re import compile as regCompile, Pattern
from typing import List, Dict, Any
from os.path import exists
from json import loads, JSONDecodeError


def _getRegex() -> Pattern:
    '''
        Compile regular expression to be for parsing out data from *.js file
    '''
    return regCompile(r'(=([\s|\S]+))$')


def parse(src: str) -> List[Dict[str, Any]]:
    '''
        Parses JS file content & returns Python object
    '''
    if not exists(src):
        return None

    _reg = _getRegex()
    with open(src, mode='r') as fd:
        data = fd.read()

    _match = _reg.search(data)
    if not _match:
        return None

    try:
        return loads(_match.group(2).strip())
    except JSONDecodeError:
        return None


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
