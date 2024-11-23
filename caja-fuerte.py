# ****************
# ENCAPSULAMIENTO 
# ****************

class CajaFuerte:
    def __init__(self, clave, cantidad):
        self.__clave = clave
        self.__cantidad = cantidad

    def verificar_clave(self, clave):
        return self.__clave == clave
    
    def obtener_cantidad(self, clave):
        if self.verificar_clave(clave):
            return self.__cantidad
        else:
            print("La clave que has colocado es incorrecta")
        
    def establecer_clave(self, clave_nueva, clave):
        if self.verificar_clave(clave):
            self.__clave = clave_nueva
        else:
            print("La clave que has colocado es incorrecta")
            
    def establecer_cantidad(self, cantidad_nueva, clave):
        if self.verificar_clave(clave):
            self.__cantidad = cantidad_nueva
        else:
            print("La clave que has colocado es incorrecta")
        
caja = CajaFuerte("123", 1000)

print(caja.obtener_cantidad("123"))
