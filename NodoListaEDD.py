# BYRON GERARDO CASTILLO GÓMEZ 201700544
class Nodo_Lista:

    dato_EDD = None
    siguiente_EDD = None

    def __init__(self, dato, siguiente):
        self.dato_EDD = dato
        self.siguiente_EDD = siguiente

    def obtener_Dato(self):
        return self.dato_EDD

    def obtener_Siguiente(self):
        return self.siguiente_EDD

    def asignar_Siguiente(self, paramSiguiente):
        self.siguiente_EDD = paramSiguiente

    def modificar_Dato(self, paramNuevoDato):
        self.dato_EDD = paramNuevoDato



