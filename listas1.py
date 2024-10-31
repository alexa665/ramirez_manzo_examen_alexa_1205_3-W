print(" ")
print("Alexa Guadalupe Ramirez Manzo 1205 3-W")
print(" ")
#lista de materias o asignaturas
materias = ["Matemáticas", "lengua y comunicasion", "ecosistemas", "ingles", "metodologias"]
#indica las materias a repetir
materias_a_repetir = []
#bucle para ingresar todas tus calificasiones en cada materia
for materias in materias:
    nota = float(input(f"Ingrese tu calificasion en {materias}: "))
#funcion if para saber si si es correcto o no lo es 
    if nota < 5.0:
        materias_a_repetir.append(materias)
#print para ingresar felisitasiones y for, bucle para las materias reprobadas
print("\nmaterias que debes repetir:" if materias_a_repetir else"¡Que bien! Has aprobado todas las materias.")
for materias in materias_a_repetir:
    print(f"- {materias}")
