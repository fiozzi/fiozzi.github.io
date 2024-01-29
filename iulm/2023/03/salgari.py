# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:11:23 2022

@author: fabrizio
"""

with open('salgari.txt', 'r') as f:
    testo = f.read()

parole = testo.split(' ')
print(len(parole))
parole_distinte = []
for parola in parole:
    if not (parola in parole_distinte):
        parole_distinte.append(parola)
print(len(parole_distinte))
