def Complejo(c1,c2):
    print(f"Ahora las tres operaciones de numeros complejos:\n")
    suma= c1+c2
    print(f"suma:{suma}")
    producto=c1*c2
    print(f"producto:{producto}")
    division=c1/c2
    print(f"division:{division}")

def Operaciones(a,b):
    m=a%b
    print(f"modulo ó resto, de {a} y {b}, es:{m}")
    divInt=a//b
    print(f"division entera, de {a} y {b}, es:{divInt}")
    pot = a**b
    print(f"potencia, de {a} a la {b}, es:{pot}")
    logic = a>=b
    print(f"es verdad que {a} es mayor o igual a {b}? Resp:{logic}")

print("Ingrese dos numeros complejos")
print("Ingrese componente real del primer numero")
r1=input()
r1=float(r1)
print("Ingrese componente imaginario del primer numero")
i1=input()
i1=float(i1)
c1=r1+i1*(1j)
print(f"El primer numero complejo es: {c1}")

print("Ingrese componente real del segundo numero")
r2=input()
r2=float(r2)
print("Ingrese componente imaginario del segundo numero")
i2=input()
i2=float(i2)
c2=r2+i2*(1j)
print(f"El segundo numero complejo es: {c2}")

Complejo(c1,c2)

print("Ingresa dos numeros reales:")
a=float(input())
b=float(input())
Operaciones(a,b)





