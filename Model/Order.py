#!/usr/bin/env python
# -*- coding: utf-8 -*

from Model.ConsumableBought import ConsumableBuying
from Model.Customer import Customer
from dataclasses import dataclass
from abc import ABC , abstractmethod

@dataclass
class Order (ABC):
    customer : Customer
    order : list[ConsumableBuying]
    totalPrice : float

    def to_dict(self):
        # Convertir l'instance Order en dictionnaire pour la sérialisation JSON
        return {
            'customer': {'NOM': self.customer.name},
            'order': [{'NAME': item.name, 'NB': item.count, 'PRIX': item.price} for item in self.order],
            'totalPrice': self.totalPrice
        }

    def orderTreatment(customName: Customer, orderList: list[ConsumableBuying]):
        orderResult = Order(customName, orderList, sum(order.price for order in orderList))
        return orderResult