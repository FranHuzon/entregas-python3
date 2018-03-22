
headers={}

headers["Accept"]="application/json"
headers["user-key"]="7dc2fc52b46a2d3de6d017123ce59cca"

r=requests.get("https://developers.zomato.com/api/v2.1/categories",headers=headers)
if r.status_code==200:
	import json
	doc=r.json()
	print(doc)