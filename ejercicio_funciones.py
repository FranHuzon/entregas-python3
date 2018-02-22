def pasar_a_segundos(h,m,s):
	
	segundos=(h*3600)+(m*60)+s
	return segundos

def calcular_coste(segundos,precio):

	total_a_pagar=segundos*precio
	return total_a_pagar

