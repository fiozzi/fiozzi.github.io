# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:03:55 2023

@author: Iozzi
"""

import utilita
    
# dati
capacita_aule = int(input('Capacità aule: '))

# input numero studenti
n_studenti = int(input('Quanti sono gli studenti?'))

n_aule = utilita.calcola_n_aule(n_studenti, capacita_aule)

print(f'Per questo esame occorrono {n_aule} aule')

