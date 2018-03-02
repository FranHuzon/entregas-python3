from funciones_temperaturas import encontrar_url_municipio,leer_url

municipio=input('''
Indique el municipio de sevilla 
que desee respetando las tíldes 
(pulse 0 para salir): ''')

while municipio!="0":

	url=encontrar_url_municipio(municipio)

	if url==False:
		print("Municipio no encontrado")
		municipio=input('''Indique el municipio de sevilla 
que desee respetando las tíldes 
(pulse 0 para salir): ''')

	else:
		lista=leer_url(url)
		print("La temperatura máxima para",municipio.upper(),"es",lista[0],"ºC y la mínima de",lista[1],"ºC")
		break
else:
	print("Fin del programa")