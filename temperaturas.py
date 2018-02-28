def encontrar_url_municio(municipio):
	from lxml import etree
	doc=etree.parse('id_municipios_sevilla.xml')

	municipios=doc.findall("municipio")
	for municipio in municipios:
		num_id=municipio.attrib["value"].split("-")
		url="http://www.aemet.es/xml/municipios/localidad_"+num_id[1].replace("id","")+".xml"
		return url

def leer_url(url):
	import webbrowser
	web=webbrowser.open(url)
	return web


municipio=input("Indique el municipio de sevilla que desee: ")

print(leer_url(encontrar_url_municio(municipio)))


