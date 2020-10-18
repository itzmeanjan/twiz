#!/usr/bin/python3

from dataclasses import dataclass

@dataclass
class Mention:
    name: str
    screenName: str
    id: str
