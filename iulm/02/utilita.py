# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:03:55 2023

@author: Iozzi
"""

def calcola_n_aule(n_studenti, capacita_aule):

    # if n_studenti % capacita_aule == 0:
    #     n_aule = n_studenti // capacita_aule
    # else:
    #     n_aule = n_studenti // capacita_aule + 1

    n_aule = n_studenti // capacita_aule
    if n_studenti % capacita_aule == 0:
        n_aule += 1
    
    return n_aule
