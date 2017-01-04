#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
url = 'http://www.sismologia.cl/links/ultimos_sismos.html'
web = requests.get(url)
html = BeautifulSoup(web.text,"lxml")
tabla = html.find('table')
for col in tabla.findAll("tr"):
    a = col.findAll("th")[0].getText()
    b = col.findAll("th")[1].getText()
    c = col.findAll("th")[2].getText()
    d = col.findAll("th")[3].getText()
    e = col.findAll("th")[4].getText()
    f = col.findAll("th")[5].getText()
    g = col.findAll("th")[6].getText()

    if a > 0:
        break
        
for col in tabla.findAll("tr",attrs={"class": "par"},limit=1):
    z = col.findAll("a")[0:]
    x = col.findAll("td")[2:3]
    y = col.findAll("td")[3:4]
    w = col.findAll("td")[4:5]
    u = col.findAll("td")[5:6]
    t = col.findAll("td")[7:8]
    s = col.findAll("td")[:-1]
    if col.getText < 0 :
        break
    else:
        for z in col.findAll("a"):
            print a,": "+z.string
        for la in col.findAll("td")[2:3]:
            print c,": "+la.string
        for lo in col.findAll("td")[3:4]:
            print d,": "+lo.string
        for pr in col.findAll("td")[4:5]:
            print e,": "+pr.string
        for ma in col.findAll("td")[5:6]:
            print f,": "+ma.string
        for loc in col.findAll("td")[-1]:
            print 'Localidad:',loc.string.encode('utf-8'), '\nFuente:Centro Sismológico Nacional, Universidad de Chile. www.sismologia.cl'
