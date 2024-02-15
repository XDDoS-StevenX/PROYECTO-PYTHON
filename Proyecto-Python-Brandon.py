#Proyecto-Campus

#1 PASO:

campers = []


def añadir_camper(nombre, priority=5):
    if any(camper['nombre'] == nombre for camper in campers):
        print("Error: El camper ya existe.")
        return
    nuevo_camper = {'nombre': nombre, 'priority': priority}
    campers.append(nuevo_camper)
    print(f"Camper '{nombre}' añadid@ correctamente.")


def mostrar_campers():
    if not campers:
        print("No hay tareas pendientes.")
    else:
        print("Tareas Pendientes:")
        for task in sorted(campers, key=lambda x: x['riesgo'], reverse=True):
            print(f"{campers['nombre']} - Prioridad: {campers['riesgo']}")


def remover_camper(name):
    for camper in mostrar_campers[:]:
        if camper['name'] == name:
            mostrar_campers.remove(camper)
            print(f"Tarea '{name}' eliminada correctamente.")
            return
    print("Error: La tarea no se encontró.")


while True:
    
    print("\n ▁ ▂ ▄ ▅ ▆ ▇ █ MENU PRINCIPAL █ ▇ ▆ ▅ ▄ ▂ ▁")
    print("1. ➕ Añadir un/a nuev@ camper. ")
    print("2. 📊 Mostrar los datos de un camper registrado. ")
    print("3. ❌ Eliminar un camper. ")
    print("4. 🚪 Salir. ")
    
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠛⢻⣿⣿⣿⣿⠿⠛⡿⠀⠀⠀⠀⠀⠀⢿⠛⠿⣟⣻⡿⠛⠻⣿⣿⣿⣿")
    print("⣿⣿⣿⡆⣾⣿⣿⠟⠁⠀⣀⣇⣀⣠⣤⣤⣄⣀⣸⣀⠀⠈⠻⣧⣀⣀⣿⣿⣿⣿")
    print("⣿⣿⣿⡇⣿⣿⠋⢀⣾⠟⠉⢉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⣿⣉⢿⣿⣿⣿")
    print("⣿⣿⣿⡿⣿⠇⢠⣿⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠸⣿⢿⣿⣿⣿")          
    print("⣿⣿⠇⢰⡟⠀⣾⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⡆⠸⣿⣿") 
    print("⣿⣿⠀⢸⡇⢰⣿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⡇⠀⣿⣿")        
    print("⣿⣧⡀⢸⡇⠘⣿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⡇⢀⣼⣿")  
    print("⣿⣿⣿⣾⣇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣸⣷⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣠⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣦⡀⠈⠛⠿⠿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠁⢀⣴⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡃⠈⠛⠷⣦⣤⣀⣀⣀⠀⠀⣀⣀⣀⣤⣴⠾⠛⠁⢘⣿⣿⣿⣿⣿")
    print("⣿⣿⠟⠋⠈⠙⠷⣦⣤⣀⡈⠉⢹⡟⠛⠛⢻⡏⠉⢁⣀⣤⣴⠾⠋⠁⠙⠻⣿⣿")
    print("⣿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠷⠶⠶⠾⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿")
    print("⣿⣤⣤⣼⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣧⣤⣤⣿")
    print("█▀▀ ▄▀█ █▀▄▀█ █▀█ █░█ █▀ █░░ ▄▀█ █▄░█ █▀▄ █▀")
    print("█▄▄ █▀█ █░▀░█ █▀▀ █▄█ ▄█ █▄▄ █▀█ █░▀█ █▄▀ ▄█")

    
    option = input("Seleccione una opción❗ (1-4): ")


    if option == '1':
        import json
        
        camper = {}
        camper["N° Identificacion"] = float(input("Ingrese el numero de identificacion: "))
        camper["Nombres"] = input("Ingrese el nombre del camper: ")
        camper["Direccion"]= input("Ingrese la direccion del camper: ")
        camper["Acudiente"] = input("Ingrese el teléfono del cliente: ")
        camper["Telefonos de contacto"] = input("Ingrese el numero del camper: ")
        camper["Numero fijo"] = input("Ingrese el numero fijo")
        camper["Estado"] = input("Ingrese el estado del camper:" )
        camper["Riesgo"] = input("Defina el riesgo del camper:" "")
        camper["Ruta"] = input("Establezca la ruta del camper:")
    
        file_name = "Camper.json"

        with open(file_name, "w") as json_file:
         json.dump(camper, json_file, indent=4)
        
        print(f"Has añadido un nuevo camper en '{file_name}'. ")

    elif option == '2':
        print("Inserte el camper que desearia ver")

        



    elif option == '3':
        camper_nombre = input("Ingrese el nombre del camper a eliminar: ")
        remover_camper(camper_nombre)


    elif option == '4':
        print("📤 𝙎𝙖𝙡𝙞𝙚𝙣𝙙𝙤 𝙙𝙚𝙡 𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙖, 𝙃𝙖𝙨𝙩𝙖 𝙡𝙪𝙚𝙜𝙤! !")
        break


    else:
        print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 4.") 