print("Ejercicio 1 Hoja 2")
print("Introduzca un Numero ")
n=input()
a="*"
for x in range (int (n)):
    print(a)
    a=a+"*"
#--------------------------------------------

print("Ejercicio 2")
print("Introduzca un Número")
n2=input()
print("--------------")
for i in range (1+int(n2)):  

    print(n2,end=",")
    n2= int(n2)-1
print()
#------------------------------------------
print("Ejercicio 3")
print("Introduzca un Número")
n3=int (input())
i=2
while n3 % i != 0:
    i+=1
if i == n3:
     print(str(n3)+" Es un Número Primo")
else:
    print(str(n3)+" No Es Un Número Primo")    
