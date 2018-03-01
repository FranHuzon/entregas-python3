from lxml import etree
import time
def encontrar_url_municio(municipio):
	
	doc=etree.parse('id_municipios_sevilla.xml')

	municipios=doc.findall("municipio")
	for i in municipios:
		if municipio.upper()==i.text.upper():
			num_id=i.attrib["value"].split("-")
			url="http://www.aemet.es/xml/municipios/localidad_"+num_id[1].replace("id","")+".xml"
			return url
	return False


def leer_url(url):
	
	doc=etree.parse(encontrar_url_municio(municipio))
	prediccion=doc.findall('root/prediccion/dia')
	lista=[]
	for i in prediccion:
		if i.find(dia).attrib["fecha"]==time.strftime("%y%m%d").replace("/","-")[::-1]:
			lista.append(i.find("temperatura/maxima").text)
			lista.append(i.find("temperatura/minima").text)
			return lista
	return False


municipio=input("Indique el municipio de sevilla que desee (respetando las tíldes): ")
hoy=input("Introduce la fecha de hoy (seperada en guiones): ")
print(time.strftime("%y%m%d").replace("/","-"))
print("La temperatura máxima para",municipio.upper(),"es",leer_url(municipio)[0],"ºC y la mínima de",leer_url(municipio)[1],"ºC")
#if not encontrar_url_municio(municipio):
#	print("Municipio no encontrado")
#else:
#	print(encontrar_url_municio(municipio))
#
#print(leer_url(municipio))
