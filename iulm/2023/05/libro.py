# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:42:51 2023

@author: fabri
"""

class Libro:
    def __init__(self, isbn, autore, titolo, lingua = 'IT'):
        self.isbn = isbn
        self.autore = autore
        self.titolo = titolo
        self.lingua = lingua

    def ISBNValido(self):
        '''
        La funzione ISBNValido restituisce una coppia di valori,
        cioè una t-upla (è come una lista ma non modificabile).
        Il primo valore è True/False se il codice è corretto o meno,
        il secondo valore è 'OK', se il codice è valido, o
        un messaggio di errore se il codice non è valido.
        
        La sintassi 
        
        return a,b
    
        è un modo sintetico di restituire due valori.
        '''
        isbn = self.isbn
        # non valido se non ha 10 o 13 caratteri
        if len(isbn) == 10:
            # Somma pesata delle prime 9 cifre
            # 10 x (prima cifra) + 9 x (seconda cifra) + 8 x (terza cifra) ...
            # fino a 1 x (nona cifra)
            somma = 0
            for i in range(9):
                # sommo solo se il carattere è una cifra
                # altrimenti c'è un errore
                if isbn[i].isdigit():
                    somma += int(isbn[i]) * (10 - i)
                else:
                    return False, 'Errore: alcuni caratteri non numerici'
            # per l'ultimo carattere, posso avere una X che
            # rappresenta 10 quindi devo distinguere i casi
            # se è X aggiungo 10
            # se è una cifra, aggiungo la cifra
            if isbn[9] == 'X':
                somma += 10
            elif isbn[9].isdigit():
                somma += int(isbn[9])
            else:
                return False, 'Ultimo carattere non numerico e diverso da X'
            # se l'ISBN è corretto, la somma deve essere 
            # un multiplo di 11
            if somma % 11 == 0:
                return True, 'OK'
            else:
                return False, 'Il codice non è corretto'
        elif len(isbn) == 13:
            # Somma pesata di tutte le cifre
            # 1 x (prima cifra) + 3 x (seconda cifra) + 1 x (terza cifra) ...
            # alternativamente 1 e 3 fino a 1 x (tredicesima cifra)
            somma = 0
            for i in range(13):
                # sommo solo se il carattere è una cifra
                # altrimenti c'è un errore
                if isbn[i].isdigit():
                    if i % 2 == 0:
                        moltiplicatore = 1
                    else:
                        moltiplicatore = 3
                    somma += int(isbn[i]) * moltiplicatore
                else:
                    return False, 'Errore: alcuni caratteri non numerici'
            # se l'ISBN è corretto, la somma deve essere 
            # un multiplo di 10
            if somma % 10 == 0:
                return True, 'OK'
            else:
                return False, 'Il codice non è corretto'
        else:
            return False, 'Lunghezza codice non uguale a 10 o 13'
        
        
