def gestionar_contactos():
    contactos = {}

    while True:
        print("\nBienvenido a la gestión de contactos.")
        print("Opciones:")
        print("1. Agregar un contacto.")
        print("2. Buscar un contacto.")
        print("3. Mostrar todos los contactos.")
        print("4. Actualizar número de teléfono.")
        print("5. Eliminar un contacto.")
        print("6. Salir.")
        
        opcion = input("Ingresa tu opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del contacto: ")
            numero = input("Ingresa el número de teléfono: ")
            contactos[nombre] = numero
            print("\nEl contacto ha sido agregado correctamente.")
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre del contacto: ")
            if nombre in contactos:
                print(f"\nEl número de teléfono de {nombre} es: {contactos[nombre]}")
            else:
                print("\nContacto no encontrado.")
        
        elif opcion == "3":
            print("\nContactos:")
            for nombre, numero in contactos.items():
                print(f"- {nombre}: {numero}")
        
        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto a actualizar: ")
            if nombre in contactos:
                nuevo_numero = input("Ingresa el nuevo número de teléfono: ")
                contactos[nombre] = nuevo_numero
                print("\nEl número de teléfono ha sido actualizado correctamente.")
            else:
                print("\nContacto no encontrado.")
        
        elif opcion == "5":
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print("\nEl contacto ha sido eliminado correctamente.")
            else:
                print("\nContacto no encontrado.")
        
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

gestionar_contactos()