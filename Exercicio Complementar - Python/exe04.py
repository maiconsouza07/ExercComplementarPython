# Imprimir os divisores de um número:

def divisores(numero):
    return [i for i in range(1, numero + 1) if numero % i == 0]
print(divisores(12))
