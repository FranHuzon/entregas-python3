def pasar_a_segundos(hh,mm,ss):
	
	segundos=(hh*3600)+(mm*60)+ss
	return segundos

def calcular_coste(segundos,precio):

	total_a_pagar=segundos*precio
	return total_a_pagar

def convertir_a_euros(centimos):

	euros=centimos/100
	return euros

print("-"*10,"Ejercicio 1","-"*10)

############### 
# Ejercicio 1 #
###############

print()

precio=float(input("Introduce la tarifa por segundo: "))
numllamadas=int(input("Introduce el número de llamadas realizadas: "))
duracion=[]
segundostotales=0
contador=1

for elem in range(numllamadas):
	lista=[]
	horas=int(input("Introduce el número de horas de la llamada: "))
	minutos=int(input("Introduce el número de minutos de la llamada: "))
	segundos=int(input("Introduce el número de segundos de la llamada: "))
	lista.append(contador)
	lista.append(pasar_a_segundos(horas,minutos,segundos))
	duracion.append(lista)
	lista=[]
	contador=contador+1 

for elem in duracion:
	segundostotales=segundostotales+elem[1]

for elem in duracion:
	print("El coste de la llamada",elem[0],"es.....",round(convertir_a_euros(float(calcular_coste(elem[1],precio))),2),"€")

print("El coste total de las llamadas es.....",round(convertir_a_euros(calcular_coste(segundostotales,precio)),2),"€")


print("-"*10,"Ejercicio 2","-"*10)

###############
# Ejercicio 2 #
###############

#He supuesto que la primera linea del fichero indica el precio por segundo
#de la llamada, en este caso 3 céntimos cada segundo.

print()

with open("comunicaciones.txt","r") as fichero:
	datos=fichero.readlines()

datos2=[]
for i in datos:
	datos2.append(i.replace("\n",""))

listatarifa=datos2[0].split(" ")
tarifa=int(listatarifa[1])

llamadas=[]

for i in datos2[1:]:
	cadallamada=[]
	hh,mm,ss=i.split(":")
	cadallamada.append(int(hh))
	cadallamada.append(int(mm))
	cadallamada.append(int(ss))
	llamadas.append(cadallamada)

sumasegundos=[]
totalsegundos=0

for i in llamadas:
	contador=0
	contador=contador+pasar_a_segundos(i[0],i[1],i[2])
	sumasegundos.append(contador)
	totalsegundos=totalsegundos+contador

numeracion=1

for i in sumasegundos:
	print("El coste de la llamada",numeracion,"es.....",round(convertir_a_euros(float(calcular_coste(i,tarifa))),2),"€")
	numeracion+=1

print("El coste total de las llamadas es.....",round(convertir_a_euros(calcular_coste(totalsegundos,tarifa)),2),"€")

