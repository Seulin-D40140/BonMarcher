#!/usr/bin/env python
# -*- coding: utf-8 -*

from Model.ConsumableCart import ConsumableCart
from Model.Customer import Customer
from dataclasses import dataclass
from abc import ABC , abstractmethod


@dataclass
class Order (ABC):
    customer : Customer
    order : list[ConsumableCart]
    totalPrice : float

    def display(self):
        # Convertir l'instance Order en chaîne formatée avec retour à la ligne
        return f"NOM : {self.customer.name}\n" + \
            f"order:\n" + \
            "\n".join([f"  NAME : {item.name}  NB : {item.count}  PRIX : {item.price}" for item in self.order]) + \
            f"\ntotalPrice : {self.totalPrice}"