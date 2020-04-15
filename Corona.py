import requests
import sys
from datetime import datetime
import re

data = datetime.now()

data1 = data.strftime("%Y/%m/%d %H:%M:%S")

if sys.argv[1:] == []:
    
    pais = ""
       
else:
    
    pais = "/country/%s/" % sys.argv[1]
    
r = requests.get('https://www.worldometers.info/coronavirus'+ pais)

texto = r.text

padrao_casos = re.findall(r'\">(.*\d+,\d+)\s<', texto)
casos = padrao_casos[0]

padrao_mortes_recuperados = re.findall(r'<span>(.*.*\d+)</span>', texto)
mortes = padrao_mortes_recuperados[0]
recuperados = padrao_mortes_recuperados[1]

      
print(casos + " ; " + mortes + " ; " + recuperados + " " + data1)
    
    
