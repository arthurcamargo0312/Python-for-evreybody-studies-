# Importa a biblioteca de comunicação de rede
import socket

# Cria um socket para comunicação TCP pela internet
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor data.pr4e.org na porta 80 (HTTP)
mysock.connect(("data.pr4e.org", 80))

# Cria uma requisição HTTP pedindo o arquivo romeo.txt
# GET -> tipo de requisição HTTP (baixar algo)
# HTTP/1.0 -> versão do protocolo
# \r\n\r\n -> indica o final do cabeçalho HTTP
# .encode() -> transforma a string em bytes para enviar pela rede
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

# Envia a requisição para o servidor
mysock.send(cmd)

# Loop para receber os dados enviados pelo servidor
while True:

    # Recebe até 512 bytes por vez
    data = mysock.recv(512)

    # Se não chegou mais dados, termina o loop
    if len(data) < 1:
        break

    # Converte os bytes recebidos para texto e imprime
    print(data.decode())

# Fecha a conexão com o servidor
mysock.close()


print (ord('H'))
print (ord('e'))


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")


tags = soup("a")
for tag in tags:
    print(tag.get("href", None))


# Ignorar erros de certificado SSL (ajuda em sites HTTPS)
# Abre a URL, lê o conteúdo e guarda em 'html'
# O BeautifulSoup organiza o HTML para podermos pesquisar
# Procura todas as tags <a> (âncoras/links)
# Pega apenas o conteúdo do atributo 'href' (o endereço)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0

html = urllib.request.urlopen(
    " http://py4e-data.dr-chuck.net/comments_2369325.html").read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
for tag in tags:
    numeros = int(tag.text)
    count = count + numeros

print(count)
