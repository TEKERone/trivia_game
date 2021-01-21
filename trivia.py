#Texto de bienvenida para quien juegue la trivia.
print("Bienvenido a mi trivia sobre computación\n")
print("Pondremos a prueba tus conocimientos\n")


puntaje=0
print("Tienes", puntaje, "puntos")

nombre = input("Ingresa tu nombre: ")

#Dar instrucciones sobre como jugar.
print("\nHola", nombre, "esponde las siguientes preguntas escribiendo la letra de la alternativa y presione 'Enter' para enviar tu respuesta:\n")

#Pregunta1
print("1) ¿Quien fue el creador de windows?\n")
print("a) Linus Torvalds")
print("b) Bill Gates")
print("c) Mark Zuckerberg")
print("d) Dennis Ritchie")

respuesta_1=input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b" "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "a":
    print("Incorrecto", nombre, "Linus es el creador de Linux")
elif respuesta_1 == "b":
    print("Muy bien", nombre,"!", "Bill es el creador de Windows")
elif respuesta_1 == "c":
    print("Incorrecto", nombre, "Linus es el creador de q")
else:
    print("Incorrecto", nombre, "Linus es el creador de x")

# if respuesta_1 == "b":
#     print("Correcto!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")

# #Pregunta2
# print("\n2) ¿Quien es el creador de Python?\n")
# print("a) Dennis Ritchie ")
# print("b) Larry Wall")
# print("c) Guido van Rossum")
# print("d) Yukihiro Matsumoto")

# respuesta_2=input("\nTu respuesta: ")

# if respuesta_2 == "c":
#     print("Respuesta Correcta!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")


# #Pregunta3
# print("\n3) ¿Que distro utiliza Linus Torvalds?\n")
# print("a) Arch Linux ")
# print("b) Debian")
# print("c) Gentoo")
# print("d) Fedora")

# respuesta_3=input("\nTu respuesta: ")
# if respuesta_3 == "d":
#     print("Respuesta Correcta!! 😄")
# else:
#     print("Respuesta Incorrecta! 😣")
