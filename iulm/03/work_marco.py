# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:58:34 2021

@author: Iozzi
"""

def prezzo_biglietto(eta, tipo_biglietto):
    prezzo_pieno = prezzo_per_tipo(tipo_biglietto)
    sconto = riduzione(tipo_biglietto, prezzo_pieno, eta)
    prezzo_finale = prezzo_pieno - sconto
        
    return prezzo_finale

def prezzo_per_tipo(tipo_biglietto):
    if tipo_biglietto == 'A' or tipo_biglietto =='B' \
        or tipo_biglietto=='C':
        prezzo_intero = 12
    else:
        prezzo_intero = 10
    return prezzo_intero

def riduzione(tipo_biglietto, prezzo, eta):
    perc_sconto = 0
    if tipo_biglietto in 'AB':
        if eta < 18:
            perc_sconto = 0.3
        else:
            if eta > 60:
                perc_sconto = 0.2
    return prezzo * perc_sconto

tipo = 'A'
prezzo = prezzo_per_tipo(tipo)
print(f'prezzo per biglietto {tipo}: {prezzo}')
tipo = 'F'
prezzo = prezzo_per_tipo(tipo)
print(f'prezzo per biglietto {tipo}: {prezzo}')

p = prezzo_biglietto(15, 'A')
print(p)