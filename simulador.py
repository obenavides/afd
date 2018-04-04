#!/usr/bin/python
from sys import argv

def AFD(d,q0,F,cinta):
    q=q0
    for simbolo in cinta:
        q=d[q,simbolo]
    return q in F
mensaje={True:'Aceptada',False:'Rechazada'}

d={}
F=set()
programa=open(argv[1])
for linea in programa:
    q,s,n=linea.split()
    if '*' in q:
        q=q.strip('*')
        F.add(q)
    d[q,s]=n
programa.close()

entrada=open(argv[2])
for cinta in entrada:
    cinta=cinta.strip()
    print 'La entrada '+cinta+' es '+mensaje[AFD(d,'0',F,cinta)]
entrada.close()
