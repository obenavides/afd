d={
0:{'1':1},
1:{'1':2},
2:{'1':3},
3:{'1':1}}

def AFD(d,q0,F,cinta):
    q = q0
    for simbolo in cinta:
        q=d[q][simbolo]
    if q in F:
        return 'Es divisible'
    else:
        return 'No es divisible'

for i in {'1','11','111','1111','11111','111111'}:
    print i,AFD(d,0,{3},i)
