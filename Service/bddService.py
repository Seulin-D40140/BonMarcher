#!/usr/bin/env python
# -*- coding: utf-8 -*

import json

def addResultOfTheDayToJson( orders ):
    """ add order to json file """
    try:
        with open("dayResult.json", "a") as file: # a = append , r = read , w , write but erase ---------------------------
            json.dump(orders, file, indent = 4)
        print("Le recus a etait sauvegarder dans dayResult.json")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier dayResult.json : {e}")

def addResultOutOfStockToJson ( stock ):
    """ add consumable if stock under one to json file """
    try:
        with open("stockResult.json", "a") as file:
            json.dump(stock, file, indent = 4)
        print("Les données du stock ont été sauvegarder dans stockResult.json")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier stockResult.json : {e}")