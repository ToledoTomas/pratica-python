class Robot:
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un robot de tipo {self.tipo}")
        
    def hacer_truco(self):
        if self.tipo == "Humanoide":
            print(f"Soy un {self.tipo} y por ende, puedo moverme")
        else:
            print(f"No soy un Humanoide, esta todo ok")
    
    
robot1 = Robot("Tesla", "Auto")
robot2 = Robot("Robotin", "Humanoide")

robot1.saludar()
robot2.saludar()
robot1.hacer_truco()
robot2.hacer_truco()

