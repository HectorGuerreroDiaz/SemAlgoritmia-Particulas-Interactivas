from algoritmos import distancia_euclidiana
import json


class Particula:
    def __init__(self, id=0, origenX=0, origenY=0, destinoX=0, destinoY=0, velocidad=0, red=0, green=0, blue=0, distancia=0.0):
        self.__distancia = distancia_euclidiana(origenX, destinoX, origenY, destinoY)
        self.__id=id
        self.__origenX=origenX
        self.__origenY=origenY
        self.__destinoX=destinoX
        self.__destinoY=destinoY
        self.__velocidad=velocidad
        self.__red=red
        self.__green=green
        self.__blue=blue

    @property
    def id(self):
        return self.__id

    @property
    def origenX(self):
        return self.__origenX
    @property
    def origenY(self):
        return self.__origenY

    @property
    def destinoX(self):
        return self.__destinoX
    
    @property
    def destinoY(self):
        return self.__destinoY

    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def RGB(self):
        return str(self.__red) + "," + str(self.__green) + "," + str(self.__blue)

    def __str__(self):
        return(
            'ID: '+ str(self.__id) + '\n'+
            'OrigenX: '+ str(self.__origenX) + '\n'+
            'OrigenY: '+ str(self.__origenY) + '\n'+
            'DestinoX: '+ str(self.__destinoX) + '\n'+
            'DestinoY: '+ str(self.__destinoY) + '\n'+
            'Distancia: '+ str(self.__distancia) + '\n'+
            'Velocidad: '+ str(self.__velocidad) + '\n'+
            'Red: '+ str(self.__red) + '\n'+
            'Green: '+ str(self.__green) + '\n'+
            'Blue: '+ str(self.__blue) + '\n'
        )

    def to_dict(self):
        return {
            "id" : self.__id,
            "origenX" : self.__origenX,
            "origenY" : self.__origenY,
            "destinoX" : self.__destinoX,
            "destinoY" : self.__destinoY,
            "velocidad" : self.__velocidad,
            "red" : self.__red,
            "green" : self.__green,
            "blue" : self.__blue
        }


class ListaParticula:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, Particula):
        self.__particulas.insert(0, Particula)  

    def agregar_final(self, Particula):
        self.__particulas.append(Particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        ) 

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0



"""
L1 = Particula(id=1234, origenX=12, origenY=12, destinoX=12, destinoY=12, velocidad=203, red=1, green=0, blue=120, distancia=70.0)
L2 = Particula(4321, 12, -12, 12, -12, 302, 1, 0, 120, 90.0)
ListaParticulas = ListaParticula()
ListaParticulas.agregar_final(L1)
ListaParticulas.agregar_inicio(L2)
ListaParticulas.mostrar()
"""