
print("hello word ")
import requests

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)
if response.status_code == 200:
    html = response.text
    #print(html)
    f= open("apprentissage",'w')
    f.write( html )
    f.close()
else:
    print("ERROR", response.status_code)

 
 
print("FIN")





