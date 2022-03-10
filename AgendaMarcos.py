#Este programa añade y modifica nombres y números de teléfono a un diccionario
def agregarModificar_MSanchez(nombre, agenda):
    #Busca el contacto en la agenda
    if nombre in agenda:
        print(nombre, "ya existe")
        letra = str(input("Pulsa N para ver su número de teléfono: "))
        if letra == ("n"):
            print("Su número es ",agenda[nombre])
        #Modifica el número en la agenda
        opcion = str(input("Para modificar pulsa la tecla M: "))
        if opcion == ("m"):
            numero = int(input("Escribe el nuevo número de teléfono: "))
            agenda[nombre]=numero

# Autor: Marcos Sánchez Jiménez
# Creación: 1/03/2022 11:00