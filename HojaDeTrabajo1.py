print("---Hoja de Trabajo 1")
print()
print("Ingrese Su Peso (kg)")
peso= float(input())
print()
print ("Ingrese Su Estatura (m)")
estatura =float(input())
imc=float(0);
imc=peso/estatura**2
print("Su Indice de Masa Corporal es de ","{0:.2f}".format(imc))
print()
print()

