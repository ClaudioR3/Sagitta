'''
Created on 04 lug 2016

@author: claudio
'''
from Query import *
import sys

def riempiArgs(lista):
    args={}
    i=0
    key=""
    for arg in sys.argv:
        if i>1:
            if arg[0]=='-':
                key=arg[1:]
            else :
                if key!="":
                    args[key]=arg
                    key=""
        i+=1
    return args

def definisci_args():
    risultato=[]
    for arg in sys.argv:
        risultato.append(arg)
    return risultato

def calcola_quantity(tot):
    quantity=0
    for i in tot:
        quantity+=1
    return quantity

def help():
    lista=["find","help","describe"]
    print "Lista di comandi disponibili"
    for elem in lista:
        print elem+"  "

q=Query()
args=definisci_args()
operazione=args[1]
if operazione=="find":
    args=riempiArgs(args[2:]) 
    risultato=q.do_query(args)
    print "%d risultati"%(calcola_quantity(risultato))
elif operazione=="describe":
    for e in q.do_describe():
        print e
elif operazione=="help":
    help()
else:
    print operazione+"  comando sconosciuto"
    help()
    
    
    
    
    
    
    
    