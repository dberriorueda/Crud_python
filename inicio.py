motos = []

def crear_marca(marca,modelo):
    motos.append((marca,modelo))
    print(f"Marca de moto '{marca}'  modelo '{modelo}' agredada al inventario")

def buscar_marca(marca):

    resultado = [modelo for m, modelo in motos if m == marca]
    if resultado:
        print(f"Modelos de motos para la marca '{marca}' : {','.join(resultado) }")
    else:
        print(f"La marca '{marca}' no fue encontrada.")

def modificar_marca(marca, nuevo_modelo):

    for i, (m, modelo) in enumerate(motos):
        if m == marca:
            motos[i]= (m, nuevo_modelo) 
            print(f"Modelo de la marca '{marca}' ha sido modificado a '{nuevo_modelo}'")
            return
    print(f"La marca '{marca}' no fue encontrada.")  

def eliminar_marca(marca):

    eliminadas = [m for m, modelo in motos if m == marca]
    if eliminadas:
        motos[:] = [(m, modelo) for m, modelo in motos if m != marca]
        print(f"Se han elimindo todas las marcas de '{marca}'")
    else:
        print(f"La marca '{marca} no se encuentra.'")

def mostrar_marcas():
    for marca, modelo in motos:
        print(f"Marca: {marca}, modelo: {modelo}") 

def main():
    while True:
        print("\nopciones:")
        print("1. Agregar marca de moto")
        print("2. Buscar marca de moto")
        print("3. Modificar marca de moto") 
        print("4. Eliminar marca de moto") 
        print("5. Mostrar todas las  marcas de moto")   
        print("6. Salir")    

        opcion = input("Ingrese la opcion deseada: ") 

        if opcion == "1":
            marca = input("Ingrese la marca de la moto: ") 
            modelo = input("Ingrese el modelo de la moto ") 
            crear_marca(marca,modelo)   
        elif opcion == "2":
            marca = input("Ingrese la marca de la moto que desea buscar: ")
            buscar_marca(marca)

        elif opcion == "3":
            marca = input("Ingrese la marca de la moto que desea modificar: ")
            nuevo_modelo = input("Ingrese el modelo de la moto:")
            marca = input("Ingrese la nueva marca a modificar:")
            nuevo_modelo = input("Ingrese el nuevo modelo: ")
            modificar_marca(marca,nuevo_modelo)  

        elif opcion == "4":
            marca = input("Ingrese la marca de la moto que desea eliminar: ")
            eliminar_marca(marca)
        elif opcion == "5":
            mostrar_marcas()
        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
if __name__ == "__main__":
    main()            