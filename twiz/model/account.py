#!/usr/bin/python3

from typing import List, Dict, Any


def getAccountDisplayName(data: List[Dict[str, Any]]) -> str:
    return data[0]['account']['accountDisplayName']


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
