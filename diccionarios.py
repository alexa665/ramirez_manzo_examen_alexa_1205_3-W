print(" ")
print("Alexa Guadalupr Ramirez Manzo 1205 3-W")
# Diccionario con los créditos de las materias
creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Muestra los créditos de cada materia y calcula el total
total_creditos = sum(credito for credito in creditos.values())
for materias, credito in creditos.items():
    print(f"{materias} tiene {credito} créditos")

print(f"\nlos créditos del curso son: {total_creditos}")
