import requests
import sys
from datetime import datetime
import re

data = datetime.now()

data1 = data.strftime("%d/%m/%Y %H:%M:%S")

if sys.argv[1:] == []:

    r = requests.get('https://www.worldometers.info/coronavirus/')

    texto = r.text
    
    padrao_casos = re.findall(r'aaa\">(\d+,\d+,\d+)\s<', texto)
    casos = padrao_casos[0]

    padrao_mortes = re.findall(r'<span>(\d+,\d+)</span>', texto)
    mortes = padrao_mortes[0]

    padrao_recuperados = re.findall(r'<span>(\d+,\d+)</span>', texto)
    recuperados = padrao_recuperados[1]

    print(casos + " ; " + mortes + " ; " + recuperados)

else:
    
    r = requests.get('https://www.worldometers.info/coronavirus/country/{}/'.format(sys.argv[1]))
    
    texto = r.text
    
    padrao_casos = re.findall(r'aaa\">(\d+,\d+)\s<', texto)
    casos = padrao_casos[0]

    padrao_mortes = re.findall(r'<span>(\d+,\d+)</span>', texto)
    mortes = padrao_mortes[0]

    padrao_recuperados = re.findall(r'<span>(\d+,\d+)</span>', texto)
    recuperados = padrao_recuperados[1]

    print(casos + ";" + mortes + ";" + recuperados)

    
    
    


   


