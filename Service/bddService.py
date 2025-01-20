#!/usr/bin/env python
# -*- coding: utf-8 -*

import json

def addResultOfTheDayToJson( orders ):
    try:
        with open("dayResult.json", "a") as file:
            json.dump(orders, file, indent=4)
        print("Les données ont été écrites avec succès dans dayResult.json")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")

def addResultOfStock ( stock ):
    try:
        with open("stockResult.json", "a") as file:
            json.dump(stock, file, indent=4)
        print("Les données ont été écrites avec succès dans stockResult.json")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")