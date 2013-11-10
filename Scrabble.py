#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string

#Lista que contendra el abecedario
#de la forma XX
L = []

#inicializamos la lista
for i in string.ascii_uppercase:
    L.append(i+i)


#procedimiento que dado una palabra
#borra de la lista todo par de letras
#consecutivas
def Contador(Palabra):
    for I in L:
        if Palabra.find(I)>=0:
            L.remove(I)



if __name__ == "__main__":
    Archivo = open('sowpods.txt','rU')
    Linea = Archivo.readline()
    
    while Linea != "":
        Contador(Linea)
        Linea = Archivo.readline()

    for i in L:
        print i[0]
