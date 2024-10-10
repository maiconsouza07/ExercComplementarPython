# Calcular as raízes da equação do segundo grau:

import math

def equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    elif delta == 0:
        return -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
print(equacao_segundo_grau(1, -5, 6))
