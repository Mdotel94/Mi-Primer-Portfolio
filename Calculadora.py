#Definimos las funciones en una calculadora (suma, resta, multiplicacion, división)
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b): #En la división contamos que entre 0 marque error porque no es posible
    if b != 0:
        return a / b
    else:
        return "Error: No es posible dividir por cero"

#Definimos lo que vamos a ver en pantalla tipo "menú"
def calculadora():
    print("Calculadora básica")
    print("Operaciones posibles: +, -, *, /")
    
    num1 = float(input("Introduce un número: "))
    operacion = input("Introduce la operación (+, -, *, /): ")
    num2 = float(input("Introduce otro número: "))
    
    if operacion == '+':
        print("El Resultado es:", suma(num1, num2))
    elif operacion == '-':
        print("El Resultado es:", resta(num1, num2))
    elif operacion == '*':
        print("El Resultado es:", multiplicacion(num1, num2))
    elif operacion == '/':
        print("El Resultado es:", division(num1, num2))
    else:
        print("Operación no encontrada")

if __name__ == "__main__":
    calculadora()
