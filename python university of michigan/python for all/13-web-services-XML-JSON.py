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
