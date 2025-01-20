#!/usr/bin/env python
# -*- coding: utf-8 -*
from Model.consumableModel import Consumable
from Model.Customer import Customer
from Model.Order import Order
from Model.ConsumableBought import ConsumableBuying


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

orderList : list[ConsumableBuying] = []

def cartTreatment(idConsumable : int , weight : int):
    for consumableData in consumableDatas:
        if idConsumable == consumableData.id:
            consumableData.stock -= weight
            bought = ConsumableBuying(consumableData.name , weight , consumableData.price*weight)
            orderList.append(bought)
    print(orderList)

def mainToMain():
        name = (input("bonjour quel est votre nom ? : "))
        customName = Customer(name)

        continu = True
        while continu :
            print("-------------------------------------------------------")
            for consumable in consumableDatas:
                if consumable.stock > 0:
                    consumable.display()
            print("-------------------------------------------------------")

            idConsumable = int(input("que voulez vous acheter ? entrez l'id : "))
            howMuch = int(input("combien en voulez vouz ? : "))
            cartTreatment(idConsumable , howMuch)
            
            continuCustom = (input("voulez vous autre chose ? 'y' pour continuer : "))
            if continuCustom !='y':
                continu = False
                print("a bientot")
        print(Order.orderTreatment(customName , orderList ).to_dict())



if __name__ == '__main__':
    mainToMain()
