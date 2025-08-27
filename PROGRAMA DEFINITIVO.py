import time
import random
import string
import os
from datetime import datetime
import calendar
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
print("PROGRAMA DEFINITIVO")
print("1. Calculador de Color de Bola de Collar de Colores(TM). Marca Registrada CCBCC")
print("2. Simulador de ATM")
print("3. Calculador de edad de la familia DS")
print("4. Generador de Contraseñas")
print("5. Simulador de Impresora")
print("6. Calculadora Básica")
print("7. Generador de Fechas de nacimiento y su edad")
print("8. Encontrador de Múltiplos")
print("9. Errores HTTP")
print("10. Calculador de tamaño de archivos y carpetas")
opcion = int(input("Elige herramienta: "))

if opcion == 1:
    colores = {
        "R": "Rojo",
        "A": "Amarillo"
    }
    secuencia = input("Ingresa la combinación del collar (ej: RARR): ").upper()
    numero = int(input("Ingresa el número de la bola: "))
    indice = (numero - 1) % len(secuencia)
    codigo_color = secuencia[indice]
    print(f"La bola número {numero} es de color {colores.get(codigo_color, 'Desconocido')}.")

elif opcion == 2:
    zion = 2
    saldo = int(input("¿Cuanto Saldo quieres tener al Inicio? "))
    pin = int(input("¿Que PIN quieres que tenga tu Cuenta? "))
    ndb = input("¿Qué nombre quieres que tenga el Banco? ")
    while zion == 2:
        print(f"Bienvenido a {ndb}")
        print("1. Retirar dinero")
        print("2. Meter dinero")
        print("3. Ver tu Saldo")
        print("4. Pedir un Prestamo")
        print("5. Obtener Dinero Gratis")
        print("6. Salir")
        accion = int(input("¿Que Quieres Hacer? "))
        if accion == 1:
            pin2 = int(input("Primero, Proporciona tu PIN/NIP: "))
            retirar = int(input("¿Cuando Quieres Retirar? "))
            if pin2 == pin:
                if retirar > saldo:
                    print("Fondos Insuficientes.")
                else:
                    print(f"Se han Retirado ${retirar} de su Cuenta.")
                    saldo -= retirar
                    print(f"Tu Saldo Actual es ${saldo}.")
            else:
                print("PIN/NIP Incorrecto.")
                
        elif accion == 2:
            # A reparar
            pin2 = int(input("Primero, Proporciona tu PIN/NIP: "))
            if pin2 == pin:
                ingresar = int(input("¿Cuanto quieres Ingresar? "))
                saldo += ingresar
                print(f"Tu Saldo Actual es ${saldo}.")
            else:
                print("PIN/NIP Incorrecto.")
        else:
            if accion > 6 and accion < 1:
                print("Opcion no Valida.")
            
        if accion == 3:
            pin2 = int(input("Primero, Proporciona tu PIN/NIP: "))
            if pin2 == pin:
                print(f"Tu Saldo Actual es ${saldo}.")
            else:
                print("PIN/NIP Incorrecto.")
                
        if accion == 4:
            pin2 = int(input("Primero, Proporciona tu PIN/NIP: "))
            if pin2 == pin:
                prestamo = int(input("¿De Cuanto quieres pedir el Prestamo? "))
                saldo += prestamo
                print("¡Pagalo a tiempo o te Matamos a tus familiares y te embargamos la casa :)!")
            else:
                 print("PIN/NIP Incorrecto.")       
        if accion == 5:
            time.sleep(1)
            print("[ERROR]: NO SE PUEDE OBTENER DINERO GRATIS")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432.")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432..")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432...")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432.")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432..")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432...")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432.")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432..")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432...")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432.")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432..")
            time.sleep(1)
            print("Mandando Misil Balistico a ATM No. 213432...")
            time.sleep(1)
            print("Nah, Mentira jajjaja :)")
            break

        if accion == 6:
            print("Adios!")
            break

