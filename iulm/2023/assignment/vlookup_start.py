# -*- coding: utf-8 -*-
"""

@author: Iozzi
"""
import csv

def vlookup(nomefile, campo, valore, output):

    pass

risultato = vlookup(nomefile = 'bridges.data', campo = 'MATERIAL', valore = 'WOOD', output = 'IDENTIF')
print()
print('lista di IDENTIF per i ponti il cui MATERIAL è WOOD')
print(risultato)

risultato = vlookup(nomefile = 'bridges.data', campo = 'PURPOSE', valore = 'HIGHWAY', output = 'IDENTIF')
print()
print('lista di IDENTIF per i ponti il cui PURPOSE è HIGHWAY')
print(risultato)

risultato = vlookup(nomefile = 'bridges.data', campo = 'PURPOSE', valore = 'HIGHWAY', output = 'LENGTH')
print()
print('lista di LENGTH per i ponti il cui PURPOSE è HIGHWAY')
print(risultato)

risultato = vlookup(nomefile = 'bridges.data', campo = 'MATERIAL', valore = 'PAPER', output = 'IDENTIF')
print()
print('lista di IDENTIF per i ponti il cui MATERIAL è PAPER')
print(risultato)

