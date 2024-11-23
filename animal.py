# ****************
# ABSTRACCION
# ****************

from abc import ABC, abstractmethod

class Animal(ABC):
    cant_de_animales = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Animal.cant_de_animales += 1
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @classmethod
    def obtenerCantidadAnimales(cls):
        print(f"La cantidad actual de animales es de: {cls.cant_de_animales}")
        
class Perro(Animal):
    def hacer_sonido(self):
        print(f"Hacer sonido de perro")
class Gato(Animal):
    def hacer_sonido(self):
        print(f"Hacer sonido de gato")
        
perro = Perro("Cholo")
gato = Gato("Gatica")

perro.hacer_sonido()
gato.hacer_sonido()

Animal.obtenerCantidadAnimales()