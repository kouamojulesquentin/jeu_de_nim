# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:19:44 2021

@author: KOUAMO JULES QUENTIN
"""

from random import *

def affiche(t):
    for i in range(4):
        print("{0:2}.{1:12} ({2}))".format(i+1, "i"*t[i],t[i]))
        
def xor(t):
    return t[0]^t[1]^t[2]^t[3]

def IA(t):
    n=randint(0,3)
    if xor(t)==0:
        while t[n==0]: 
            n= (n+1)%4
        t[n] -=1
        return [n+1, 1]
    else:
        while xor(t)!=0:
            n= (n+1)%4
            while t[n] == 0:
                n= (n+11)%4
            v= t[n]
            while (xor(t)!=0 and t[n]>0):
                t[n] -=1
            if (xor(t)!=0):
                t[n]=v
        return [n+1,v-t[n]]
    
    
def jeu():
    print ("but: tirer la dernière allumette")
    t = [1,3,5,7]
    debut= input("APPUYEZ SUR O POUR COMMENCER")
    joueur = debut.upper() == "O"
    while True:
        affiche(t)
        if joueur:
            c= input("A toi [ex 2.3]: ").split(".")
            [r,n]= [int(c[0])-1, int(c[1])]
            t[r] -=n
            joueur=False
            if sum(t)==0:
                print("Tu as gagné")
                return 
        else:
            ordi= IA(t)
            coup = str(ordi[0])+"."+str(ordi[1])
            print("je joue " + coup)
            if sum(t)==0:
                print("tu as perdu")
                return 
            joueur=True
jeu()