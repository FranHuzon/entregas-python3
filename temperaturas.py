def encontrar_url_municio(municipio):
	from lxml import etree
	doc=etree.parse('id_municipios_sevilla.xml')

	municipios=doc.findall("municipio")
	for municipio in municipios:
		num_id=municipio.attrib["value"].split("-")

		return "http://www.aemet.es/xml/municipios/localidad_"+num_id[1].replace("id","")+".xml"

municipio=input("Indique el municipio de sevilla que desee: ")

print(encontrar_url_municio(municipio))


