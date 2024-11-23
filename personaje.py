# ****************
# HERENCIA
# ****************

class Personaje:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y mi poder es {self.poder}")
        
class Superheroe(Personaje):
    def __init__(self, nombre, poder, ciudad):
        super().__init__(nombre, poder)
        self.ciudad = ciudad
    def salvar_la_ciudad(self):
        print(f"{self.nombre} está salvando {self.ciudad}")

class Villano(Personaje):
    def __init__(self, nombre, poder, companiero):
        super().__init__(nombre, poder)
        self.companiero = companiero
    def plan_maligno(self):
        print(f"Cuidado, {self.nombre} esta atacando usando {self.poder} junto con {self.companiero}")
        
heroe = Superheroe("Batman", "tener dinero", "Ciudad Gotica")
villano = Villano("Joker", "la locura", "El Pinguino")

heroe.salvar_la_ciudad()

villano.plan_maligno()