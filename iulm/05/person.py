# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:39:49 2023

@author: Iozzi
"""

import datetime

class Person:
    def __init__(self, \
                firstname = 'Unknown', \
                lastname = 'Unknown', \
                birthdate = 'Unknown'):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        
    def age(self):
        age = datetime.datetime.today() - self.birthdate
        return age.days // 365
    
    def person_2_dict(self):
        d={}
        d['firstname']=self.firstname
        d['lastname']=self.lastname
        d['birthdate']=self.birthdate
        return d

class Student(Person):
    def __init__(self, firstname = 'Unknown', lastname='Unknown', \
                 birthdate='Unknown', academic_program = 'PhD'):
        # creo una persona con nome, cognome e data di nascita
        # usando i parametri forniti
        super().__init__(firstname, lastname, birthdate)
        self.academic_program = academic_program
