mi_lista = [20,3,'Alex',1.4,7]
print(mi_lista)
mi_lista.append(10)
print(mi_lista)
mi_lista.append([100,23])
print(mi_lista)
mi_lista.remove('Alex')
print(mi_lista)
l3=mi_lista.index(7)# Saca la posición del num 7
print(l3)
l1=mi_lista.pop(1) # Saca el valor de la posición 1
print(l1)

print("Hola no me caes, no avisas")
lst = [12,"hola", "ay", 23]

x = lst.pop(1)
f = f"{x} YA PUES NO LEES"
print(f)