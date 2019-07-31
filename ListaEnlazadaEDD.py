# BYRON GERARDO CASTILLO GÓMEZ 201700544
from NodoListaEDD import Nodo_Lista

class Lista_Enlazada:

    encabezador = Nodo_Lista(None, None)
    contador = 0

    def agregar_Elemento(self, paramDato):
        nuevo_dato = Nodo_Lista(paramDato, None)
        if self.encabezador.obtener_Dato() == None:
            self.encabezador = nuevo_dato
            self.contador = self.contador + 1
        else:
            momentaneo = self.encabezador
            for indice in range(0, self.contador-1):
                momentaneo = momentaneo.obtener_Siguiente()
            momentaneo.asignar_Siguiente(nuevo_dato)
            self.contador = self.contador + 1


    def imprimir_Actuales(self):
         recorredor = self.encabezador
         print("**INICIO LISTA**")
         for recorrido in range(0, self.contador):
             print("- - - -")
             print("  " + str(recorredor.obtener_Dato()))
             print("- - - -")
             print("   | \n   _")
             print("   V")
             recorredor = recorredor.obtener_Siguiente()
         print("**FIN LISTA**")

    def contar_actuales(self):
        return self.contador

    def modificar_por_posicion(self, posicion, dato_modificado):
        modificador_p = self.encabezador
        for recorrido in range(0, posicion):
            modificador_p = modificador_p.obtener_Siguiente()
        modificador_p.modificar_Dato(dato_modificado)

    def eliminar_por_posicion(self, posicion):
        if posicion == 0:
            antiguo_encabezador = self.encabezador
            self.encabezador = antiguo_encabezador.obtener_Siguiente()
            antiguo_encabezador.modificar_Dato(None)
            antiguo_encabezador.asignar_Siguiente(None)
            self.contador = self.contador - 1
        else:
            anterior_p = self.encabezador
            for recorrido in range(0, posicion - 1):
               anterior_p = anterior_p.obtener_Siguiente()
            eliminador_p = anterior_p.obtener_Siguiente()
            posterior_p = eliminador_p.obtener_Siguiente()
            eliminador_p.modificar_Dato(None)
            eliminador_p.asignar_Siguiente(None)
            anterior_p.asignar_Siguiente(posterior_p)
            self.contador = self.contador - 1

