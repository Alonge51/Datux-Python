num = int(input("¿Cuántos números quiere ingresar?"))

lista_num = list()

for item in range(1,num+1):
    x = int(input(f'Ingrese el {item}) número: '))
    lista_num.append(x)
    pass

print(lista_num)

i = 0
while i < len(lista_num):
    if lista_num[i] % 2 == 0:
        print(f'El número {lista_num[i]} es múltiplo de 2')
    else:
        print(f'El número {lista_num[i]} no es múltiplo de 2')
    i += 1