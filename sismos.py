#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
url = 'http://www.sismologia.cl/links/tabla.html'
web = requests.get(url)
html = BeautifulSoup(web.text,"lxml")
tabla = html.find("table")
print("Información de los últimos sismos en Chile.")
for row in tabla.findAll("tr", limit=4):
    if row.find_all('td') == []:
        pass
    else:
        a = row.findAll("a")[0:1]
        b = row.findAll('td')[1:2]
        c = row.findAll('td')[2:3]
        for fec in a:
            print("Fecha:",fec.getText())
        for lug in b:
            print("Lugar",lug.getText().encode("latin-1").decode("utf-8"))
        for mag in c:
            print("Magnitud",mag.getText())
            print('-------------------------')
print("Fuente:Centro Sismológico Nacional, Universidad de Chile. www.sismologia.cl")
