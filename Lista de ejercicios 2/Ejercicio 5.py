a = 0
b = 0

while a <= 0:
    a = int(input("Ingrese el primer número: "))
    
    if a <= 0:
        print("El número debe ser mayor que cero")

while b <= 0:
    b = int(input("ingrese el segundo número: "))

    if b <= 0:
        print("El número debe ser mayor que cero")

def mult(a,b):
    return a*b

print(f'El producto de ambos números es: {mult(a,b)}')