from lxml import etree

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

	return doc


municipio=input("Indique el municipio de sevilla que desee: ")

if not encontrar_url_municio(municipio):
	print("Municipio no encontrado")
else:
	print(encontrar_url_municio(municipio))

print(leer_url(municipio))
