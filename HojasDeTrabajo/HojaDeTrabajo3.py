print("Hoja de Trabajo 3")
print("---------------------------")


print("Ejercicio 1")
print("Ingrese Contraseña ")
contr = str(input())
print("Confirmar Contraseña")
confir=str(input())
if contr.upper()==confir.upper():
    print("Contraseña Correcta ")
elif contr.upper()!=confir.upper():
    print("Error En La Contraseña ")
print("----------------------------------")
print("Ejercicio 2")
print("Ingrese Nombre ")
nombre=input()
print("Ingrese su Genero (H o M)")
genero=input()
if genero=="M":
    if  nombre.lower()<"m":
        grupo="B"
    else:
        grupo = "A"
else:
    if  nombre.lower()>"n":
        grupo="A"
    else:
        grupo="B"
print("Su Grupo es : "+grupo)