# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:43:07 2023

@author: Iozzi
"""
import datetime

import person 
import csv

# from person import Person

p1 = person.Person('Marco', 'Bilucaglia', \
            datetime.datetime.strptime('27061988', '%d%m%Y'))
print(p1.firstname)
p2 = person.Person(lastname='Conti', firstname='Sara', \
            birthdate=datetime.datetime.strptime('18051996', '%d%m%Y'))
print(p1.birthdate)
print(p1.age())
print(p2.firstname)
print(p2.birthdate)
print(p2.age())

p3 = person.Person(lastname='Casiraghi', firstname='Chiara', \
            birthdate=datetime.datetime.strptime('31121997', '%d%m%Y'))

s1 = person.Student(firstname='Francesco', \
                    lastname='Minetti', \
                    birthdate=datetime.datetime.strptime('30081985', '%d%m%Y'))
print(s1.firstname)
print(s1.age())
s2 = person.Student(lastname='Ignoto', \
                    birthdate=datetime.datetime.strptime('30081985', '%d%m%Y'))
print(s2)

persons_list = []
persons_list.append(p1)
persons_list.append(p2)
persons_list.append(p3)

with open('persone.csv','w', newline='') as f_output:
    # dict_writer = csv.DictWriter(f_output, ['firstname', 'lastname', 'birthdate'])
    dict_writer = csv.DictWriter(f_output, \
                                 persons_list[0].person_2_dict().keys())
    dict_writer.writeheader()
    for persona in persons_list:
        dict_writer.writerow(persona.person_2_dict())
        