# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:34:37 2023

@author: Iozzi
"""

lista1 = [44,76,23,68,54,99]
soglia = 50

for el in lista1:
    if el < soglia:
        print(el)

print('fine della lista')

for i in range(12):
    print(i)
    
for elemento in range(3,12):
    print(elemento)

listacitta = []
listacitta.append(['Milano', 'Italia'])
listacitta.append(['roma', 'italia'])
listacitta.append(['london', 'uk'])
# print(listacitta)

for citta in listacitta:
    if citta[1].upper() == 'ITALIA':
        print(citta)

for i in range(5):
    print('fabrizio')