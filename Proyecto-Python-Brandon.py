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
    
    print("\n ˜”*°•.˜”*°• ▁ ▂ ▄ ▅ ▆ ▇ █ MENU PRINCIPAL █ ▇ ▆ ▅ ▄ ▂ ▁ •°*”˜.•°*”˜")
    print("1. ᴀñᴀᴅɪʀ ᴜɴ/ᴀ ɴᴜᴇᴠᴏ/ᴀ ᴄᴀᴍᴘᴇʀ.")
    print("2. (っ◔◡◔)っ Mostrar todos los campers.")
    print("3. 𝔼𝕝𝕚𝕞𝕚𝕟𝕒𝕣 un 𝕔𝕒𝕞𝕡𝕖𝕣.")
    print("4. Salir.")
    
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⠛⢻⣿⣿⣿⣿⠿⠛⡿⠀⠀⠀⠀⠀⠀⢿⠛⠿⣟⣻⡿⠛⠻⣿⣿⣿⣿")
    print("⣿⣿⣿⡆⣾⣿⣿⠟⠁⠀⣀⣇⣀⣠⣤⣤⣄⣀⣸⣀⠀⠈⠻⣧⣀⣀⣿⣿⣿⣿")
    print("⣿⣿⣿⡇⣿⣿⠋⢀⣾⠟⠉⢉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⣿⣉⢿⣿⣿⣿")
    print("⣿⣿⣿⡿⣿⠇⢠⣿⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠸⣿⢿⣿⣿⣿")          
    print("⣿⣿⠇⢰⡟⠀⣾⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⡆⠸⣿⣿") 
    print("⣿⣿⠀⢸⡇⢰⣿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⡇⠀⣿⣿")        
    print("⣿⣧⡀⢸⡇⠘⣿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⡇⢀⣼⣿          ✈ 𓆙𓆙")     
    print("⣿⣿⣿⣾⣇⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣸⣷⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣠⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣦⡀⠈⠛⠿⠿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠁⢀⣴⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⡃⠈⠛⠷⣦⣤⣀⣀⣀⠀⠀⣀⣀⣀⣤⣴⠾⠛⠁⢘⣿⣿⣿⣿⣿")
    print("⣿⣿⠟⠋⠈⠙⠷⣦⣤⣀⡈⠉⢹⡟⠛⠛⢻⡏⠉⢁⣀⣤⣴⠾⠋⠁⠙⠻⣿⣿")
    print("⣿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠷⠶⠶⠾⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿")
    print("⣿⣤⣤⣼⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣧⣤⣤⣿")
    print("█▀▀ ▄▀█ █▀▄▀█ █▀█ █░█ █▀ █░░ ▄▀█ █▄░█ █▀▄ █▀")
    print("█▄▄ █▀█ █░▀░█ █▀▀ █▄█ ▄█ █▄▄ █▀█ █░▀█ █▄▀ ▄█")

    
    option = input("Seleccione una opción (1-4): ")


    if option == '1':
        camper_nombre = input("Ingrese el nombre del camper: ")
        try:
            camper_prioridad = int(input("Ingrese la prioridad de la tarea (por defecto es 5): "))
        except ValueError:
            print("Error: El riesgo debe ser neutro o condicinal. Se utilizará el riesgo por defecto.")
            task_priority = 5
        añadir_camper(camper_nombre, camper_prioridad)


    elif option == '2':
        mostrar_campers()


    elif option == '3':
        camper_nombre = input("Ingrese el nombre de la tarea a eliminar: ")
        remover_camper(camper_nombre)


    elif option == '4':
        print("🅴🆂🆃🅰🆂 🆂🅰🅻🅸🅴🅽🅳🅾 🅳🅴🅻 🅿🆁🅾🅶🆁🅰🅼🅰, 🅷🅰🆂🆃🅰 🅻🆄🅴🅶🅾!")
        break


    else:
        print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 4.") 