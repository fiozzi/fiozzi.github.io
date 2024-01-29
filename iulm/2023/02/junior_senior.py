# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:08:17 2023

@author: Iozzi
"""

print("Benvenuto al cinema!")
age = int(input("Quanti anni hai? "))

if age < 18:
    ticket_price = 10 * 0.8  # applica lo sconto del 20%
else:
    if age < 65:
        ticket_price = 10  # prezzo pieno
    else:
        ticket_price = 10 * 0.7  # applica lo sconto del 30%
       
print(f"Il prezzo del tuo biglietto è {ticket_price} euro.")