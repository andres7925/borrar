def suma(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

def resta(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b

def division(a, b):
    """Divide dos números y retorna el resultado. Maneja división por cero."""
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b
def multiplicacion(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b --quedaron todos

# Ejemplo de uso
resultado = suma(5, 3)
print(resultado)  # Output: 8