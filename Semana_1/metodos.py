#recibir listas
def sumar(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

lista=[4,5,10]
sumar(lista)

#recibir dicionarios
def sumar1(**numbers):
    print(numbers)
    #print(numbers["number1"]+numbers["number2"])
    for k in numbers:
        print(f"La clave es:{k} y el valor es: {numbers[k]}")
sumar1(num1=4,num2=7,num3=9)    

class Persona:
    def saludar(self):
        print("Hola, como estás?")

persona = Persona()
persona.saludar()

class Persona1:
    def __init__(self):
        print("hola")

persona1 = Persona1()

class Persona2:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print(f"Hola, {self.nombre} {self.apellido}")

persona2 = Persona2("Heber", "Milla")

print("Borrando persona")
del(persona2)

print(persona2)