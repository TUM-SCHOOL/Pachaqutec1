nota = int(input("Ingrese su nota: "))
if nota >= 14:
    print("Aprobaste")
elif nota < 10:
    print("Desaprobaste")
else:
    print("Aun tienes chance")

input("continuar?")

suma = 0
numero = 1
iteracion = 0
print ("Valores iniciales")
print("Numero es: "+str(numero))
print("La Suma es: "+str(suma))
print("####################")
while numero <= 10:
    iteracion = iteracion+1
    suma = suma+numero
    numero=numero+1
    print("Iteracion numero: "+str(iteracion))
    print("Numero es: "+str(numero))
    print("La Suma es: "+str(suma))
    print("-----------------------")
print("La suma final es: "+str(suma))    

input("continuar?")
palabras = ["gato", "ventana", "defenestrado"]
for p in palabras:
    print(p)

input("continuar?")
for i in range(0,10,3):
    print(i)
print("FIN!")   

palabras = ["gato", "ventana", "defenestrado"]
for val in palabras:
    if val == "ventana":
        break
    print(val)
print("The End")    
