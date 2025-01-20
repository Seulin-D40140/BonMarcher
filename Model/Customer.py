#!/usr/bin/env python
# -*- coding: utf-8 -*

from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class Customer (ABC):
    name : str