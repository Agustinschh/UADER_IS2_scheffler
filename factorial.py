#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    """Calcula el factorial de un número entero no negativo."""
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def procesar_rango(entrada):
    """Convierte una entrada en formato de rango (ej. '4-8', '-10', '5-') en valores numéricos."""
    try:
        # Rango con inicio y fin (ej. '4-8')
        if '-' in entrada and entrada.count('-') == 1:
            partes = entrada.split('-')
            if partes[0] == '':  # Caso '-10' (de 1 a 10)
                return 1, int(partes[1])
            elif partes[1] == '':  # Caso '5-' (de 5 a 60)
                return int(partes[0]), 60
            else:  # Caso '4-8'
                return int(partes[0]), int(partes[1])
        else:
            # Si no hay un formato válido, intentamos convertir a entero
            num = int(entrada)
            return num, num  # Si es un número solo, calcula solo ese factorial
    except ValueError:
        return None  # Si hay un error en la conversión, se retorna None

# Obtener entrada del usuario (argumento o input manual)
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Procesar entrada y calcular factoriales
rango = procesar_rango(entrada)

if rango:
    inicio, fin = rango
    if inicio > fin:
        print("Error: El rango de valores es inválido (el inicio no puede ser mayor que el fin).")
        sys.exit(1)

    # Calcular y mostrar factoriales en el rango indicado
    for num in range(inicio, fin + 1):
        result = factorial(num)
        if result is not None:
            print(f"Factorial {num}! es {result}")

else:
    print("Error: Entrada inválida. Debe ingresar un número o un rango válido.")
    sys.exit(1)


