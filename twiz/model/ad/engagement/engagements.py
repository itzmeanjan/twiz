#!/usr/bin/python3

from __future__ import annotations
from .engagement import Engagement
from typing import List, Dict, Any


class Engagements:
    def __init__(self, all: List[Engagement]):
        self.all = all

    @staticmethod
    def build(self, data: Dict[str, Any]) -> Engagements:
        return Engagements(
            [
                Engagement.build(j) for j in i['ad']['adsUserData']['adEngagements']['engagements']
                for i in data])


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
