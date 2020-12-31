arch = open("historial_precision.txt")
arch2 = open("checks.txt","w")

for linea in arch:
	lista= linea.strip().split(" tuvo precision de: ")


	if float(lista[-1]) >= 0.80:
		arch2.write(linea)
	

arch.close()
arch2.close()
