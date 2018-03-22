with open("api_key_zomato","r") as fichero:
	key=fichero.read().replace("\n","")

import requests

headers={"Accept":"application/json","user-key":key}
ciudad=input("Dime la ciudad en inglés: ").replace(" ","%20")

r=requests.get("https://developers.zomato.com/api/v2.1/cities?q="+ciudad,headers=headers)
if r.status_code==200:
	import json
	doc=r.json()
	for i in doc["location_suggestions"]:
		print(i)