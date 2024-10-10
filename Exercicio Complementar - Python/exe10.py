# Ler 10 números e imprimir a soma, o maior e o menor:

def ler_numeros():
    numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]
    return sum(numeros), max(numeros), min(numeros)
soma, maior, menor = ler_numeros()
print(f"Soma: {soma}, Maior: {maior}, Menor: {menor}")
