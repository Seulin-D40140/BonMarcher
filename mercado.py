#!/usr/bin/env python
# -*- coding: utf-8 -*

from Service import customableService
from Service.customableService import *

def mainToMain():
    name : str = (input("bonjour quel est votre nom ? : "))
    customName : Customer = Customer(name)

    continu : bool = True
    while continu :
        print("-----------------~~~~~~~~~~~~~~~~~-------------------")
        for consumable in consumableDatas:
            consumable.display()
        print("-----------------~~~~~~~~~~~~~~~~~-------------------")

        idConsumable = customableService.idVerif(input("que voulez vous acheter ? entrez l'id : "))
        howMany = customableService.stockVerif(idConsumable, input("combien en voulez vouz ? : "))
        customableService.cartTreatment(idConsumable, howMany)

        for consumable in consumableDatas:
            customableService.outStock(consumable)

        continuCustom = (input("voulez vous autre chose ? 'y' pour continuer / All-Other = 'no' : "))
        if continuCustom !='y':
            continu = False

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("*************** a bientot , RESUMER DE LA COMMANDE : ******************")
    print(customableService.orderTreatment(customName , orderList).display())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == '__main__':
    mainToMain()