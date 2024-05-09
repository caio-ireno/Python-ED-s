def contador(texto):
    palavras = texto.split()
    dici = {}
    for palavra in palavras:
        if palavra not in dici:
            dici[palavra]=1
        else:
            dici[palavra]+=1
    return dici

r = contador("o doce mais doce")
print(r)

dici = {}

dici['a']=1
dici['b']=2

dici.popitem()

print(dici)

dici["c"]=3

del dici['c']

print(dici)