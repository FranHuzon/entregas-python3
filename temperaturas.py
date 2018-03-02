from funciones_	temperaturas.py import encontrar_url_municio,leer_url

municipio=input("Indique el municipio de sevilla que desee (respetando las tíldes): ")

url=encontrar_url_municio(municipio)
lista=leer_url(url)
print("La temperatura máxima para",municipio.upper(),"es",lista[0],"ºC y la mínima de",lista[1],"ºC")


if not encontrar_url_municio(municipio):
#	print("Municipio no encontrado")
#else:
#	print(encontrar_url_municio(municipio))
# 
#print(leer_url(municipio))