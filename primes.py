#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

import math  # Importamos la librería para utilizar la función sqrt()

def es_primo(n):
    """
    Verifica si un número es primo.
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    """
    if n < 2:  # Los números menores a 2 no son primos
        return False
    # Verificamos divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False  # Si es divisible por otro número, no es primo
    return True  # Si no encontró divisores, es primo

# Solicitar al usuario el rango de números a evaluar
try:
    lower = int(input("Ingrese el valor inferior del rango: "))
    upper = int(input("Ingrese el valor superior del rango: "))

    # Verificar que los valores sean correctos
    if lower > upper:
        print("Error: El límite inferior no puede ser mayor que el superior.")
    else:
        print(f"Números primos entre {lower} y {upper}:")
        
        # Generamos la lista de números primos dentro del rango y la imprimimos
        primes = [num for num in range(lower, upper + 1) if es_primo(num)]
        print(primes)

except ValueError:
    # Manejo de error en caso de que el usuario ingrese un valor no numérico
    print("Error: Debe ingresar valores numéricos enteros.")