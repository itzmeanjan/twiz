#!/usr/bin/python3

from __future__ import annotations
from .engagement import Engagement
from .criteria import MatchedCriteria
from typing import List, Dict, Any, Tuple
from itertools import chain
from collections import Counter
from functools import reduce


class Engagements:
    def __init__(self, all: List[Engagement]):
        self.all = all

    @staticmethod
    def build(data: Dict[str, Any]) -> Engagements:
        return Engagements(list(
            chain.from_iterable(
                [[Engagement.build(j) for j in i['ad']['adsUserData']
                  ['adEngagements']['engagements']] for i in data])))

    def countByDeviceType(self) -> Counter:
        return Counter(filter(lambda e: e,
                              map(lambda e: e.device.type,
                                  self.all)))

    def countByDisplayLocation(self) -> Counter:
        '''
            Counts how many twitter ads were displayed on which location
            of your profile while you were browsing twitter
        '''
        return Counter(map(lambda e: e.displayLocation, self.all))

    def percentageOfAdsByDisplayLocation(self) -> List[Tuple[str, float]]:
        '''
            Percentage distribution of total ads shown on twitter to YOU,
            in terms of location of ad display
        '''
        _buffer = self.countByDisplayLocation()
        _total = sum(_buffer.values())

        return [(i, (_buffer[i] / _total) * 100) for i in sorted(_buffer,
                                                                 key=lambda e: _buffer[e],
                                                                 reverse=True)]

    def groupAdCountByDeviceTypeAndDisplayLocation(self) -> Dict[str, Counter]:
        '''
            Distribution of shown twitter ads by device type & respective location
            of display on device
        '''
        def _groupByDeviceType(acc: Dict[str, List[str]], cur: Tuple[str, str]) -> Dict[str, List[str]]:
            if cur[0] in acc:
                acc[cur[0]].append(cur[1])
            else:
                acc[cur[0]] = [cur[1]]

            return acc

        return dict(map(lambda e: (e[0], Counter(e[1])),
                        reduce(_groupByDeviceType,
                               map(lambda e: (e.device.type, e.displayLocation),
                                   self.all),
                               {}).items()))

    def adCountGroupedByAdvertiserName(self) -> Counter:
        '''
            How many ads this user engaged in from each advertiser
        '''
        return Counter(map(lambda e: e.advertiser.fullName, self.all))

    def topXAdvertiserNames(self, x: int) -> List[Tuple[str, int]]:
        '''
            Returns a list of top X advertisers in terms of number of ads 
            engaged in
        '''
        return self.adCountGroupedByAdvertiserName().most_common(x)

    def adCountGroupedByEngagementType(self) -> Counter:
        '''
            Counts how many ad engagements happened in which way i.e.
            {EmbeddedMedia, ChargeableImpression}
        '''
        return Counter(chain.from_iterable(
            map(lambda e: map(lambda _e: _e.type, e.attrs), self.all)))

    def topXEngagementTypes(self, x: int) -> List[Tuple[str, int]]:
        '''
            Top X ways how you got engaged with a twitter advertisement i.e.
            rather twitter engaged you in
        '''
        return self.adCountGroupedByEngagementType().most_common(x)

    def groupAdCountByAdvertiserNameAndEngagementTypes(self):
        '''
            Groups advertisement counts by advertiser name & under each of those
            respective engagement type used for showing advertisement, along with their
            count
        '''
        def _groupIt(acc: Dict[str, List[map]], cur: Tuple[str, map]) -> Dict[str, List[map]]:
            if cur[0] in acc:
                acc[cur[0]].append(cur[1])
            else:
                acc[cur[0]] = [cur[1]]

            return acc

        return dict(map(lambda e: (e[0], Counter(chain.from_iterable(e[1]))),
                        reduce(_groupIt, map(lambda e: (e.advertiser.fullName,
                                                        map(lambda _e: _e.type, e.attrs)), self.all), {}).items()))

    def topXAdvertiserNamesWithRespectiveEngagementTypes(self, x: int):
        '''
            Returns top X advertisers with their respective engagement types & counts used
            for showing you ad on twitter
        '''
        _ads = self.groupAdCountByAdvertiserNameAndEngagementTypes()

        _topX = sorted(_ads,
                       key=lambda e: sum(_ads[e].values()),
                       reverse=True)[:x]

        return dict(map(lambda e: (e, _ads[e]), _topX))

    def groupEngagementsByAdvertiserName(self) -> Dict[str, List[Engagement]]:
        '''
            Groups all engagements by their respective advertiser's screen name
        '''
        def _groupBy(acc: Dict[str, List[Engagement]], cur: Engagement) -> Dict[str, List[Engagement]]:
            if cur.advertiser.fullName in acc:
                acc[cur.advertiser.fullName].append(cur)
            else:
                acc[cur.advertiser.fullName] = [cur]

            return acc

        return reduce(_groupBy, self.all, {})

    def getEngagementsByAdvertiserName(self, advertiser: str) -> List[Engagement]:
        '''
            Returns a list of all engagements, when advertiser name is given
        '''
        return self.groupEngagementsByAdvertiserName().get(advertiser)

    def getMatchedTargetingCriteriasByAdvertiserName(self, advertiser: str) -> List[MatchedCriteria]:
        '''
            Returns a list of all advertise targeting criterias used by a certain advertiser,
            along with their respective values set by them
        '''
        return list(chain.from_iterable(map(lambda e: map(lambda _e: _e, e.criterias),
                                            self.getEngagementsByAdvertiserName(advertiser))))

    def getGroupedTargetingCriteriasByAdvertiserName(self, advertiser: str) -> Dict[str, Counter]:
        '''
            Groups all targeting criterias for a specific advertiser, by their
            respective criteria type & under each of them keep a counter for all values
        '''
        def _groupBy(acc: Dict[str, List[str]], cur: MatchedCriteria) -> Dict[str, List[str]]:
            if cur.type in acc:
                acc[cur.type].append(cur.value)
            else:
                acc[cur.type] = [cur.value]

            return acc

        return dict(map(lambda e: (e[0], Counter(e[1])),
                        reduce(_groupBy,
                               self.getMatchedTargetingCriteriasByAdvertiserName(
                                   advertiser),
                               {}).items()))

    def usageCountByAdTargetCriteriaValue(self) -> Counter:
        '''
            Counting number of occurance of ad target criteria values
        '''
        return Counter(chain.from_iterable(
            map(lambda e: map(lambda _e: _e.value,
                              e.criterias), self.all)))

    def topXAdTargetCriteriasUsed(self, x: int) -> List[Dict[str, int]]:
        '''
            Finding top X ad target criteria values
        '''
        return self.usageCountByAdTargetCriteriaValue().most_common(x)

    def adTargetCriteriaUsageCountGroupedByType(self) -> Dict[str, Counter]:
        '''
            Grouping ad target criteria usage count by targeting criteria type 
            & under each type, holding the usage count of each target value
        '''
        def _groupBy(acc: Dict[str, List[str]], cur: Tuple[str, str]) -> Dict[str, List[str]]:
            if cur[0] in acc:
                acc[cur[0]].append(cur[1])
            else:
                acc[cur[0]] = [cur[1]]

            return acc

        return dict(map(lambda e: (e[0], Counter(e[1])),
                        reduce(_groupBy,
                               chain.from_iterable(map(lambda e: map(lambda _e: (_e.type, _e.value),
                                                                     e.criterias), self.all)), {}).items()))


if __name__ == '__main__':
    print('It\'s not supposed to be used this way !')
