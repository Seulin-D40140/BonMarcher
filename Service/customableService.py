#!/usr/bin/env python
# -*- coding: utf-8 -*

from Service.bddService import addResultOfTheDayToJson
from Model.consumableModel import Consumable
from Model.Customer import Customer
from Model.Order import Order
from Model.ConsumableCart import ConsumableCart
import json

orderList: list[ConsumableCart] = []
outOfStock = []
dayResult: list[Order] = []

consumableDatas = \
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

def numberVerif ( nb : str):
    while not nb.isdigit():
        nb = (input("entrez un nombre valide : "))
    return int(nb)

def idVerif(id: str):
    idVerif : int = numberVerif(id)
    idList = []
    for consumable in consumableDatas:
        idList.append(consumable.id)
    while not idList.__contains__(idVerif):
        idVerif : int = numberVerif(input("entrez un nombre compris dans les ids : "))
    return idVerif

def stockVerif( id : int , nb : str ):
    size : int = numberVerif(nb)
    for consumable in consumableDatas:
        if id == consumable.id:
            while size > consumable.stock or size <= 0 :
                size : int = numberVerif(input("entrez un nombre compris dans le stock : "))
    return size

def outStock(consumable : Consumable):
    if consumable.stock == 0:
        outOfStock.append(consumable)
        consumableDatas.remove(consumable)

def cartTreatment(idConsumable : int , weight : int):
    for consumableData in consumableDatas:
        if idConsumable == consumableData.id:
            consumableData.stock -= weight
            bought = ConsumableCart(consumableData.name, weight, consumableData.price * weight)
            orderList.append(bought)
    for order in orderList:
        print(order.display())

def orderTreatment(customer: Customer, orderList: list[ConsumableCart]):
    orderResult = Order(customer, orderList, sum(order.price for order in orderList))
    orders = []

    orders.append({
        "customer : ": orderResult.customer.name,
        # "order : ": orderList,
        "price total : ": orderResult.totalPrice
    })
    addResultOfTheDayToJson(orders)
    dayResult.append(orderResult.display())
    return orderResult