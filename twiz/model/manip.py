#!/usr/bin/python3

def getBothFollowersAndFollowings(followings: map, followers: map):
    '''
        Computes list of those followings who you follow back or in other terms
        followers whom you follow too
    '''
    return set(map(lambda e: e[0], followers)).intersection(
        set(map(lambda e: e[0], followings)))


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
