#!/usr/bin/env python
# -*- coding: utf-8 -*

from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class ConsumableCart (ABC):
    name : str
    count : int
    price : float

    def display(self):
        return  f"NOM : {self.name} - prince : {self.price}"