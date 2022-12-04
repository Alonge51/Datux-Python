h = int(input('Ingrese la altura del triangulo: '))
for i in range(h):
    f = i+1 # valor fila
    g = 2*i+1
    print(' '*(h-f) +'#'* (g))