elif opcion == 3:
    from datetime import datetime
    hoy = datetime.now()
    NDS_OG = datetime(2004, 11, 21)
    NDS_Lite = datetime(2006, 3, 2)
    NDSi = datetime(2008, 11, 1)
    NDSi_XL = datetime(2010, 2, 28)
    N3DS = datetime(2011, 2, 27)
    N3DS_XL = datetime(2012, 8, 19)
    N2DS = datetime(2013, 10, 12)
    New_N3DS = datetime(2015, 9, 25)
    New_N3DS_XL = datetime(2015, 2, 13)
    New_N2DS_XL = datetime(2017, 7, 28)
    FL01 = hoy.year - NDS_OG.year - ((hoy.month, hoy.day) < (NDS_OG.month, NDS_OG.day))
    FL02 = hoy.year - NDS_Lite.year - ((hoy.month, hoy.day) < (NDS_Lite.month, NDS_Lite.day))
    FL03 = hoy.year - NDSi.year - ((hoy.month, hoy.day) < (NDSi.month, NDSi.day))
    FL04 = hoy.year - NDSi_XL.year - ((hoy.month, hoy.day) < (NDSi_XL.month, NDSi_XL.day))
    FL05 = hoy.year - N3DS.year - ((hoy.month, hoy.day) < (N3DS.month, N3DS.day))
    FL06 = hoy.year - N3DS_XL.year - ((hoy.month, hoy.day) < (N3DS_XL.month, N3DS_XL.day))
    FL07 = hoy.year - N2DS.year - ((hoy.month, hoy.day) < (N2DS.month, N2DS.day))
    FL08 = hoy.year - New_N3DS.year - ((hoy.month, hoy.day) < (New_N3DS.month, New_N3DS.day))
    FL09 = hoy.year - New_N3DS_XL.year - ((hoy.month, hoy.day) < (New_N3DS_XL.month, New_N3DS_XL.day))
    FL10 = hoy.year - New_N2DS_XL.year - ((hoy.month, hoy.day) < (New_N2DS_XL.month, New_N2DS_XL.day))
    nombres = [
        "Nintendo DS Original", 
        "Nintendo DS Lite", 
        "Nintendo DSi", 
        "Nintendo DSi XL", 
        "Nintendo 3DS", 
        "Nintendo 3DS XL", 
        "Nintendo 2DS", 
        "New Nintendo 3DS", 
        "New Nintendo 3DS XL", 
        "New Nintendo 2DS XL"
    ]
    opciones = {
        "1": f"La {nombres[0]} salio el {NDS_OG.day}/{NDS_OG.month}/{NDS_OG.year} y tiene {FL01} años",
        "2": f"La {nombres[1]} salio el {NDS_Lite.day}/{NDS_Lite.month}/{NDS_Lite.year} y tiene {FL02} años",
        "3": f"La {nombres[2]} salio el {NDSi.day}/{NDSi.month}/{NDSi.year} y tiene {FL03} años",
        "4": f"La {nombres[3]} salio el {NDSi_XL.day}/{NDSi_XL.month}/{NDSi_XL.year} y tiene {FL04} años",
        "5": f"La {nombres[4]} salio el {N3DS.day}/{N3DS.month}/{N3DS.year} y tiene {FL05} años",
        "6": f"La {nombres[5]} salio el {N3DS_XL.day}/{N3DS_XL.month}/{N3DS_XL.year} y tiene {FL06} años",
        "7": f"La {nombres[6]} salio el {N2DS.day}/{N2DS.month}/{N2DS.year} y tiene {FL07} años",
        "8": f"La {nombres[7]} salio el {New_N3DS.day}/{New_N3DS.month}/{New_N3DS.year} y tiene {FL08} años",
        "9": f"La {nombres[8]} salio el {New_N3DS_XL.day}/{New_N3DS_XL.month}/{New_N3DS_XL.year} y tiene {FL09} años",
        "10": f"La {nombres[9]} salio el {New_N2DS_XL.day}/{New_N2DS_XL.month}/{New_N2DS_XL.year} y tiene {FL10} años",
        }
    #0 = "Nintendo DS Original"
    # #1 = "Nintendo DS Lite"
    # #2 = "Nintendo DSi"
    # #3 = "Nintendo DSi XL"
    # #4 = "Nintendo 3DS"
    # #5 = "Nintendo 3DS XL"
    # #6 = "Nintendo 2DS"
    # #7 = "New Nintendo 3DS"
    # #8 = "New Nintendo 3DS XL"
    # #9 = "New Nintendo 2DS XL"
    while True:
        try:
            print("1. Todos")
            print("2. A Eleccion")
            print("3. Salir")
            Modo = input("Que Modo quieres? (1/2/3):")
            
            if Modo == "1":
                print("Familia Nintendo DS:")
                print(f"La {nombres[0]} salio el {NDS_OG.day}/{NDS_OG.month}/{NDS_OG.year} y tiene {FL01} años")
                print(f"La {nombres[1]} salio el {NDS_Lite.day}/{NDS_Lite.month}/{NDS_Lite.year} y tiene {FL02} años")
                print(f"La {nombres[2]} salio el {NDSi.day}/{NDSi.month}/{NDSi.year} y tiene {FL03}")
                print(f"La {nombres[3]} salio el {NDSi_XL.day}/{NDSi_XL.month}/{NDSi_XL.year} y tiene {FL04} años")
                print("Familia Nintendo 3DS:")
                print(f"La {nombres[4]} salio el {N3DS.day}/{N3DS.month}/{N3DS.year} y tiene {FL05}")
                print(f"La {nombres[5]} salio el {N3DS_XL.day}/{N3DS_XL.month}/{N3DS_XL.year} y tiene {FL06} años")
                print(f"La {nombres[6]} salio el {N2DS.day}/{N2DS.month}/{N2DS.year} y tiene {FL07}")
                print(f"La {nombres[7]} salio el {New_N3DS.day}/{New_N3DS.month}/{New_N3DS.year} y tiene {FL08} años")
                print(f"La {nombres[8]} salio el {New_N3DS_XL.day}/{New_N3DS_XL.month}/{New_N3DS_XL.year} y tiene {FL09} años")
                print(f"La {nombres[9]} salio el {New_N2DS_XL.day}/{New_N2DS_XL.month}/{New_N2DS_XL.year} y tiene {FL10} años")
                print("               ")
                print("               ")
                print("               ")
                break
            elif Modo == "2":
                print("1. Nintendo DS Original")
                print("2. Nintendo DS Lite")
                print("3. Nintendo DSi")
                print("4. Nintendo DSi XL")
                print("5. Nintendo 3DS")
                print("6. Nintendo 3DS XL")
                print("7. Nintendo 2DS")
                print("8. New Nintendo 3DS")
                print("9. New Nintendo 3DS XL")
                print("10. New Nintendo 2DS XL")
                Nosecomollamarle = (input("Que Modelo de Nintendo DS?:"))
            if Nosecomollamarle in opciones:
                print(opciones[Nosecomollamarle])
                break
            elif Modo == "3":
                print("Adios!")
                break
        except ValueError:
            print("Modo no valido")

