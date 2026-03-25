import urllib.request, urllib.parse 
import http, json, ssl

url= input("Digite a url que o senhor deseja: ")
data = urllib.request.urlopen(url).read()
info = json.loads(data)
#json virou dicionário e lista 
soma = 0 
count = 0 
for item in info["comments"]:
    soma = soma +  item["count"]
    count = count + 1 
print(f"a soma é {soma}, e o contador é {count}")
