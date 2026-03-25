import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 0 

html = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_2369325.html").read()
soup = BeautifulSoup(html , 'html.parser')

tags = soup ('span')
for tag in tags:
    numeros = int(tag.text)
    count = count + numeros 

print (count)


