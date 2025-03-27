class Factorial:
    def __init__(self):
        pass  # No necesitamos atributos en este caso

    def run(self, min_val, max_val):
        """
        Calcula el factorial de los números en el rango [min_val, max_val]
        y devuelve un diccionario con los resultados.
        """
        factoriales = {}
        for num in range(min_val, max_val + 1):
            factoriales[num] = self.calcular_factorial(num)
        return factoriales
    
    def calcular_factorial(self, n):
        """ Calcula el factorial de un número usando recursión. """
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calcular_factorial(n - 1)


# Prueba del código
def main():
    min_val = int(input("Ingrese el valor mínimo: "))
    max_val = int(input("Ingrese el valor máximo: "))
    
    fact_obj = Factorial()
    resultados = fact_obj.run(min_val, max_val)
    
    for num, fact in resultados.items():
        print(f"Factorial de {num} es {fact}")


if __name__ == "__main__":
    main()
#para ejecutar el codigo se usa: python factorial_OOP.py
