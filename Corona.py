import requests
import sys
from datetime import datetime

#import re

data = datetime.now()

data1 = data.strftime("%d/%m/%Y %H:%M:%S")

if sys.argv[1:] == []:

    r = requests.get('https://www.worldometers.info/coronavirus/')

    texto = str(r.content)
    
    #padrao = re.compile(r"\d\d\d,\d\d\d")

    #achados = padrao.finditer(texto)

    #for achado in achados:
    #print(achado)
    
    print(texto[384:393] + " ; " + texto[404:410] + " ; " + texto[9788:9795] + " ; " + data1 )

elif sys.argv[1] == "brazil":

    r1 = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')

    texto1 = str(r1.content)
    
    if texto1[8930] == ">":
        
        print(texto1[375:381] + " ; " + texto1[392:395] + " ; " + texto1[8931:8934] + " ; " + data1 )
    
    else:
        
        print(texto1[375:381] + " ; " + texto1[392:395] + " ; " + texto1[8930:8933] + " ; " + data1 )
   
elif sys.argv[1] == "italy":

    r2 = requests.get('https://www.worldometers.info/coronavirus/country/italy/')

    texto2 = str(r2.content)
    
    if texto2[8934] == ">":
        
        print(texto2[374:381] + " ; " + texto2[392:398] + " ; " + texto2[8935:8941] + " ; " + data1 )
        
    else:
        
       print(texto2[374:381] + " ; " + texto2[392:398] + " ; " + texto2[8934:8940] + " ; " + data1 )

elif sys.argv[1] == "us":

    r3 = requests.get('https://www.worldometers.info/coronavirus/country/us/')

    texto3 = str(r3.content)
    
    if texto3[8964] == ">":
        
        print(texto3[382:389] + " ; " + texto3[400:405] + " ; " + texto3[8965:8971] + " ; " + data1 )
        
    else:

        print(texto3[382:389] + " ; " + texto3[400:405] + " ; " + texto3[8964:8970] + " ; " + data1 )

elif sys.argv[1] == "spain":

    r4 = requests.get('https://www.worldometers.info/coronavirus/country/spain/')

    texto4 = str(r4.content)
    
    if texto4[8934] == ">":
        
        print(texto4[374:381] + " ; " + texto4[392:398] + " ; " + texto4[8935:8941]  + " ; " + data1)    
        
    else:
        
        print(texto4[374:381] + " ; " + texto4[392:398] + " ; " + texto4[8934:8940]  + " ; " + data1)
