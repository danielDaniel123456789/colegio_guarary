# calculadora_division.py

# Define una función llamada 'dividir' que recibe dos parámetros (a y b)
# y devuelve el resultado de dividir a entre b
def dividir(a, b):
    return a / b


if __name__ == "__main__":  # unidad de arranque o el punto de entrada principal
    try:
        # Solicita al usuario que ingrese el primer número
        num1 = float(input("Ingrese el primer número: "))

        # Solicita al usuario que ingrese el segundo número
        num2 = float(input("Ingrese el segundo número: "))

        # Verifica que el divisor no sea cero
        if num2 == 0:
            print("No se puede dividir entre cero.")
        else:
            # Llama a la función 'dividir' con los dos números como argumentos
            resultado = dividir(num1, num2)

            # Muestra en pantalla el resultado de la división
            print("La división es:", resultado)

    # Este bloque captura errores si el usuario escribe algo que no es un número
    except ValueError:
        print("Por favor, ingrese solo números.")
