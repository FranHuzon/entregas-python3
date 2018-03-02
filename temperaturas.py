from lxml import etree
import time
def encontrar_url_municio(municipio):
	
	doc=etree.parse('id_municipios_sevilla.xml')

	municipios=doc.findall("municipio")
	for i in municipios:
		if municipio.upper()==i.text.upper():
			num_id=i.attrib["value"][-5:]
			url="http://www.aemet.es/xml/municipios/localidad_"+num_id+".xml"
			return url
	return False


def leer_url(url):
	
	doc=etree.parse(url)
	prediccion=doc.findall('prediccion/dia')
	lista=[]
	for i in prediccion:
		if i.attrib["fecha"]==time.strftime("%Y-%m-%d"):
			lista.append(i.find("temperatura/maxima").text)
			lista.append(i.find("temperatura/minima").text)
			return lista
	return False


municipio=input("Indique el municipio de sevilla que desee (respetando las tíldes): ")
url=encontrar_url_municio(municipio)
lista=leer_url(url)
print("La temperatura máxima para",municipio.upper(),"es",lista[0],"ºC y la mínima de",lista[1],"ºC")


