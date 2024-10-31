print("")
print("Alexa Guadalupe Ramirez Manzo 1205 3-W")
print(" ")
# Lista de materias
materias = ["lengua y comunicasion", "ingles", "matematicas", "ecosistemas", "metodologias"]
#bucle en el cual te pregunta las materia y repite para ingresar tu calificasion en cada una
for materia in materias:
    calif = float(input(f"Ingrese la calif de la {materia}: "))
    print(f"En {materia} has sacado {calif}")
