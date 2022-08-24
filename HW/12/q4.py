import json
from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
from datetime import datetime

response = requests.get("https://time.ir")

soup =BeautifulSoup(response.content , "lxml")

# print(soup.prettify())


t1=soup.find_all("span",attrs={"class":'inlineBlock ltr text-nowrap'})
t1=[i.text for i in t1 ]
oghat= {"azane_sobh":None ,"tolooe_khorshid":None, "azane_zohr":None, "ghoroobe_khorshid":None, "azane_maghreb":None, "nime_shab":None}
c=0
for i in oghat:
    oghat[i] =datetime.strptime(unidecode(t1[c]),"%H : %M").strftime("%I : %M %p")
    c += 1

# print(oghat)

with open("oghat.json" , 'w') as f :
    json.dump(oghat,f,indent=2)

"""
<span id="ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon" class="inlineBlock ltr text-nowrap">۱۳ : ۰۷</span>
"""


