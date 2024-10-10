# Calcular o MDC de dois números (recursivo):

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
print(mdc(54, 24))
