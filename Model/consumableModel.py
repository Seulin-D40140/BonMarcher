#!/usr/bin/env python
# -*- coding: utf-8 -*

from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class Consumable (ABC):
    id : int
    name : str
    price : float
    stock : int

    def display (self):
        print(f"id : {self.id} - name : {self.name} - Price : {self.price:.2f}€ - Stock : {self.stock}")
