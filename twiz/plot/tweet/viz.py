#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from twiz.model.tweet.tweets import Tweets
from wordcloud import WordCloud


def plotTopXHashTags(data: Tweets, x: int, title: str, sink: str):
    try:
        _tmp = data.topXHashTagsWithCount(x)
        _x = [i[0] for i in _tmp]
        _y = [i[1] for i in _tmp]

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=_y, y=_x, ax=fig.gca(), orient='h', palette='plasma')

        fig.gca().set_title(title, fontsize=20, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.8)
        plt.close(fig)

        return True
    except Exception:
        return False


def plotTopXUserMentions(data: Tweets, x: int, title: str, sink: str):
    try:
        _tmp = data.topXUserMentionsWithCount(x)
        _x = [i[0] for i in _tmp]
        _y = [i[1] for i in _tmp]

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=_y, y=_x, ax=fig.gca(), orient='h', palette='plasma')

        fig.gca().set_title(title, fontsize=20, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.8)
        plt.close(fig)

        return True
    except Exception:
        return False


def wordCloudOfHashTagsUsedInTweets(data: Tweets, sink: str) -> bool:
    '''
        Given all hash tags used in tweets by this user, generates
        word cloud with it
    '''
    try:
        wc = WordCloud(width=1600, height=900, regexp=r'\#\w+')
        wc.generate(data.getAllHashTags())

        wc.to_file(sink)

        return True
    except Exception:
        return False

def wordCloudOfTaggedUsersInTweets(data: Tweets, sink: str) -> bool:
    '''
        Given all tagged users in tweets by this user, generates
        word cloud with it
    '''
    try:
        wc = WordCloud(width=1600, height=900, regexp=r'\@\w+')
        wc.generate(data.getAllTaggedUsers())

        wc.to_file(sink)

        return True
    except Exception:
        return False

if __name__ == '__main__':
    print('[!] This is not an executable script')
