import re #se encarga de imprimir el re.match para agregar caracteres especiales
from datetime import datetime  # Importar al inicio

def generar_hoja_de_vida(usuario, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("========== HOJA DE VIDA ==========\n\n")

        # DATOS PERSONALES
        dp = usuario["datosPersonales"]
        archivo.write(">> DATOS PERSONALES\n")
        archivo.write(f"Nombre: {dp['nombre']}\n")
        archivo.write(f"Número de Identificación: {dp['identificadores'][0]}\n")
        archivo.write(f"Fecha de Nacimiento: {dp['identificadores'][1]}\n")
        archivo.write(f"Celular: {dp['contacto']}\n")
        archivo.write(f"Dirección: {dp['dirección']}\n")
        archivo.write(f"Correo Electrónico: {dp['correo']}\n\n")

        # FORMACIÓN ACADÉMICA
        archivo.write(">> FORMACIÓN ACADÉMICA\n")
        for fa in usuario["formacionAcademica"]:
            archivo.write(f"- Universidad: {fa['Universidad']}\n")
            archivo.write(f"  Título: {fa['Titulo']}\n")
            archivo.write(f"  Año de Graduación: {fa['añoGraduación']}\n")
        archivo.write("\n")

        # EXPERIENCIA PROFESIONAL
        archivo.write(">> EXPERIENCIA PROFESIONAL\n")
        if usuario["experienciaProfesional"]:
            for exp in usuario["experienciaProfesional"]:
                archivo.write(f"- Empresa: {exp['Empresa']}\n")
                archivo.write(f"  Cargo: {exp['Cargo']}\n")
                archivo.write(f"  Duración: {exp['Duración']}\n")
        else:
            archivo.write("Sin experiencia laboral registrada.\n")
        archivo.write("\n")

        # REFERENCIAS PERSONALES
        archivo.write(">> REFERENCIAS PERSONALES\n")
        for ref in usuario["referenciasPersonales"]:
            archivo.write(f"- Nombre: {ref['nombre']}\n")
            archivo.write(f"  Relación: {ref['relación']}\n")
            archivo.write(f"  Teléfono: {ref['telefono']}\n")
        archivo.write("\n")

        # HABILIDADES ADICIONALES
        archivo.write(">> HABILIDADES ADICIONALES\n")
        if usuario["habilidadesAdicionales"]:
            for hab in usuario["habilidadesAdicionales"]:
                archivo.write(f"- {hab}\n")
        else:
            archivo.write("Sin habilidades adicionales registradas.\n")
        archivo.write("\n")

        archivo.write("==================================\n")


usuarios = {
    "1" : {
            "datosPersonales" : {
                "nombre":"J", 
                "identificadores":("1000456789","12/88/2005"),
                "contacto": "31359450559",
                "dirección": "Cra12 #34 A 45",
                "correo": "miguelarias@gmial.com",},
            
            "formacionAcademica" : [{"Universidad": "ECCI","Titulo":"Profesional lenguas modernas", "añoGraduación": "2024"}],
            
            "experienciaProfesional" : [{"Empresa":"Teleperformance", "Cargo":"Asesor Bilingüe", "Duración": "10 meses"}, {"Empresa":"Concentrix", "Cargo":"Asesor Bilingüe", "Duración": "4 meses"}],
            "referenciasPersonales": [{"nombre":"miguel angel arias marin II", "relación": "vecino", "telefono": "3205118016"}],
            "habilidadesAdicionales": ["HTML","CSS","Python","Inglés B2", "Diploma Pedagogía"]
    }
}
serial = len(usuarios)

def datosPersonalesDict(nombre,identificacion,fecha,contacto,direccion,correo):
    lista=[identificacion,fecha]
    tupla=tuple(lista)
    diccionario={"nombre":nombre,"identificadores":tupla,"contacto":contacto,"dirección":direccion,"correo":correo}
    return diccionario
    
def formaciónDict(universidad,titulo,año):
    diccionario={"Universidad":universidad,"Titulo":titulo, "añoGraduación":año}
    return diccionario
def referenciasDict(nombre,relación,telefono):
    diccionario={"nombre":nombre,"relación":relación, "telefono":telefono}
    return diccionario

añadir=True
while añadir:
    serial += 1
    usuarios[str(serial)] = {}
    listaFormaciones=[]
    listaReferencias=[]
    experiencias = []
    habilidades = []

    #DatosPersonales
    datosPersonales= print("A continuacion se le pediran sus datos personales")
    while True:
        nombre=input("Ingresa tu nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Ingresa un nombre valido.")
    while True:
        identificacion=input("Agrega tu numero de identidad: ")
        if identificacion.isdigit() and 8<= len(identificacion) <= 10 :
            break
        else:
            print("La identificacion no es válida: ")
    while True:    
        fecha_nacimiento=input("Ingresa tu fecha de nacimiento (DD/MM/AA): ")
        try:
            fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            hoy = datetime.now()
            if fecha >= hoy:
                print("La fecha no puede ser el dia actual")
            else:
                print("Fecha válida:", fecha.strftime("%d/%m/%Y"))
            break
        except ValueError:
            print("Error: Formato de fecha inválido. Usa DD/MM/YYYY (ej: 15/05/2000).")
    while True:
        celular_numero=input("Ingresa tu numero de celular: ")
        if celular_numero.isdigit() and len(celular_numero) == 10:
            break
        else:
            print("El numero de celular no es válido")
    while True:
        direccion=input("Ingresa la direccion de tu vivienda: ")
        if re.match(r'^[a-zA-Z0-9\sáéíóúñÁÉÍÓÚÑ#\-/.,()]+$', direccion):
            if len(direccion) >=5:
                print("Direccion valida ")
                break
            else:
                print("La direccion debe de contener al menos 5 caracteres (Debe ser real)")
        else:
            print("Error: La dirección solo puede contener letras, números, espacios, #, -, /, ., ,, () y acentos.")
    while True:
        correo_elect=input("Ingresa tu correo electronico:")
        if  re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_elect):
            if len(correo_elect) <=100:
                    print("El correo ha sido agregado")
                    break
            else:
                print("El correo debe tener minimo 100 caracteres")
        else:
            print("El correo debe de tener los siguientes caracteres(ej. ejemplo@dominio.com)")
    datosPersonales = datosPersonalesDict(nombre,identificacion,fecha_nacimiento,celular_numero,direccion,correo_elect)   

    #formacion académica:
    print("A continuacion se le pediran su información académica")
    while True:
        while True: 
            universidad = input("Ingresa el nombre de la universidad: ")
            if universidad.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            titulo = input("Ingresa el nombre del título: ")
            if titulo.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            año = input("Ingresa el año de graduación: ")
            if año.isdigit(): 
                break
            else:
                print("Ingresa un año válido")
                                
        formacion = formaciónDict(universidad,titulo,año)
        listaFormaciones.append(formacion)
        while True: 
            reset = input("¿Quieres añadir más formación profesional? 1.Si/2.No: ")
            if reset.isdigit()==False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break               

    #Experiencias
    print("A continuacion se le pedirá su experiencia laboral")
    experiencia = input("¿Tienes experiencia laboral? 1.Si/2.No: ")
    while True:
        
        if experiencia == "1":
            while True:
                Empresa = input("Empresa donde trabajo: ")
                if  Empresa.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese un nombre valido\n")
            while True:
                    cargo = input("¿Que cargo ejercias?: ")
                    if  cargo.replace(" ", "").isalpha():
                        break
                    else:
                        print("Ingrese un nombre valido\n")
            while True:
                    duracion = input("¿Tiempo de duracion (cantidad de meses)?: ")
                    if  duracion.isdigit():
                        break
                    else:
                        print("Ingrese un nombre valido\n")
                        
            informacion = {"Empresa":Empresa, "Cargo":cargo, "Duración": duracion}
            
            experiencias.append(informacion)            
            salir = input("¿Quieres ingresar mas expreciencias laborales? (si/no): ")
            if salir == "2":
                break
        else:
            print("a bueno")
            break

    #referenciasPersonales
    print("A continuacion se le pedirán sus referencias personales")
    while True:
        while True: 
            nombreRef = input("Ingresa el nombre de tu referencia : ")
            if nombreRef.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un nombre válido")
        while True: 
            relacion = input("Ingresa tu relación con esta persona: ")
            if relacion.replace(" ", "").isalpha(): 
                break
            else:
                print("Ingresa un dato válido")
        while True: 
            telefonoRef = input("Ingresa el teléfono de tu referencia: ")
            if telefonoRef.isdigit() and len(telefonoRef) == 10: 
                break
            else:
                print("Ingresa un teléfono válido")
                                
        referencias = referenciasDict(nombreRef,relacion,telefonoRef)
        listaReferencias.append(referencias)
        while True: 
            reset = input("¿Quieres añadir más referencias 1.Si/2.No: ")
            if reset.isdigit()==False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break
            
    #Habilidades adicionales
    habilidadesAdicionales = input("¿Tienes habilidades adicionales? 1.Si/2.No: ")
    while True: 
        if habilidadesAdicionales == "1":
            while True:
                habilidad = input("Digite una habilidad: ")
                if  habilidad.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese texto valido valido\n")
                                
            habilidades.append(habilidad)            
            salir = input("¿Quieres ingresar otra habilidad? 1.Si/2.No: ")
            if salir == "2":
                break
        else:
            break
            
    usuarios[str(serial)]["datosPersonales"] = datosPersonales
    usuarios[str(serial)]["formacionAcademica"] = listaFormaciones
    usuarios[str(serial)]["experienciaProfesional"] = experiencias
    usuarios[str(serial)]["referenciasPersonales"] = listaReferencias
    usuarios[str(serial)]["habilidadesAdicionales"] = habilidades
    
    generar_hoja_de_vida(usuarios,"miguel.txt")
    
    
    salir = input("¿Quieres añadir otro usuario? 1.Si/2.No: ")
    if salir == "2":
        añadir=False
    
print(usuarios)


    
    
