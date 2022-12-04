import requests

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat

# https://apis.net.pe/api-tipo-cambio.html

# 1. conectarme al sitio
response = requests.get(url)

response.json() # nos brinda la información en formato JSON
# 2. Recupero la informacion como json
res=response.json()

# obteniendo tipo cambio

# 3. Recupero valor tipo cambio - compra - venta
dolar_compra = res['compra']
dolar_venta = res['venta']


cantidad=float(input("ingrese la cantidad a comprar"))

print(cantidad*dolar_compra)