# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:43:12 2020

@author: Iozzi
"""

import csv

def bridges_per_year(filename, year_field_name):
    bridges_per_year = {}
    with open(filename,'r') as fp:
        dict_reader = csv.DictReader(fp, delimiter=',')
        for row in dict_reader:
            year = int(row[year_field_name])
            if year in bridges_per_year.keys():
                bridges_per_year[year] += 1
            else:
                bridges_per_year[year] = 1
    return bridges_per_year

def invert_dict(d):
    inverse = dict()
    for key in d.keys():
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def materials(filename, material_field_name, unknown):
    materials = {}
    with open(filename,'r') as fp:
        dict_reader = csv.DictReader(fp, delimiter=',')
        for row in dict_reader:
            mat = row[material_field_name]
            if mat == '?':
                mat = unknown
            if mat in materials.keys():
                materials[mat] = materials[mat] + 1
            else:
                materials[mat] = 1
    return materials

if __name__ == '__main__':
    bridges_per_year = bridges_per_year('bridges.data', 'ERECTED')
    bridges = sum(bridges_per_year.values())
    print(f'{bridges} bridges built in Pittsburgh, PA.')
    print('Bridges per year of construction.')
    for i in sorted(bridges_per_year.keys()):
        if bridges_per_year[i] == 1:
            str1 = f'Year {i}: 1 bridge.'
        else:
            str1 = f'Year {i}: {bridges_per_year[i]} bridges.'
        print(str1)
    
    year_per_bridges = invert_dict(bridges_per_year)
    
    print('Years per number of bridges built.')
    for i in sorted(year_per_bridges.keys()):
        if i == 1:
            str1 = 'During the following year(s) 1 bridge was built:'
        else:
            str1 = f'During the following year(s) {i} bridges were built.'
        print(str1,year_per_bridges[i])
    
    
    materials = materials('bridges.data', 'MATERIAL', 'UNKNOWN')
    print('Bridges per material:')
    for i in sorted(materials.keys()):
        if materials[i] == 1:
            str1 = f'Material {i}: 1 bridge.'
        else:
            str1 = f'Material {i}: {materials[i]} bridges.'
        print(str1)
    
    import matplotlib.pyplot as plt
    
    plt.bar(materials.keys(),materials.values())
