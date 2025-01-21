#!/usr/bin/env python
# -*- coding: utf-8 -*

from Service.bddService import *
from Model.consumableModel import Consumable
from Model.Customer import Customer
from Model.Order import Order
from Model.ConsumableCart import ConsumableCart
import json

orderList: list[ConsumableCart] = []
outOfStock: list[Consumable] = []

consumableDatas : list[Consumable] = \
    [
        Consumable( 1 , "clementine" , 2.90 , 6),
        Consumable( 2 , "datte" , 7.0 , 4),
        Consumable( 3 , "grenade" , 3.50 , 3),
        Consumable( 4 ,"kiwi" , 3.50 , 3),
        Consumable( 5 ,"orange" , 1.50 , 8),
        Consumable( 6 ,"poire" , 2.50 , 5),
        Consumable( 7 ,"pomme" , 1.50 , 8),
        Consumable( 8 ,"carotte" , 1.30 , 7),
        Consumable( 9 ,"endive" , 2.50 , 5),
        Consumable( 10 ,"epinard" , 2.60 , 4),
        Consumable( 11 ,"poireau" , 1.20 , 5),
        Consumable( 12 ,"radis noir" , 5.0 , 10),
        Consumable( 13 ,"salsifis" , 2.50 , 3),
        Consumable( 14 ,"choux vert" , 2.50 , 12)
    ]

def numberVerif ( nb : str) -> int :
    """ verify if number """
    while not nb.isdigit():
        nb = (input("entrez un nombre valide : "))
    return int(nb)

def idVerif(id: str) -> int:
    """ verify if number and cunsumablesDatas contain id """
    idVerif : int = numberVerif(id)
    idList : list[int] = []

    for consumable in consumableDatas:
        idList.append(consumable.id)
    while not idList.__contains__(idVerif):
        idVerif = numberVerif(input("entrez un nombre compris dans les ids : "))
    return idVerif

def stockVerif( id : int , nb : str ) -> int:
    """ verify if number isn't too much or low than current stock """
    size : int = numberVerif(nb)
    for consumable in consumableDatas:
        if id == consumable.id:
            while size > consumable.stock or size <= 0 :
                size  = numberVerif(input("entrez un nombre compris dans le stock : "))
    return size

def outStock(consumable : Consumable):
    """ add consumable to outOfStock 'table' and remove it from consumableDatas """
    if consumable.stock == 0:
        addResultOutOfStockToJson(consumable.__dict__) # attention ici .......................................................
        consumableDatas.remove(consumable)

def cartTreatment(idConsumable : int , weight : int):
    """ creat 'cart' orderList """
    for consumableData in consumableDatas:
        if idConsumable == consumableData.id:
            consumableData.stock -= weight
            bought : ConsumableCart = ConsumableCart(consumableData.name, weight, consumableData.price * weight)
            orderList.append(bought)
    for order in orderList:
        print(order.display())

def orderTreatment(customer: Customer, orderList: list[ConsumableCart]) -> Order:
    """ create order and add to json file """
    orderResult : Order = Order(customer, orderList, sum(order.price for order in orderList))

    orders : list[dict[str, object]] = []
    orders.append({
        "customer : ": orderResult.customer.name,
        "order : ":[vars(order) for order in orderList], # attention ici ------------------------------------------------------
        "price total : ": orderResult.totalPrice
    })

    addResultOfTheDayToJson(orders)
    return orderResult