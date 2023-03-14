# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:28:44 2023

@author: Iozzi
"""

phd_student = [{'name': 'sara', 'eta': 26, \
                'laurea': 'comunicazione'}, \
               {'name': 'marco', 'eta': 35, \
                'laurea': 'ingegneria'}]

for student in phd_student:
    eta = student['eta']
    nome = student['name']
    print(f"{nome} ha {eta} anni.")
    