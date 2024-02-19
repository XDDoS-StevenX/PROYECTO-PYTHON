#Proyecto-Campus

class Camper:
    def __init__(self, id, nombres, apellidos, direccion, acudiente, telefono_celular, telefono_fijo, estado, riesgo, ruta_asignada=None):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.telefono_celular = telefono_celular
        self.telefono_fijo = telefono_fijo
        self.estado = estado
        self.riesgo = riesgo
        self.ruta_asignada = ruta_asignada

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def asignar_ruta(self, nueva_ruta):
        self.ruta_asignada = nueva_ruta

class Trainer:
    def __init__(self, nombre, especialidad, horario):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario

    def asignar_ruta(self, ruta):
        # Implementar lógica para asignar ruta al Trainer
        pass

class Ruta:
    def __init__(self, nombre, capacidad, entrenador_asignado=None):
        self.nombre = nombre
        self.capacidad = capacidad
        self.entrenador_asignado = entrenador_asignado
        self.campers_asignados = []

    def asignar_entrenador(self, entrenador):
        self.entrenador_asignado = entrenador

    def agregar_camper(self, camper):
        self.campers_asignados.append(camper)

    def verificar_capacidad(self):
        if len(self.campers_asignados) < self.capacidad:
            return True
        else:
            return False

class Modulo:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

class Coordinador:
    def matricular_camper(self, camper, ruta, entrenador, fecha_inicio, fecha_finalizacion, salon_entrenamiento):
        camper.asignar_ruta(ruta)
        ruta.agregar_camper(camper)
        ruta.asignar_entrenador(entrenador)
        

    def registrar_notas(self, camper, modulo, nota_teorica, nota_practica):
        # Implementar lógica para registrar notas
        pass

    def generar_reportes(self):
        # Implementar lógica para generar reportes
        pass

#Cree instancias de clases para pruebas
camper_1 = Camper("5553228779", "Andres", "Galan", "Carrera 12 #154-24", "Adam Noruega", "7788246513", "1324456243", "Inscrito", "Ninguno")
trainer_1 = Trainer("Juan Perez", "NodeJS", "Lunes y Miércoles")
ruta_1 = Ruta("Ruta NodeJS", 33)
modulo_1 = Modulo("Fundamentos de programación", "Introducción a la algoritmia, PSeInt y Python")
coordinador = Coordinador()

# Matricular camper en una ruta
coordinador.matricular_camper(camper_1, ruta_1, trainer_1, "2024-02-01", "2024-05-01", "Salón A")

# Cambiar estado de un camper
camper_1.cambiar_estado("Cursando")

# Asignar notas a un camper en un módulo
coordinador.registrar_notas(camper_1, modulo_1, 70, 80)

# Generar reportes
coordinador.generar_reportes()


while True:
    
    print("\n ▁ ▂ ▄ ▅ ▆ ▇ █ MENU PRINCIPAL █ ▇ ▆ ▅ ▄ ▂ ▁")
    print("1. ➕ Añadir un/a nuev@ camper. ")
    print("2. 📊 Mostrar los datos de un camper registrado. ")
    print("3. ❌ Eliminar un camper. ")
    print("4")
    print("0. 🚪 Salir. ")
    
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
        camper["Numero de Identificacion"] = float(input("Ingrese el numero de identificacion:  "))
        camper["Nombres"] = input("Ingrese el nombre del camper:  ")
        camper["Direccion"]= input("Ingrese la direccion del camper:  ")
        camper["Acudiente"] = input("Ingrese el teléfono del cliente:  ")
        camper["Telefonos de contacto"] = input("Ingrese el numero del camper:  ")
        camper["Numero fijo"] = input("Ingrese el numero fijo:  ")
        camper["Estado"] = input("Ingrese el estado del camper:  " )
        camper["Riesgo"] = input("Defina el riesgo del camper:  " )
        camper["Ruta"] = input("Establezca la ruta del camper:  ")
    
        file_name = "Camper.json"

        with open(file_name, "w") as json_file:
         json.dump(camper, json_file, indent=4)
        
        print(f"Has añadido un nuevo camper en '{file_name}'. ")

    elif option == '2':
        print("Inserte el camper que desearia ver")

        



    elif option == '3':
        camper_nombre = input("Ingrese el nombre del camper a eliminar: ")
        remover_camper(camper_nombre)


    elif option == '0':
        print("📤 𝙎𝙖𝙡𝙞𝙚𝙣𝙙𝙤 𝙙𝙚𝙡 𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙖, 𝙃𝙖𝙨𝙩𝙖 𝙡𝙪𝙚𝙜𝙤! !")
        break


    else:
        print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 4.") 