elif opcion == 4:

    caracteres_posibles = string.ascii_letters + string.digits + string.punctuation
    def Generate_Password(longitud):
        password = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
        return password
    longitud = int(input("Longitud de la Contraseña: "))
    password = Generate_Password(longitud)
    print("Tu Contraseña generada es:",password)

elif opcion == 5:
    print("1. Todos los cartuchos RGB")
    print("2. Todos los cartuchos CMYK")
    print("3. Ninguno")
    cartuchos = int(input("¿Que cartuchos Instalastes?: "))
    errores = {
         1: "Error General. Revise el Manual",
          2: "Papel Atascado. Desatasque el Papel y Reintente",
          3: "Falta de Color Magenta. Recargue el Cartucho/Color",
          4: "Falta de Color N/A. Recargue el Cartucho/Color",
          5: "Cartucho Falsificado Detectado. Compre Cartuchos Originales, Rata",
          6: "Componente Defectuoso o Dañado Detectado. Lleve la Impresora a un Tecnico Autorizado",
          7: "Conexion Perdida. Reconecte y Reintente",
          8: "Reparacion No Oficial Detectada. Por Favor Lleve la Impresora a un Tecnico Autorizado",
          9: "Suscripcion de HP Instant Ink no encontrada/Vencida/Invalida. Por Favor Pague la Suscripcion y Reintente"
    }
    
    os.system("cls")
    while cartuchos == 1:
        print("Bueno. Podes Imprimir en RGB")
        print("1. Si.")
        print("2. No.")
        imprimir = int(input("¿Quieres Imprimir?: "))
        if imprimir == 1:
            print("*Haciendo Ruidos que parece que va a imprimir pero solo son sonidos random*")
            tomate = 1
            while tomate <= 5:
                print("_")
                time.sleep(0.5)
                os.system("cls")
                print(" ")
                time.sleep(0.5)
                os.system("cls")
                print("_")
                time.sleep(0.5)
                os.system("cls")
                print(" ")
                time.sleep(0.5)
                os.system("cls")
                tomate += 1
                print("Empezando a Imprimir...")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [--------------------------------------------------] (0%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [--------------------------------------------------] (5%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [#-------------------------------------------------] (10%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [##------------------------------------------------] (20%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [##------------------------------------------------] (25%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [###-----------------------------------------------] (30%)")
                time.sleep(2)
                os.system("cls")
                print("Imprimiendo... [####----------------------------------------------] (40%)")
                time.sleep(2)
                os.system("cls")
                randomnumber = random.randint(1, 9)
                errorseleccionado = errores[randomnumber]
                print(errorseleccionado)
                print("1. Intentar de Nuevo")
                print("2. Cancelar")
                hela2 = int(input("¿Cual Eliges?: "))
                if hela2 == 2:
                    break

        if cartuchos == 2:
            os.system("cls")
            print("Imprimiendo... [--------------------------------------------------] (0%)")
            time.sleep(2)
            os.system("cls")
            randomnumber = random.randint(1, 9)
            errorseleccionado = errores[randomnumber]
            print(errorseleccionado)

        elif cartuchos == 3:
            print("Idiota, carga tinta o no imprimis")

        else:
            print("Codigo de Error: 010010000100010001010000")
            print("Error General. Revise el Manual")

elif opcion == 6:
    primernumero = int(input("Primer Numero: "))
    segundonumero = int(input("Segundo Numero: "))
    resultado = primernumero + segundonumero
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Multiplicacion")
    print("3. Division")
    print("4. Resta")
    
    operacion = input("Elige una operacion (1/2/3/4): ")
    
    if operacion == "1":
        resultado = primernumero + segundonumero
        operacion_str = "más"
        
    elif operacion == "2":
        resultado = primernumero * segundonumero
        operacion_str = "por"
    
    elif operacion == "3":
        resultado = primernumero / segundonumero
        operacion_str = "dividido"
        
    elif operacion == "4":
        resultado = primernumero - segundonumero
        operacion_str = "menos"

    else:
        print("Opcion no valida") 
        resultado = None
        operacion_str = ""
        
    if resultado is not None:
        print(f"{primernumero} {operacion_str} {segundonumero} es {resultado}")

elif opcion == 7:
    fecha_actual = datetime.now()
    validar_años = input("Quieres activar las restricciones para los años? (s/n)")
    
    while True:
        try:
            inicioyear = int(input("Año de inicio:"))
            finyear = int(input("Año Final:"))
        
            if validar_años == "s":
                if inicioyear > finyear:
                    print("El año de inicio no puede ser mayor que el año final. Intenta de nuevo.")
                elif finyear > fecha_actual.year:
                 print("El año final no puede ser mas que el año actual.")
                else:
                    break
            else:
                break
    
        except ValueError:
            print("Por Favor Ingresa un numero valido")

    repeticiones = int(input("Repeticiones:"))

    for i in range(repeticiones):
        month = random.randint(1, 12)
        year = random.randint(inicioyear, finyear)
        dias_en_mes = calendar.monthrange(year, month)[1]
        day = random.randint(1, dias_en_mes)
        fecha_nacimiento = datetime(year, month, day)
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        print(f"{day}/{month}/{year} y {edad} años")

elif opcion == 8:
    # Programa interactivo para comprobar múltiplos

    numero = int(input("Ingresa el número principal: "))

    # Pedimos los números a comprobar, separados por comas
    entrada = input("Ingresa los números a comprobar separados por coma (ej: 3,4,5,9): ")
    numeros_a_comprobar = [int(x.strip()) for x in entrada.split(",")]

    print(f"\nComprobando de qué números {numero} es múltiplo:\n")
    for n in numeros_a_comprobar:
        if numero % n == 0:
            print(f"{numero} es múltiplo de {n}")
        else:
            print(f"{numero} NO es múltiplo de {n}")

elif opcion == 9:
    # Función para cargar la imagen de http.cat
    def cargar_imagen():
        try:
            # Obtener el número de error HTTP
            numero_error = entry_error.get()
        
            # Validar que el número de error sea un número
            if not numero_error.isdigit():
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")
                return
        
            # Construir la URL para la imagen
            url = f"https://http.cat/{numero_error}"
        
            # Realizar la solicitud HTTP para obtener la imagen
            response = requests.get(url)
        
            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                # Cargar la imagen desde la respuesta
                img_data = response.content
                image = Image.open(BytesIO(img_data))
                image.thumbnail((600, 600))  # Ajustar el tamaño de la imagen
            
                # Convertir la imagen para usarla en Tkinter
                photo = ImageTk.PhotoImage(image)
            
                # Mostrar la imagen en el label
                label_imagen.config(image=photo)
                label_imagen.image = photo
            else:
                # Si no se puede cargar la imagen, mostrar la imagen de error 404
                url_404 = "https://http.cat/404"
                response_404 = requests.get(url_404)
                img_data_404 = response_404.content
                image_404 = Image.open(BytesIO(img_data_404))
                image_404.thumbnail((600, 600))
            
                # Convertir la imagen de error para usarla en Tkinter
                photo_404 = ImageTk.PhotoImage(image_404)
            
                # Mostrar la imagen de error 404
                label_imagen.config(image=photo_404)
                label_imagen.image = photo_404
    
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cargar Imagen de http.cat")

    # Crear un campo de entrada para el número de error HTTP
    label = tk.Label(root, text="Ingresa el número de error HTTP:")
    label.pack(pady=10)

    label = tk.Label(root, text="Lista de Errores: 100, 101, 200, 201, 202, 203, 204, 205, 206, 300,")
    label.pack(pady=10)

    label = tk.Label(root, text=" 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405,")
    label.pack(pady=10)

    label = tk.Label(root, text=" 406, 407, 408, 410, 411, 413, 314, 415, 416, 417, 418, 422, 423,")
    label.pack(pady=10)

    label = tk.Label(root, text=" 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 506, 507, 508, 510, 511")
    label.pack(pady=10)

    entry_error = tk.Entry(root)
    entry_error.pack(pady=5)

    # Crear un botón para cargar la imagen
    boton = tk.Button(root, text="Cargar Imagen", command=cargar_imagen)
    boton.pack(pady=10)

    # Crear un label para mostrar la imagen
    label_imagen = tk.Label(root)
    label_imagen.pack(pady=10)

    # Iniciar la interfaz gráfica
    root.mainloop()

elif opcion == 10:
    def get_size(path='.'):
        """Calcula el tamaño total en bytes de un archivo o carpeta."""
        total_size = 0
        if os.path.isfile(path):
            total_size = os.path.getsize(path)
        elif os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
        return total_size

    def format_size(size):
        """Formatea el tamaño en una forma más legible (KB, MB, GB)."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"

    # Directorio donde está el script
    print(r"Ejemplo: 'C:\Windows\System32'")
    current_directory = input("Ruta: ")

    print(f"\nTamaño de archivos y carpetas en {current_directory}:\n")

    files_and_sizes = []

    # Listar todos archivos y carpetas en el directorio actual
    for item in os.listdir(current_directory):
        path = os.path.join(current_directory, item)
        size = get_size(path)
        formatted_size = format_size(size)
        print(f"{item}: {formatted_size}")
        files_and_sizes.append((item, size))

    # Encontrar el archivo o carpeta más pesada
    most_heavy = max(files_and_sizes, key=lambda x: x[1])
    print(f"\nEl archivo o carpeta más pesado es '{most_heavy[0]}' con un tamaño de {format_size(most_heavy[1])}.")
