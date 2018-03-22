with open("api_key_zomato","r") as fichero:
	key=fichero.read().replace("\n","")

import requests
headers={}

headers["Accept"]="application/json"
headers["user-key"]=key

r=requests.get("https://developers.zomato.com/api/v2.1/categories",headers=headers)
if r.status_code==200:
	import json
	doc=r.json()
	for i in doc["categories"]:
		print(i["categories"]["name"])