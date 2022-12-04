def saludar(n):
    print(f'Hola, mucho gusto {n}')

def suma(a,b):
    return a + b

def despedirse(m):
    print(f'Hasta pronto {m}')

while True:
    print("""Elija una opción"
            1) Saludar
            2) Sumar
            3) Despedir""")
    opcion = input()

    if opcion == '1':
        n = input('Ingrese su nombre: ')
        saludar(n)
        break

    elif opcion == '2':
        print(suma(input("Ingrese el primer número: "),input("Ingrese el primer número: ")))
        break

    elif opcion == '3':
        n = input('Ingrese su nombre: ')
        despedirse(n)
        break

    else:
        print("Ingrese una opción válida")