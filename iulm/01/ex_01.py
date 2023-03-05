# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:03:55 2023

@author: Iozzi
"""

# dati
capacita_aule = 50

# input numero studenti
n_studenti = int(input('Quanti sono gli studenti?'))

n_aule = n_studenti // capacita_aule + 1

print(f'Per questo esame occorrono {n_aule} aule')

