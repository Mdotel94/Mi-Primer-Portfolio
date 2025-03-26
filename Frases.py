#"input" Pide al usuario que introduzca palabras
frase = input("Introduce una frase: ")

#"Split" divide cada palabra usando espacio como separador
palabras = frase.split()

#"len" sirve para contar cada palabra
numero_de_palabras = len(palabras)

#"Print" muestra resultado a usuario.
print(f"La frase tiene {numero_de_palabras} palabras.")
