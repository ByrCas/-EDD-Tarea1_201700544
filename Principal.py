
from ListaEnlazadaEDD import Lista_Enlazada

print("ESTRUCTURA DE DATOS B")
print("\nBYRON GERARDO CASTILLO GÓMEZ 201700544")

lista_principal = Lista_Enlazada()

def mostrar_menu():
    print("\nMENÚ DE OPERACIONES DE LISTA:")
    print("1.Agregar.")
    print("2.Modificar.")
    print("3.Listar/Imprimir.")
    print("4.Eliminar.")
    print("5.Salir.")

def delimitar_encabezador():
    lista_principal.modificar_por_posicion(0, None)
    lista_principal.contador = lista_principal.contador - 1
    print("Dato eliminado")


while True:
    mostrar_menu()
    opcion = input("Elija una opción del menú:")
    try:
     seleccion = int(opcion)
     if seleccion <= 0 or seleccion > 5:
         print("La opción elegida no se encuentra dentro de las opciones establecidas.")
     elif seleccion == 1:
         try:
             dato_nodo = input("Escriba el dato a agregar: ")
             lista_principal.agregar_Elemento(dato_nodo)
             print("Dato Agregado")
         except ValueError as errorDato:
             print(errorDato)
     elif seleccion == 2:
            dato_de_cambio = input("Ingrese el nuevo dato: ")
            try:
                posicion_de_cambio = int(input("Ingrese la posicion donde desee el cambio:"))
                if (lista_principal.contar_actuales()) == 0:
                    print("No es posible modificar, debido a que la lista esta vacía.")
                elif posicion_de_cambio >=0 and posicion_de_cambio <(lista_principal.contar_actuales()):
                    lista_principal.modificar_por_posicion(posicion_de_cambio, dato_de_cambio)
                    print("Dato modificado")
                else:
                    print("la posición indicada no existe dentro de la lista")
            except ValueError as errorPos:
                print("la posición ingresada no es válida")
     elif seleccion == 3:
         lista_principal.imprimir_Actuales()
         print("Elementos actuales: " + str(lista_principal.contar_actuales()))
     elif seleccion == 4:
         try:
             posicion_eliminar = int(input("Ingrese la posicion donde desea eliminar:"))
             if (lista_principal.contar_actuales()) == 0:
                 print("No es posible eliminar, debido a que la lista esta vacía.")
             elif (lista_principal.contar_actuales()) == 1 and posicion_eliminar == 0:
                 delimitar_encabezador()
             elif posicion_eliminar >= 0 and posicion_eliminar <(lista_principal.contar_actuales()):
                 lista_principal.eliminar_por_posicion(posicion_eliminar)
                 print("Dato eliminado")
             else:
                 print("la posición indicada no existe dentro de la lista")
         except ValueError as errorPosElim:
             print("la posición ingresada no es válida")
     else:
         print("EJECUCIÓN FINALIZADA")
         break
    except ValueError as errorOpcion:
        print("El dato ingresado no es válido dentro del menú.")












