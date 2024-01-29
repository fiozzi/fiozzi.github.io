# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:42:51 2023

@author: fabri
"""

from libro import Libro

libro1 = Libro(autore='Graham Green', \
               titolo='Our man in Havana', \
               lingua='EN', \
               isbn='0140017909')

libro2 = Libro(autore='Stanislaw Lem', \
               titolo='Cyberiade', \
               lingua='IT', \
               isbn='9771120528002')

# ho modificato il 5 codice di libro2

libro3 = Libro(autore='Fabrizio Iozzi', \
               titolo='Il libro che non ho scritto', \
               lingua='IT', \
               isbn='9771120628002')

libri = []
libri.append(libro1)
libri.append(libro2)
libri.append(libro3)

for libro in libri:
    print(libro.autore, libro.titolo)
    if libro.ISBNValido()[0]:
    	print('Valido')
    else:
    	print(libro.ISBNValido()[1])

