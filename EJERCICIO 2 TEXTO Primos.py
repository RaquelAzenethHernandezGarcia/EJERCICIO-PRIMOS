# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# calcular el promedio de N numeros
	# y el mayor de ellos
	print("Ingrese la cantidad")
	n = input()
	i = 0
	mayor = 0
	suma = 0
	while i<n:
		print("Ingrese un numero: ")
		x = float(input())
		if x>mayor:
			mayor = x
		i = i+1
		suma = suma+x
	print("El mayor es ",mayor)
	print("El promedio es ",suma/n)

