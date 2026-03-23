"""
Extracting Data from XML

"""
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


inp = input("Enter location: ")

data = urllib.request.urlopen(inp).read()
tree = ET.fromstring(data)
lista_contagem = tree.findall(".//count")
count = 0 

for number in lista_contagem:
    number = int(number.text)
    count = count + number

print(count)

'''
Ler dados da internet (urllib)

Interpretar XML (ElementTree)

Navegar em estrutura (.findall)

Extrair dados (.text)

Trabalhar com dados reais (API-like)
'''


import urllib.request, urllib.parse
import http, json, ssl

url = input("Digite a url que o senhor deseja: ")
data = urllib.request.urlopen(url).read()
info = json.loads(data)
# json virou dicionário e lista
soma = 0
count = 0
for item in info["comments"]:
    soma = soma + item["count"]
    count = count + 1
print(f"a soma é {soma}, e o contador é {count}")
