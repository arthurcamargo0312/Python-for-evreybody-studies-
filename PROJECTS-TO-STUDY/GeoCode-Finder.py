# Pedir um local (texto)
# Montar uma URL com esse texto
# Fazer requisição pra API
# Receber JSON
# Pegar o plus_code



import urllib.request, urllib.parse
import http, json, ssl

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

local = input("Digite o local: ")

# criando o dicionário corretamente
dic_localizacao = {}
dic_localizacao["q"] = local

url = serviceurl + urllib.parse.urlencode(dic_localizacao)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)

# pegando o plus_code
plus_code = js["features"][0]["properties"]["plus_code"]

print("Plus code:", plus_code)



