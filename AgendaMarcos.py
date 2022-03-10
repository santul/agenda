def agregarModificar_MSanchez():
    nombre = str(input("Escribe el nombre del contacto:"))
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

# Modificaficón:10/02/2022 8:58