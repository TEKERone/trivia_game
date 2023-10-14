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
    print("Incorrecto", nombre, "Linus es el creador de Linux")
elif respuesta_1 == "b":
    print("Muy bien", nombre,"!", "Bill Gates es el creador de Windows")
elif respuesta_1 == "c":
    print("Incorrecto", nombre, "Mark Zuckerberg es el creador de Meta")
else:
    print("Incorrecto", nombre, "Steve Jobs es el creador de Apple")

# if respuesta_1 == "b":
#     print("Correcto!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")

# #Pregunta2
print("\n2) ¿Quien es el creador de Python?\n")
print("a) Dennis Ritchie ")
print("b) Larry Wall")
print("c) Guido van Rossum")
print("d) Yukihiro Matsumoto")
# respuesta_2=input("\nTu respuesta: ")

# if respuesta_2 == "c":
#     print("Respuesta Correcta!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")
respuesta_2=input("\nTu respuesta: ")
while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "a":
    print("Incorrecto", nombre, "Dennis Ritchie es el creador del lenguaje de programación C")
elif respuesta_2 == "b":
    print("Incorrecto", nombre, "Larry Wall es el creador del lenguaje de programación Perl")
elif respuesta_2 == "c":
    print("Muy bien", nombre,"!", "Guido van Rossum es el creador del lenguaje de programación Python")
else:
    print("Incorrecto", nombre, "Yukihiro Matsumoto es el creador del lenguaje de programación Ruby")


# #Pregunta3
print("\n3) ¿Que distro utiliza Linus Torvalds?\n")
print("a) Fedora")
print("b) Debian")
print("c) Gentoo")
print("d) Arch Linux")

respuesta_3=input("\nTu respuesta: ")
while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "a":
    print("Muy bien", nombre,"!", "Linus Torvalds utiliza Fedora")
elif respuesta_3 == "b":
    print("Incorrecto", nombre, "Linus Torvalds no utiliza Debian")
elif respuesta_3 == "c":
    print("Incorrecto", nombre, "Linus Torvalds no utiliza Gentoo")
else:
    print("Incorrecto", nombre, "Linus Torvalds no utiliza Arch Linux")

# respuesta_3=input("\nTu respuesta: ")
# if respuesta_3 == "d":
#     print("Respuesta Correcta!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")


