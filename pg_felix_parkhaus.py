import pygame
from pygame.locals import *

pygame.init()

#Eingabefelder (Preis, Parkplatzanzahl, Geschwindigkeit)
#Funktion zur Eingabe des Preises
def inputprice():
    global price
    price = float(input("Preis pro Stunde: "))
    print("Preis/Std", price)

#Funktion zur Eingabe der Parkplätze
def inputlots():
    global total_lots
    rows = int(input("Anzahl der Reihen : "))
    columns = int(input("Anzahl der Spalten: "))
    total_lots = rows * columns
    print( total_lots, "Parkplätze")

#Funktion zur Eingabe der Geschwindigkeit
def inputvelocity():
    global velocity
    velocity = float(input("Geschwindigkeit der Simulation: "))
    print(velocity)

#Ausgabefelder (Preis, Parkplatzanzahl, Geschwindigkeit)
#Funktion zur Ausgabe des Preises
def outputprice():
    #opprice = price * hour
    currency = "€"
    print(f"Der Preis pro Stunde beträgt: {currency}{price:.2f}")

#Funktion zur Ausgabe der Parkplätze
def outputlots():
    print(f"Die Anzahl der Parkplätze beträgt: {total_lots} Stück")

#Funktion zur Ausgabe der Geschwindigkeit
def outputvelocity():
    print(f"Geschwindigkeit der Simualtion: {velocity}")
