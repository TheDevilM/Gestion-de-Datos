def gestionar_inventario():
    inventario = {}

    while True:
        print("\nBienvenido al sistema de inventario de la tienda.")
        print("Opciones:")
        print("1. Agregar un producto al inventario")
        print("2. Vender un producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            producto = input("Ingresa el nombre del producto: ")
            cantidad = int(input(f"Ingresa la cantidad de {producto}: "))
            if producto in inventario:
                inventario[producto] += cantidad
            else:
                inventario[producto] = cantidad
            print("\nProducto agregado al inventario.")
        
        elif opcion == "2":
            producto = input("Ingresa el nombre del producto a vender: ")
            if producto in inventario:
                cantidad = int(input(f"Ingresa la cantidad a vender de {producto}: "))
                if cantidad <= inventario[producto]:
                    inventario[producto] -= cantidad
                    if inventario[producto] == 0:
                        del inventario[producto]
                    print("\nVenta realizada.")
                else:
                    print("\nNo hay suficiente stock.")
            else:
                print("\nProducto no encontrado en el inventario.")
        
        elif opcion == "3":
            print("\nInventario:")
            for producto, cantidad in inventario.items():
                print(f"- {producto}: {cantidad}")
        
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

gestionar_inventario()
