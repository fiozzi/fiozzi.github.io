# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:48:41 2023

@author: Iozzi
"""

import csv

def file_stat(filename, fieldname):
    with open(filename,'r', encoding='utf-8') as f_input:
        dict_reader = csv.DictReader(f_input, delimiter=',')
        column_dict = {}
        for riga in dict_reader:
            if riga[fieldname] in column_dict.keys():
                column_dict[riga[fieldname]] += 1
            else:
                column_dict[riga[fieldname]] = 1
    return column_dict

column_dict = file_stat('bridges.data', 'MATERIAL')
print(column_dict)
column_dict = file_stat('Artists.csv', 'Gender')
print(column_dict)
