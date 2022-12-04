def mayor(numero1,numero2):
    if numero1 < numero2:
        print(f'El número {numero2} es el mayor')
    elif numero1 > numero2:
        print(f'El número {numero1} es el mayor')
    else:
        print('Los números son iguales')

mayor(int(input('Ingrese el primer número: ')),int(input('Ingrese el segundo número: ')))