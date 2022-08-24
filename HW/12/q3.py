import requests
import json
from datetime import datetime

#32.6539° N, 51.6660° E

response=requests.get("https://api.sunrise-sunset.org/json?lat=32.6539&lng=51.6660&date=today").json()

sunrise=response['results']['sunrise']

sunset=response['results']['sunset']

saat_utc=datetime.utcnow()
saat_now=datetime.now()

ekhtelaf=saat_now - saat_utc


#sunrise
sunrise_utc=datetime.strptime(sunrise,'%I:%M:%S %p')
print(f" sunrise in isfahan: {(sunrise_utc + ekhtelaf).time()}")

#sunset
sunset_utc=datetime.strptime(sunset,'%I:%M:%S %p')
print(f" sunset in isfahan: {(sunset_utc + ekhtelaf).time()}")








