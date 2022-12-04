def aumento(l:list):
    i = 0
    while i < len(l):
        l[i] = l[i] + 1
        i += 1
    print(l)

lista = list()
n = 0
while n < 4:
    x = int(input('Ingrese un número: '))
    lista.append(x)
    n += 1

print(lista)

print('A continuación la lista modificada:')

aumento(lista)