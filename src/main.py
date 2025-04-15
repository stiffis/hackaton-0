
  GNU nano 8.3                                                                                maimport re
import re
#ACTUALIZE LA FUNCION Y ARREGLE UNOS CONFLICTOS
# Funciones para cada operación básica
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


# Función que maneja la evaluación de la expresión
def calculate(expression):
    # Eliminar los espacios extra
    expression = expression.replace(" ", "")

    # Verificar si la expresión está vacía o contiene caracteres no válidos
    if not expression:
        raise ValueError("La entrada está vacía.")

    if re.search(r'[^0-9+\-*/(). ]', expression):
        raise ValueError("La expresión contiene caracteres no válidos.")

    # Agregar un signo '+' al principio si la expresión empieza con un número negativo
    expression = re.sub(r'(^|\+|-|\*|/|^)\s*(-\d)', r'\1\2', expression)

    # Evaluar las operaciones de manera secuencial (prioridad de operaciones)
    while '(' in expression:
        # Resolver expresiones entre paréntesis
        expression = re.sub(r'\(([^()]+)\)', lambda m: str(calculate(m.group(1))), expression)

    # Evaluar multiplicación y división primero
    while '*' in expression or '/' in expression:
        expression = re.sub(r'(\d+(\.\d+)?)\s*([*/])\s*(\d+(\.\d+)?)',
                            lambda m: str(operar(m.group(1), m.group(3), m.group(4))), expression)

    # Evaluar suma y resta
    while '+' in expression or '-' in expression:
        expression = re.sub(r'(\d+(\.\d+)?)\s*([+-])\s*(\d+(\.\d+)?)',
                            lambda m: str(operar(m.group(1), m.group(3), m.group(4))), expression)

    return float(expression)


# Función que ejecuta la operación según el operador
def operar(a, operador, b):
    a = float(a)
    b = float(b)
    if operador == '+':
        return sumar(a, b)
    elif operador == '-':
        return restar(a, b)
    elif operador == '*':
        return multiplicar(a, b)
    elif operador == '/':
        return dividir(a, b)









