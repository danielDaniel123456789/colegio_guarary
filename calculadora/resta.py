# calculadora_resta.py

# Define una función llamada 'restar' que recibe dos parámetros (a y b)
# y devuelve la resta de ambos
def restar(a, b):
    return a - b


if __name__ == "__main__":  # unidad de arranque o el punto de entrada principal
    try:
        # Solicita al usuario que ingrese el primer número
        num1 = float(input("Ingrese el primer número: "))

        # Solicita al usuario que ingrese el segundo número
        num2 = float(input("Ingrese el segundo número: "))

        # Llama a la función 'restar' con los dos números como argumentos
        resultado = restar(num1, num2)

        # Muestra en pantalla el resultado de la resta
        print("La resta es:", resultado)

    # Este bloque captura errores si el usuario escribe algo que no es un número
    except ValueError:
        print("Por favor, ingrese solo números.")
