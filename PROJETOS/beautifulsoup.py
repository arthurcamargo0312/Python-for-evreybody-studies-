from bs4 import BeautifulSoup

html = "<html><head><title>Teste</title></head><body></body></html>"

soup = BeautifulSoup(html, "html.parser")

print(soup.title.string)
