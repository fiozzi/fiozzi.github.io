# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:03:55 2023

@author: Iozzi
"""

def calcola_n_aule(n_studenti, capacita_aule):
    n_aule = n_studenti // capacita_aule + 1
    return n_aule
