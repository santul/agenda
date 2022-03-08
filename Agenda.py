#Muestra menú
#Comprueba si el usuario ha introducido un número del 1 al 5
#Al pulsar 1:
#Pregunta un nombre, si el nombre no está lo añade y si el nombre ya está te da la opción de modificarlo.
#Una vez añadido o modificado el nommbre vuelve a preguntarte un nombre.

diccionario = {}
def mostrarmenu():
    print("|_______________________|")
    print("|         Menú          |")
    print("|_______________________|")
    print("|  1. Añadir/modificar  |")
    print("|  2. Buscar            |")
    print("|  3. Borrar            |")
    print("|  4. Listar            |")
    print("|  5. Salir             |")
    print("|_______________________|")

def agregarModificar_MSanchez():
    nombre = str(input("Escribe el nombre del contacto:"))
    if nombre in diccionario:
        print(nombre, "ya existe")
        letra = str(input("Pulsa N para ver su número de teléfono: "))
        if letra == ("n"):
            print("Su número es ",diccionario[nombre])
        opcion = str(input("Para modificar pulsa la tecla M: "))
        if opcion == ("m"):
            numero = int(input("Escribe el nuevo número de teléfono: "))
            diccionario[nombre]=numero
    else:
        numero = int(input("Escribe el número de teléfono: "))
        diccionario[nombre]=numero
mostrarmenu()
opcion = int(input("¿Qué quieres hacer? (1 - 5): "))

while opcion < 1 or opcion > 5:
    print("El número es incorrecto")
    opcion = int(input("¿Qué quieres hacer? (1 - 5): "))

while opcion == 1:
    agregarModificar_MSanchez()