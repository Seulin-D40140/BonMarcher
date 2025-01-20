
#!/usr/bin/env python
# -*- coding: utf-8 -*

from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class ConsumableBuying (ABC):
    name : str
    count : int
    price : float