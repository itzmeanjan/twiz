#!/usr/bin/python3

import seaborn as sns
from matplotlib import pyplot as plt
from typing import List


def plotAdTargetDeviceTypes(x: List[str], y: List[str], title: str, sink: str) -> bool:
    try:
        fig = plt.Figure(figsize=(16, 9), dpi=100)
        sns.set_style('darkgrid')

        sns.barplot(x=x, y=y, ax=fig.gca())

        for i, j in enumerate(fig.gca().patches):
            fig.gca().text(j.get_x() + j.get_width() * .5,
                           j.get_y() + j.get_height() * .5,
                           y[i],
                           ha='center',
                           rotation=0,
                           fontsize=14,
                           color='black')

        fig.gca().set_title(title, fontsize=20, pad=10)
        fig.tight_layout(pad=4)

        fig.savefig(sink, pad_inches=.8)
        plt.close(fig)

        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
