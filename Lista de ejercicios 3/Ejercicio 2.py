#Ejercicio 2

class Producto:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Catalogo:

    listaproducto = []

    def __init__(self,producto):
        self.listaproducto.append(producto)
    
    def agregar(self,p):
        self.listaproducto.append(p)

    def mostrar(self):
        for p in self.listaproducto:
            print(p)

p = Producto("Llanta")
c1 = Catalogo(p)

while True:
    print("""Elija una opción"
            1) Agregar producto
            2) Mostrar lista de productos
            3) Salir""")
    opcion = input()

    if opcion == '1':
        pr = Producto(input("Ingrese el nombre del producto: "))
        c1.agregar(pr)
        print('Se creó el producto')

    elif opcion == '2':
        print("Se muestra el catálogo de productos")
        c1.mostrar()

    elif opcion == '3':
        break
    else:
        print("Ingrese una opción válida")