# ****************
# POLIMORFISMO
# ****************

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        print(f"Hacer un sonido generico")
        
class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("guitarra")
    def tocar(self):
        print(f"Hacer sonido de {self.nombre}")
class Bateria(Instrumento):
    def __init__(self):
        super().__init__("bateria")
    def tocar(self):
        print(f"Hacer sonido de {self.nombre}")
class Piano(Instrumento):
    def __init__(self):
        super().__init__("piano")
    def tocar(self):
        print(f"Hacer sonido de {self.nombre}")
        
guitarra = Guitarra()
guitarra.tocar()