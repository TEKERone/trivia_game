#Texto de bienvenida para quien juegue la trivia.
print("Bienvenido a mi trivia sobre computación\n")
print("Pondremos a prueba tus conocimientos\n")

puntaje=0
print("Tienes", puntaje, "puntos")
nombre = input("Ingresa tu nombre: ")

#Indicar instrucciones sobre como jugar.
print("\nHola", nombre, "Responde las siguientes preguntas escribiendo la letra de la alternativa y presione 'Enter' para enviar tu respuesta:\n")

##Inicio de Preguntas##
#Pregunta1
print("1) ¿Quien fue el creador de windows?\n")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Steve Jobs")
respuesta_1=input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "a":
    print("Incorrecto 😣")
elif respuesta_1 == "b":
    puntaje += 10
    print("Excelente 🥳")
elif respuesta_1 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta2
print("2) ¿Quien es el creador de Python?\n")
print("a) Dennis Ritchie ")
print("b) Larry Wall")
print("c) Guido van Rossum")
print("d) Yukihiro Matsumoto")
respuesta_2=input("\nTu respuesta: ")
while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_2 == "a":
    print("Incorrecto 😣")
elif respuesta_2 == "b":
    print("Incorrecto 😣")
elif respuesta_2 == "c":
    puntaje += 10
    print("Muy bien 🥳")
else:
    print("Incorrecto 😣")

#Pregunta3
print("3) ¿Que distro utiliza Linus Torvalds?\n")
print("a) Fedora")
print("b) Debian")
print("c) Gentoo")
print("d) Arch Linux")
respuesta_3=input("\nTu respuesta: ")
while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_3 == "a":
    puntaje += 10
    print("Perfecto 🥳")
elif respuesta_3 == "b":
    print("Incorrecto 😣")
elif respuesta_3 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta4
print("4) ¿La Web 2.0 es un elemento que permite?\n")
print("a) Concepto de las tecnologías de la información y comunicación que se fundamenta en crear y compartir recursos de diferente naturaleza")
print("b) Herramienta para solo enviar correos electrónicos")
print("c) Plataforma de alta tecnología de computo para compartir recursos en las redes basadas en Cisco")
print("d) todas las anteriores")
respuesta_4=input("\nTu respuesta: ")
while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_4 == "a":
    puntaje += 10
    print("Excelente 🥳")
elif respuesta_4 == "b":
    print("Incorrecto 😣")
elif respuesta_4 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta5
print("5) ¿Qué es hipertexto e hipermedia?\n")
print("a) Son texto o gráficos que tienen vínculos incrustados")
print("b) Son objetos o equipos que forman el Internet")
print("c) Son documentos con información de otros sitios Web, películas, fotografías o sonidos")
print("d) Ninguna de las anteriores")
respuesta_5=input("\nTu respuesta: ")
while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_5 == "a":
    puntaje += 10
    print("Muy bien 🥳")
elif respuesta_5 == "b":
    print("Incorrecto 😣")
elif respuesta_5 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta6
print("6) ¿Dentro del lenguaje de control de datos la sentencia GRANT de SQL hace?\n")
print("a) Concede los derechos de acceso a un objeto")
print("b) Revoca los derechos de acceso a un objeto")
print("c) Concede los derechos de conexión al host.")
print("d) Revoca los derechos de conexión al host")
respuesta_6=input("\nTu respuesta: ")
while respuesta_6 not in ("a", "b", "c", "d"):
    respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_6 == "a":
    puntaje += 10
    print("Perfecto 🥳")
elif respuesta_6 == "b":
    print("Incorrecto 😣")
elif respuesta_6 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta7
print("7) ¿La correspondencia dinámica es posible realizarla gracias a?\n")
print("a) La utilización del ensamblador para la programación")
print("b) El planificador de procesos")
print("c) Los compiladores especializados ")
print("d) La unidad de gestión de memoria (MMU)")
respuesta_7=input("\nTu respuesta: ")
while respuesta_7 not in ("a", "b", "c", "d"):
    respuesta_7 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_7 == "a":
    print("Incorrecto 😣")
elif respuesta_7 == "b":
    print("Incorrecto 😣")
elif respuesta_7 == "c":
    print("Incorrecto 😣")
else:
    puntaje += 10
    print("Excelente 🥳")

#Pregunta8
print("8) ¿Cual de las siguientes opciones corresponden a tipos de Sistemas Operativos Existentes en el mercado?\n")
print("a) Windows, Mac Os, Linux")
print("b) Office, Word, Excel")
print("c) Mother Board, Mouse, Teclado")
print("d) Internet, Servidor, Conexión FTP")
respuesta_8=input("\nTu respuesta: ")
while respuesta_8 not in ("a", "b", "c", "d"):
    respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_8 == "a":
    puntaje += 10
    print("Muy bien 🥳")
elif respuesta_8 == "b":
    print("Incorrecto 😣")
elif respuesta_8 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta9
print("9) ¿En que año nase el primer computador?\n")
print("a) 1975")
print("b) 1974")
print("c) 2000")
print("d) 1985")
respuesta_9=input("\nTu respuesta: ")
while respuesta_9 not in ("a", "b", "c", "d"):
    respuesta_9 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_9 == "a":
    print("Incorrecto 😣")
elif respuesta_9 == "b":
    puntaje += 10
    print("Perfecto 🥳")
elif respuesta_9 == "c":
    print("Incorrecto 😣")
else:
    print("Incorrecto 😣")

#Pregunta10
print("10) ¿Como se lla la compañia que lanso el primer microprosesador?\n")
print("a) Mediatek")
print("b) AMD")
print("c) Intel")
print("d) Qualcomm")
respuesta_10=input("\nTu respuesta: ")
while respuesta_10 not in ("a", "b", "c", "d"):
    respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_10 == "a":
    print("Incorrecto 😣")
elif respuesta_10 == "b":
    print("Incorrecto 😣")
elif respuesta_10 == "c":
    puntaje += 10
    print("Muy bien 🥳")
else:
    print("Incorrecto 😣")

#Congratulations
print("🎊 Gracias!! 🎊", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos!! 🤓")


