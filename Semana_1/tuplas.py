tup = (1,"hola", [3,4],1)
print("cantidad 1->",tup.count(1))
print("posicion 1->",tup.index(1))
print("hola->",tup.count("hola"))
print("posicion hola->",tup.index("hola"))

tup = tuple(range(4,10))
print(tup)
tupla = 1,2,"hola"
print(tupla)
otra = tupla, (6,7,8)
print(otra)
x,y,z=tupla
print(x, y, z)