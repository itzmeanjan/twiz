#!/usr/bin/python3

from re import compile as regCompile, Pattern


def _getRegex() -> Pattern:
    '''
        Compile regual expression to be for parsing out data from *.js file
    '''
    return regCompile(r'(=([\s|\S]+))$')


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
