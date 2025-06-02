# calculadora.py

# Define una función llamada 'sumar' que recibe dos parámetros (a y b)
# y devuelve la suma de ambos
def sumar(a, b):
    return a + b


if __name__ == "__main__": #unidad de arranque o el punto de entrada principal 
    try:
        # Solicita al usuario que ingrese el primer número
        # El valor ingresado se convierte a tipo float (número decimal)
        num1 = float(input("Ingrese el primer número: "))

        # Solicita al usuario que ingrese el segundo número
        # También se convierte a tipo float
        num2 = float(input("Ingrese el segundo número: "))

        # Llama a la función 'sumar' con los dos números como argumentos
        # El resultado de la suma se guarda en la variable 'resultado'
        resultado = sumar(num1, num2)

        # Muestra en pantalla el resultado de la suma
        print("La suma es:", resultado)

    # Este bloque captura errores si el usuario escribe algo que no es un número
    except ValueError:
        print("Por favor, ingrese solo números.")
