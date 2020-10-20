#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from twiz.model.tweet.tweets import Tweets


def plotTopXHashTags(data: Tweets, x: int, title: str, sink: str):
    try:
        _tmp = data.topXHashTagsWithCount(x)
        x = [i[0] for i in _tmp]
        y = [i[1] for i in _tmp]

        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=y, y=x, ax=fig.gca(), orient='h', palette='plasma')

        fig.gca().set_title(title, fontsize=20, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.8)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('[!] This is not an executable script')
