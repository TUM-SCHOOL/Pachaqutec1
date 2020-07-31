class  persona:
    __programa = "Pachacutec"
    def __init__(self, dni, nombre, apellido, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
    
    def getPrograma(self):
        return self.__programa

    def setPrograma(self, nuevo_programa):
        self.__programa = nuevo_programa

    @property
    def programa(self):
        return self.__programa
    
    @programa.setter
    def programa(self, nuevo_programa):
        self.__programa = nuevo_programa    



persona_1 = persona(32930347,"Heber","Milla","M")
print(persona_1.dni)
print(persona_1.nombre)

print(persona_1.getPrograma())
persona_1.setPrograma ("Pachaqutec - Backend")
print(persona_1.getPrograma())

print(persona_1.programa)
persona_1.programa = "Pachacutec - Bcakend 2"
print(persona_1.programa)


class Accion(persona):
    pass

accion = Accion (2333,"mmm","hasaf","iiiuiu")
print(accion.dni)

class Accion2(persona):
    def __init__(self,dni1, nombre, apellido, sexo, accion):
        super().__init__(dni1,nombre,apellido,sexo)
        self.accion = accion

accion2 = Accion2(44444,"hafsghfasf","agfgfga","dfasfdfas","cocinar")
print(accion2.dni)
print(accion2.accion)
