print(" ")
print("Alexa Guadalupe Ramirez manzo 1205 3-W")
print(" ")
# Pregunta a la persona por sus datos y se ponen en un diccionario
persona = {
    'nombre': input("Ingrese su nombre: "),
    'edad': int(input("Ingrese su edad: ")),
    'direccion': input("Ingrese su dirección: "),
    'telefono': input("Ingrese su número de teléfono: ")
}

# Muestra el mensaje con los datos de la persona
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su número de teléfono es {persona['telefono']}.")


