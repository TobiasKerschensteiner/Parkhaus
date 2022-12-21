import pygame
from pygame.locals import *

pygame.init()

#Eingabefelder (Preis, Parkplatzanzahl, Geschwindigkeit)
#Preis
def inputprice(): #Funktion zur Eingabe des Preises
    price = 0
    price = float(input("Preis pro Stunde: "))
    print("Preis/Std", price)

inputprice()

#Anzahl der Parkplätze
def quantitylots(): #Funktion zur Anzahl der Parkplätze


